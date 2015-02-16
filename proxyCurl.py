def get_file(host, url, filename=None, location='.'):
    """Downloads a file on remote server."""
    url_effective = '%{url_effective}'
    url = subprocess.Popen('curl -sL -w "{0}" "{1}" -o /dev/null'.format(url_effective, url),stdout=subprocess.PIPE,shell=True)
    (out,err) = url.communicate()
    url = out
    print('[{0}] Downloading {1}'.format(host, url))
    if filename is None:
        filename = url.split('/')[-1]
    run(host, path=location, cmd='curl -o {0} {1}'.format(filename, url))
    return filename