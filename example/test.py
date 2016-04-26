#! /usr/bin/env python2.7
from __future__ import print_function
from os.path import dirname, abspath
from chrome_crawler import ChromeCrawler

if __name__=="__main__":
    srv = ChromeCrawler(
        custom_root=dirname(abspath(__file__)),
        entry="test"
    )
    @srv.on("data")
    def data_handler(data):
        print(data)
        srv.emit("data", "woo!")
    srv.run()
