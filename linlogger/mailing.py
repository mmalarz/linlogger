import smtplib

from . import cli

email_to = ''
email_from = ''
email_password = ''
smtp_host = ''
smtp_port = ''


def check_credentials():
    print('Email to:', email_to)
    print('Email from:', email_from)
    print('Email password:', email_password)
    print('SMTP host:', smtp_host)
    print('SMTP port:', smtp_port)


def set_credentials():
    global email_to
    global email_from
    global email_password
    global smtp_host
    global smtp_port

    email_to = input('Email to: ')
    email_from = input('Email from: ')
    email_password = input('Email password: ')
    smtp_host = input('SMTP host: ')
    smtp_port = input('SMTP port: ')


def send_file(file_path):
    if email_to and email_from and email_password and smtp_host and smtp_port:
        try:
            with open(file_path, 'r') as file:
                msg = file.read()
        except FileNotFoundError:
            cli.message_to_screen('Cannot open file', False)
            return
        try:
            server = smtplib.SMTP(smtp_host, smtp_port)
            server.starttls()
            server.login(email_from, email_password)
            server.sendmail(email_from, email_to, msg)
            server.quit()
            cli.message_to_screen('Mail sent', True)
        except smtplib.SMTPServerDisconnected:
            cli.message_to_screen('Server Disconnected Error: check your smtp server details', False)
        except smtplib.SMTPConnectError:
            cli.message_to_screen('Connection Error: can\'t connect with specified server.', False)
        except smtplib.SMTPAuthenticationError:
            cli.message_to_screen('Authentication Error: check your email credentials', False)
        except:
            cli.message_to_screen('An error occurred', False)
    else:
        cli.message_to_screen('Email details not specified', False)
