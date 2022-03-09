import requests


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

    if not 'http' in url:
        url = 'http://' + url
    if not url.endswith('/'):
        url = url + '/'
    return url


def html_unescape(url: str):
    # """
    #     Returns (basic conversion) HTML unescaped value
    #
    #     >>> html_unescape('&lt;script&gt;') == '<script>'
    #     True
    # """

    retVal = url

    if url:
        replacements = (("&lt;", '<'), ("&gt;", '>'), ("&quot;", '"'), ("&nbsp;", ' '), ("&amp;", '&'), ("&apos;", "'"))
        for code, value in replacements:
            retVal = retVal.replace(code, value)

    return retVal


def get_html_data(url: str, headers: str):
    try:
        response = requests.get(url, headers, timeout=15)
        response.text
    except TimeoutError:
        error_msg('Connection time out')
    return response


def post_data(url: str, data: str, headers: str):
    try:
        response = requests.post(url, data, headers, timeout=15)
    except TimeoutError:
        error_msg('Connection time out')
    return response


def get_cookie(url: str):
    '''
    Get the cookie if the server response with Set-Cookie header

    '''
    response = get_endpoint(url).headers
    full_cookie = response['set-cookie'].split(';')
    cookie = full_cookie[0]
    return cookie


# status code
# status = response.status_code
# if status == 200:
#     wait_msg('Waiting...')
# else:
#     warn_msg('Could not request')

# def crawler_vulnExtension(url: str):
#     response = get_endpoint(url, header)
#     json_raw = json.loads(response.text)
#     json_data = json_raw['data']['items']


if __name__ == '__main__':
    url = '121.123.231.121'
    print(format_url(url))
