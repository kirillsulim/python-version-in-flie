import pkg_resources


def run():
    version = pkg_resources.resource_string('app', '../app.version').decode('utf-8').strip()
    print('Me version is: {}'.format(version))
    return 0


if __name__ == '__main__':
    exit(run())
