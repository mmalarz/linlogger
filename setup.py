from setuptools import setup, find_packages

setup(
    name='linlogger',
    version='0.1',
    description='Keylogger for linux systems',
    url='https://github.com/mmalarz/linlogger',
    license='LICENSE',
    packages=find_packages(),
    install_requires=[
        'clipboard >= 0.0.4',
        'pyxhook >= 1.0.0',
    ],
    zip_safe=False
)
