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
    print(f'[{font.green}+{font.default}] {message}', end='')


def wait_msg(message: str):
    print(f'[{font.turquoise}*{font.default}] {message}', end='')


def warn_msg(message: str):
    print(f'[{font.yellow}!{font.default}] {message}', end='')


def link_msg(message: str):
    message = f'{font.blue}{font.under_line}{message}{font.default}'
    return message

def format_url(url: str):
    # """
    #         Returns (basic conversion) HTML unescaped value
    #
    #         E.g: parse_url('192.168.2.130') == 'http://192.168.2.130/'
    #         str
    # """

    retVal = url
    if not 'http' in url:
        retVal = 'http://' + url
    return retVal