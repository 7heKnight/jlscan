from utils.version_handler import check_version
from update.update_core import update_db
from core.version_cmp import compare_versions
from utils import io_utils


def user_selection():
    try:
        io_utils.banner()
        print('--------------------------------------------------------------------------\n')
        print(f'{io_utils.font.blue}Option 1:{io_utils.font.default} Scan Joomla server.')
        print(f'{io_utils.font.yellow}Option 2:{io_utils.font.default} Update database.')
        print(f'{io_utils.font.red}Option 3:{io_utils.font.default} Exit The program.\n')
        while True:
            try:
                choice = io_utils.input_integer('Enter option: ')
                if choice == 1:  # In this option, add more option for output
                    url = io_utils.input_url()

                    # Core Vulnerable check via version
                    core_list = open('database/core.jdb', 'r').readlines()
                    scanned_version = check_version(io_utils, url, compare_versions, core_list)

                elif choice == 2:
                    print(f'-------[ {io_utils.font.purple}Update option{io_utils.font.default} ]-------')
                    update_db(io_utils)
                    return user_selection()
                elif choice == 3:
                    io_utils.error_msg('Closing program. Bye Bye!\n')
                    break
                else:
                    io_utils.error_msg('Option not found!\n')
            except ValueError as v:
                print(v)
                io_utils.error_msg('Integer only\n')
            print()
    except KeyboardInterrupt:
        io_utils.error_msg('Keyboard Interruption. Terminated!')


if __name__ == '__main__':
    user_selection()
