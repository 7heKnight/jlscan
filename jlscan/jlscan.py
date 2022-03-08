import utils
import update_core
import requests


def check_valid_url():
    url = ''
    try:
        utils.wait_msg('Enter target URL: ')
        url = requests.get(input())
    except IOError:
        utils.error_msg('Invalid URL!\n')
        return check_valid_url()
    finally:
        return url


def user_selection():
    try:
        utils.banner()
        print('--------------------------------------------------------------------------\n')
        print(f'{utils.font.blue}Option 1:{utils.font.default} Scan Joomla server.')
        print(f'{utils.font.yellow}Option 2:{utils.font.default} Update database.')
        print(f'{utils.font.red}Option 3:{utils.font.default} Exit The program.\n')
        while True:
            try:
                utils.wait_msg('Enter option: ')
                user_sel = int(input())
                if user_sel == 1: # In this option, add more option for output
                    check_valid_url()
                    return user_selection
                elif user_sel == 2:
                    print(f'-------[ {utils.font.purple}Update option{utils.font.default} ]-------')
                    update_core()
                    return user_selection()
                elif user_sel == 3:
                    utils.error_msg('Closing program. Bye Bye!')
                    break
                else:
                    utils.error_msg('Option not found!')
            except ValueError:
                utils.error_msg('Integer only')
    except KeyboardInterrupt:
        print()
        utils.error_msg('Keyboard Interruption. Terminated!')

if __name__ == '__main__':
    user_selection()