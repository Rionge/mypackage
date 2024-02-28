from setuptools import setup, find_packages

setup(
    name = 'mypackage',
    version = '0.1',
    packages = find_packages(exclude = ['test*s']),
    license = 'MIT',
    description = 'EDSA example python project',
    long_description =open('README.md').read(), 
    installrequires = ['numpy'],
    url = '.com',
    author = 'Kariuki Rionge',
    author_email = 'kariukiwangangarionge@gmail.com'

)