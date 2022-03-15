def __get_source(io_utils, url):

    version_location = ['administrator/components/com_content/content.xml',
                        'administrator/components/com_plugins/plugins.xml',
                        'administrator/components/com_media/media.xml',
                        'administrator/manifests/files/joomla.xml',
                        'mambots/content/moscode.xml',
                        'language/en-GB/en-GB.xml']

    import requests
    for version in version_location:
        source = requests.get(url + version)
        if source.ok:
            io_utils.success_msg(f'Found Version Directory in: {source.url} \n')
            return source.text
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
