class font:
    default = '\033[0m'
    black = '\033[30m'
    red = '\033[31m'
    yellow = '\033[33m'
    green = '\033[32m'
    turquoise = '\033[96m'
    white = '\033[97m'
    orange = '\033[226m'
    purple = '\033[35m'
    pink = '\033[95m'
    blue = '\033[94m'
    gray = '\033[90m'
    under_line = '\033[4m'


def error_msg(message: str):
    print(f'[{font.red}-{font.default}] {message}', end='')


def success_msg(message: str):
    print(F'[{font.green}+{font.default}] {message}', end='')


def wait_msg(message: str):
    print(f'[{font.turquoise}*{font.default}] {message}', end='')


def warn_msg(message: str):
    print(f'[{font.yellow}!{font.default}] {message}', end='')


def link_msg(message: str):
    message = f'{font.blue}{font.under_line}{message}{font.default}'
    return message


def banner():
    print(f'       _ _     ____                       |        {font.purple}{font.under_line}Team Members:{font.default}')
    print(f'      | | |   / ___|  ___ __ _ _ __       | --[{font.turquoise}    Ly Tuan Kiet{font.default}    ]--')
    print(f'   _  | | |   \___ \ / __/ _` | \'_ \      | --[{font.turquoise}  Nguyen Phuong Duy{font.default} ]--')
    print(f'  | |_| | |___ ___) | (_| (_| | | | |     | --[{font.turquoise} Nguyen Lam Y Khang{font.default} ]--')
    print(f'   \___/|_____|____/ \___\__,_|_| |_|     | --[{font.turquoise}  Trinh Quang Thai{font.default}  ]--')
    print(f' ========================================================================={font.default}')
    print(f'  ---[ {font.white}Project name: {font.yellow}Joomla Scanner{font.default} ]---')
    print(f'  ---[ {font.white}Project link: {font.blue}{font.under_line}https://github.com/7heKnight/jlscan/{font.default} ]---')
