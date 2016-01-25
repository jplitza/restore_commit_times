from os import path
from distutils.core import setup


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='restore_commit_times',
    version='0.2',
    description='Restore files mtime from Git commit times',
    long_description=long_description,
    author='Andrew Grigorev',
    author_email='andrew@ei-grad.ru',
    url='https://github.com/ei-grad/restore_commit_times',
    py_modules='restore_commit_times',
    install_requires=['gitpython'],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [
            'restore_commit_times=restore_commit_times:main',
        ],
    },
)
