# -*- coding: utf-8 -*-

from setuptools import setup


version = '1.0.1'


setup(
    name='pywe-response',
    version=version,
    keywords='Wechat Weixin Response',
    description='Wechat Server Response Module for Python.',
    long_description=open('README.rst').read(),

    url='https://github.com/sdkwe/pywe-response',

    author='Hackathon',
    author_email='kimi.huang@brightcells.com',

    packages=['pywe_response'],
    py_modules=[],
    install_requires=[],

    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
