from os import path
from distutils.core import setup


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='restore_commit_times',
    version='0.1',
    description='Restore files mtime from Git commit times',
    long_description=long_description,
    author='Andrew Grigorev',
    author_email='andrew@ei-grad.ru',
    url='https://github.com/ei-grad',
    py_modules='restore_commit_times',
    entry_points={
        'console_scripts': [
            'restore_commit_times=restore_commit_times:main',
        ],
    },
)
