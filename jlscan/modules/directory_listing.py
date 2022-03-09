
from jlscan.utils import utils
from jlscan.core.module_handler import status_code_handler

DIRLIST = ('/administrator/components', '/components', '/administrator/modules', '/modules', '/administrator/templates',
           '/templates', '/cache', '/images', '/includes', '/language', '/media', '/templates', '/tmp',
           '/images/stories',
           '/images/banners')
KEYWORDS = ('Index of', 'Last modified')


def directory_listing(url: str):
    print('\n' + '[+]Directory Listing: ')
    for endpoint in DIRLIST:
        response = utils.get_html_data(url + endpoint, '')
        print(response)

        #
        # for string in soup.strings:
        #     string = string.strip()
        #     if string.startswith( keyWord[0]) or string.endswith( keyWord[1]):
        #         print('Founded')
    return False

directory_listing('http://192.168.2.130')
