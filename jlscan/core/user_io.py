from jlscan.core.updater.update_core import *
from jlscan.core.utils import *
import requests


def check_valid_url():
    url = ''
    try:
        wait_msg('Enter target URL: ')
        url = requests.get(input())
    except IOError:
        error_msg('Invalid URL!\n')
        return check_valid_url()
    finally:
        return url


def user_selection():
    try:
        banner()
        print('--------------------------------------------------------------------------\n')
        print('1. Scan Joomla server.')
        print('2. Check for update.')
        print('3. Exit The program.\n')
        while True:
            try:
                wait_msg('Enter option: ')
                user_sel = int(input())
                if user_sel == 1: # In this option, add more option for output
                    check_valid_url()
                    return user_selection
                elif user_sel == 2:
                    print(f'-------[ {font.purple}Update option{font.default} ]-------')
                    update_core()
                    return user_selection()
                elif user_sel == 3:
                    error_msg('Closing program. Bye Bye!')
                    break
                else:
                    error_msg('Option not found!')
            except ValueError:
                error_msg('Integer only')
    except KeyboardInterrupt:
        print()
        error_msg('Keyboard Interruption. Terminated!')
