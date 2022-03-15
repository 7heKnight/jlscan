DIRLIST = ('/administrator/components',
           '/administrator/templates',
           '/administrator/modules',
           '/images/stories',
           '/images/banners',
           '/components',
           '/templates',
           '/templates',
           '/language',
           '/includes',
           '/modules',
           '/images',
           '/media',
           '/cache',
           '/tmp')

KEYWORDS = ('Index of', 'Last modified')


def directory_listing(io_utils, url: str):
    print('\n' + '[+]Directory Listing: ')
    for endpoint in DIRLIST:
        response = io_utils.get_html_data(url + endpoint, '')
        print(response)

        #
        # for string in soup.strings:
        #     string = string.strip()
        #     if string.startswith( keyWord[0]) or string.endswith( keyWord[1]):
        #         print('Founded')
    return False


directory_listing('http://192.168.2.130')
