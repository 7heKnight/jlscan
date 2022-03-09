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

if __name__ == '__main__':
    url = 'go.com'
    print(parse_url(url))