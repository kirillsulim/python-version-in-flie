from setuptools import setup
from os import path


project_directory = path.abspath(path.dirname(__file__))
data_files = []


def load_from(file_name):
    data_files.append(file_name)
    with open(path.join(project_directory, file_name), encoding='utf-8') as f:
        return f.read()


setup(
    name='demo',
    version=load_from('app.version').strip(),
    url='https://github.com/kirillsulim/python-version-in-flie',
    author='Kirill Sulim',
    author_email='kirillsulim@gmail.com',
    description='A simple general purpose scaffold tool',
    long_description=load_from('README.md'),
    long_description_content_type='text/markdown',
    keywords='scaffold build generator generate',
    packages=[
        'demo',
    ],
    package_data={
        '': [
            'README.md',
        ]
    },
    data_files=[
        ('.', data_files),
    ],
    entry_points={
        'console_scripts': [
            'demo=demo.app:run',
        ],
    },
)


