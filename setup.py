from setuptools import setup, find_packages

setup(
    name='my_package',
    packages=find_packages(where='my_package'),
    version='1.0'
)
