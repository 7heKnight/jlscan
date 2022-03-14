import requests

from jlscan.utils import io_utils


def status_code_handler():
    status = requests.status_code
    if status == 200:
        pass
    elif status == 301:
        #HTTPS handler
        pass
    else:
        io_utils.error_msg('Error!')

