import argparse

from utils.utils import font
from update.update_core import update_db
from utils.utils import error_msg

# def user_selection():
#     try:
#         utils.banner()
#         print('--------------------------------------------------------------------------\n')
#         print(f'{utils.font.blue}Option 1:{utils.font.default} Scan Joomla server.')
#         print(f'{utils.font.yellow}Option 2:{utils.font.default} Update database.')
#         print(f'{utils.font.red}Option 3:{utils.font.default} Exit The program.\n')
#         while True:
#             try:
#                 utils.wait_msg('Enter option: ')
#                 choice = int(input())
#                 if choice == 1:  # In this option, add more option for output
#                     parse.parse_url('192.168.2.130')
#                     return user_selection
#                 elif choice == 2:
#                     print(f'-------[ {utils.font.purple}Update option{utils.font.default} ]-------')
#                     update_db()
#                     return user_selection()
#                 elif choice == 3:
#                     utils.error_msg('Closing program. Bye Bye!')
#                     break
#                 else:
#                     utils.error_msg('Option not found!')
#             except ValueError:
#                 utils.error_msg('Integer only')
#     except KeyboardInterrupt:
#         print()
#         utils.error_msg('Keyboard Interruption. Terminated!')


if __name__ == '__main__':
    print(f'       _ _     ____                       |        {font.purple}{font.under_line}Team Members:{font.default}')
    print(f'      | | |   / ___|  ___ __ _ _ __       | --[{font.turquoise}    Ly Tuan Kiet{font.default}    ]--')
    print(f'   _  | | |   \___ \ / __/ _` | \'_ \      | --[{font.turquoise}  Nguyen Phuong Duy{font.default} ]--')
    print(f'  | |_| | |___ ___) | (_| (_| | | | |     | --[{font.turquoise} Nguyen Lam Y Khang{font.default} ]--')
    print(f'   \___/|_____|____/ \___\__,_|_| |_|     | --[{font.turquoise}  Trinh Quang Thai{font.default}  ]--')
    print(f' ========================================================================={font.default}')
    print(f'  ---[ {font.white}Project name: {font.yellow}Joomla CMS Scanner{font.default} ]---')
    print(f'  ---[ {font.white}Project link: {font.blue}{font.under_line}https://github.com/7heKnight/jlscan/{font.default} ]---\n')

    """
    Core functionality
    
    
    """
    parser = argparse.ArgumentParser(usage='jlscan.py [options]')
    parser.add_argument('-u', action='store', dest='url', help='Domain/URL for scanning', type=str)  # ok
    # update_option = parser.add_argument_group('Update setting:')

    parser.add_argument('--update', action='store_const', const='update', dest='update',
                        help='Update the database')  # ok
    parser.add_argument('--joomla-check', action='store_const', const='version_check', dest='version_check',
                        help='Check does it Joomla')
    parser.add_argument('--version-check', action='store_const', const='version_check', dest='version_check',
                        help='Check version of Joomla')

    """
    Customize the requesst
    
    
    """

    # parser.add_argument('--user-agent', action='store_const', const='user_agent', dest='user_agent',
    #                     default='Mozilla/5.0',
    #                     help='Select specific User-Agent header')
    # parser.add_argument('--cookie', action='store_const', const='cookie', dest='cookie',
    #                     default=None,
    #                     help='Specific Cookie header')
    # parser.add_argument('--random-agent', action='store_const', const='random_agent', dest='random_agent', default=False,
    #                     help='Random User-Agent')
    """
    Finding dictionary attack for finding administrator credentials
    
    
    """

    # parser.add_argument('--username', action='store', dest='usernames', default='',help='Username for dictionary attack')
    # parser.add_argument('--users-list', action='store', dest='users_list', default=None, help='Users list for dictionary attack')
    # parser.add_argument('--passwords-list', action='store', dest='passwords_list', default=None,
    #                     help='Passwords list for dictionary attack')
    args = parser.parse_args()

    try:
        if args.update:
            update_db()
        elif args.url != None:
            print('do sth')
        else:
            parser.print_help()
    except IOError:
        error_msg('Keyboard Interruption. Terminated!')
