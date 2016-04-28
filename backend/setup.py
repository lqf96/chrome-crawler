#! /usr/bin/env python2.7

# Python system libraries
from setuptools import setup

# Distribution information
setup(
    name="ChromeCrawler",
    version="0.0.2",
    description="Chrome web page crawler backend.",
    author="Qifan Lu",
    author_email="lqf.1996121@gmail.com",
    packages=["frontend"],
    py_modules = ["chrome_crawler"],
    license="BSD",
    url="https://github.com/lqf96/chrome-crawler",
    install_requires=[
        "gevent",
        "bottle"
    ],
    include_package_data=True
)
