#! -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='bert4torch',
    version='0.0.1',
    description='an elegant bert4torch',
    long_description='bert4keras: https://github.com/liwenju0/bert4torch',
    license='Apache License 2.0',
    url='https://github.com/liwenju0/bert4torch',
    author='liwenju0',
    author_email='liwenjudetiankong@126.com',
    install_requires=['torch>=1.10.0'],
    packages=find_packages()
)
