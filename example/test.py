#! /usr/bin/env python2.7

# Python language features
from __future__ import print_function, unicode_literals
# Python system libraries
from os.path import dirname, abspath
# Chrome crawler
from chrome_crawler import ChromeCrawler

if __name__=="__main__":
    # Create a Chrome crawler backend
    srv = ChromeCrawler(
        custom_root=dirname(abspath(__file__)),
        entry="test"
    )
    # Handle data event
    @srv.on("data")
    def data_handler(data):
        # Print Baidu hot news
        print()
        for title in data:
            print(title)
        print()
        # Send message to client
        srv.emit("data", "Server received %d titles!" % len(data))
    # Run backend server
    srv.run()
