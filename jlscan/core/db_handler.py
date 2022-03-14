import requests
import json
import re

from jlscan.utils import io_utils
from jlscan.core.version_cmp import compare_versions


def __get_version(url: str):
    source = requests.get(url).text
    version = re.search(r'<version>(.+?)</version>', source)
    if not version:
        utils.error_msg('Version not found!/n')
        return 'Version not found!'
    return version.group(1)


def match_vuln(url: str):
    databases = open('../database/core.jdb').readlines()
    target_version = __get_version(url)
    for i in databases:
        data = json.loads(i)
        if data['version'] != '':
            compare_versions(target_version=target_version, db_versions=data['version'])
