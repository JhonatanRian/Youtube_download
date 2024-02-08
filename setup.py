from setuptools import setup

class CONFIG:
    VERSION = 'v1.0.1'
    platform = 'darwin-x86_64'
    executable_stub = '/Library/Frameworks/Python.framework/Versions/3.11/lib/libpython3.11.dylib' # htis is important, check where is your Python framework and get the `dylib`
    APP_NAME = f'pytube_{VERSION}_{platform}'
    APP = ['downloader.py']
    DATA_FILES = [
        ('utils', ['utils/get_path_donwload.py']),
        ('utils', ['utils/helpers.py']),
        ('utils', ['utils/helpers.py']),
        ('img/1x', ['img/1x/youtube_logo_white.png']),
    ]

    OPTIONS = {
        'argv_emulation': False,
        'iconfile': 'app.ico',
        'plist': {
            'CFBundleName': APP_NAME,
            'CFBundleDisplayName': APP_NAME,
            'CFBundleGetInfoString': APP_NAME,
             'CFBundleVersion': VERSION,
            'CFBundleShortVersionString': VERSION,
            'PyRuntimeLocations': [
                executable_stub
           ]
        }
    }

def main():
    setup(
        name=CONFIG.APP_NAME,
        app=CONFIG.APP,
        data_files=CONFIG.DATA_FILES,
        options={'py2app': CONFIG.OPTIONS},
        setup_requires=['py2app'],
        maintainer='Jhonatan',
        author_email='jhonatanrian0543@outlook.com',
    )

if __name__ == '__main__':
    main()