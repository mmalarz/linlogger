from setuptools import setup, find_packages

setup(
    name='linlogger',
    version='0.1',
    description='Keylogger for linux systems',
    url='https://github.com/mmalarz/linlogger',
    license='LICENSE',
    packages=[
        'linlogger',
        'linlogger.files',
    ],
    install_requires=find_packages(),
    zip_safe=False
)
