def __get_source(io_utils, url):
    import requests
    source = requests.get(url + '/administrator/manifests/files/joomla.xml')
    if source.ok:
        return source.text
    else:
        io_utils.error_msg('Version not found!\n')
        return 'Version not found!'


def __get_version(io_utils, source):
    from re import search
    version = search(r'<version>(.+?)</version>', source)

    if version:
        return version.group(1)
    else:
        io_utils.error_msg('Version not found!\n')
        return 'Version not found!'


def check_version(io_utils, url, compare_versions, core_list: list):
    core_vuln_list = []
    target_version = __get_version(io_utils, __get_source(io_utils, url))
    if target_version == 'Version not found!':
        return 'Version not found!'
    else:
        print()
        print('========================= Core Vulnerable Matched =========================')
        io_utils.wait_msg(f'Target version: {target_version}\n')
        import json
        for core in core_list:
            version = json.loads(core).get('version')
            if compare_versions(target_version, version):
                if json.loads(core).get('CVE') == '':
                    io_utils.warn_msg(f"{json.loads(core).get('name')}")
                    print()
                else:
                    io_utils.warn_msg(f"{json.loads(core).get('CVE')} - {json.loads(core).get('name')}")
                    print()
                core_vuln_list.append(core)
    return target_version, core_vuln_list


# def main():
#     core_vuln_list = []
#     from jlscan.core.version_handler import compare_versions
#     core_list = open('../database/core.jdb', 'r').readlines()
#     target_version = __get_version(__get_source('https://www.nissegaard.com/'))
#     if target_version == 'Version not found!':
#         return 'Version not found!'
#     else:
#         utils.wait_msg(f'Target version: {target_version}\n')
#         import json
#         print('\n========================= Matching core exploit =========================\n')
#         for core in core_list:
#             version = json.loads(core).get('version')
#             if compare_versions(target_version, version):
#                 if json.loads(core).get('CVE') == '':
#                     utils.warn_msg(f"{json.loads(core).get('name')}")
#                     print()
#                 else:
#                     utils.warn_msg(f"{json.loads(core).get('CVE')} - {json.loads(core).get('name')}")
#                     print()
#                 core_vuln_list.append(core)
