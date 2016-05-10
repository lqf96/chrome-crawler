# Chrome Crawler
Proof-of-concept web page content crawler that runs in Google Chrome.

## Get Started
* Download latest [Python distribution](https://github.com/lqf96/chrome-crawler/raw/master/dist/ChromeCrawler-0.0.3.tar.gz) and install it with `pip`. It is highly recommended to install it in a virtual environment.
<pre><code>
$ wget https://github.com/lqf96/chrome-crawler/raw/master/dist/ChromeCrawler-0.0.3.tar.gz
$ virtualenv testenv
$ . testenv/bin/activate
(testenv) $ pip install ChromeCrawler-0.0.3.tar.gz
</code></pre>
* Copy the example folder in this repository and run test.py. Then open Chrome with proper flags to allow unconditional cross origin access.  
Then browse http://127.0.0.1:8080 and you should see example crawling script running.

## API
The backend APIs documentation can be found [here](backend/README.md).  
The frontend APIs documentation can be found [here](frontend/README.md).

## Known Problems
* Sending message from server to client sometimes doesn't work. (Something wrong with SSE?)
* Currently console doesn't ignore errors and logs generated within the iframe, which makes output messy and confused.  
A workaround is to print crawling output directly on the webpage.

## License
The whold project is licensed under 3-clause BSD license.
