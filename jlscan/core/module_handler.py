import requests

from jlscan.utils import utils


def status_code_handler():
    status = requests.status_code
    if status == 200:
        pass
    elif status == 301:
        #HTTPS handler
        pass
    else: utils.error_msg('Error!')