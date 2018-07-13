def menu():
    print('''

 /@@       /@@           /@@                                                  
| @@      |__/          | @@                                                  
| @@       /@@ /@@@@@@@ | @@  /@@@@@@   /@@@@@@   /@@@@@@   /@@@@@@   /@@@@@@ 
| @@      | @@| @@__  @@| @@ /@@__  @@ /@@__  @@ /@@__  @@ /@@__  @@ /@@__  @@
| @@      | @@| @@  \ @@| @@| @@  \ @@| @@  \ @@| @@  \ @@| @@@@@@@@| @@  \__/
| @@      | @@| @@  | @@| @@| @@  | @@| @@  | @@| @@  | @@| @@_____/| @@      
| @@@@@@@@| @@| @@  | @@| @@|  @@@@@@/|  @@@@@@@|  @@@@@@@|  @@@@@@@| @@      
|________/|__/|__/  |__/|__/ \______/  \____  @@ \____  @@ \_______/|__/      
                                       /@@  \ @@ /@@  \ @@                    
                                      |  @@@@@@/|  @@@@@@/                    
                                       \______/  \______/                                                            

    |------------------------------|
    |           Commands           |
    |------------------------------|
    | start                        |
    |------------------------------|
    | set_email                    |
    |------------------------------|
    | check_email                  |
    |------------------------------|
    | send_log                     |
    |------------------------------|
    | check_log                    |
    |------------------------------|
    | remove_log                   |
    |------------------------------|
    | stop                         |
    |------------------------------|
    | help                         |
    |------------------------------|
    | quit                         |
    |------------------------------|
''')


def hints():
    print('''start - script runs in terminal
set_email - sets needed credentials to send mails
check_email - checks email credentials
send_log - sends log file on given email address
check_log - prints out log file content
remove_log - clears log file content
quit - safely quits script''')


def message_to_screen(msg, positive):
    if positive:
        print('[+]', msg)
    else:
        print('[-]', msg)


def invalid_command():
    message_to_screen('No such option', False)
