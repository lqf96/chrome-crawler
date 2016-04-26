#! /usr/bin/env python2.7

# Python system libraries
from setuptools import setup

# Package information
setup(
    name="ChromeCrawlerBackend",
    version="0.0.1",
    description="Chrome web page crawler backend.",
    author="Qifan Lu",
    author_email="lqf.1996121@gmail.com",
    py_modules = ["chrome_crawler"],
    license="BSD",
    install_requires=[
        "gevent",
        "bottle"
    ],
    include_package_data=True,
    data_files=[
        ("lib/chrome-crawler", ["frontend"])
    ]
)
