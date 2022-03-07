from jlscan.core.utils import *


def user_selection():
    user_sel = 0
    print('----------------------')
    print('1. Enter target URL.')
    print('2. Check for update.')
    print('3. Exit The program.\n')
    while True:
        try:
            wait_msg('Enter option: ')
            user_sel = int(input())
            if user_sel == 1:
                pass
                break
            elif user_sel == 2:

                break
            elif user_sel == 3:
                error_msg('Closing program. Bye Bye!')
                break
            else:
                error_msg('Option not found!')
        except ValueError:
            error_msg('Integer only')



user_selection()