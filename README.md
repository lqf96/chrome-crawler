# Chrome Crawler
Proof-of-concept web page content crawler that runs in Google Chrome.

## Get Started
* Download latest [Python distribution](https://github.com/lqf96/chrome-crawler/raw/master/dist/latest.tar.gz) and install it with `pip`. It is highly recommended to install it in a virtual environment.
```bash
$ wget https://github.com/lqf96/chrome-crawler/raw/master/dist/latest.tar.gz
$ virtualenv testenv
$ . testenv/bin/activate
(testenv) $ pip install latest.tar.gz
```
* Copy the example folder in this repository and run test.py. Then open Chrome with proper flags to allow unconditional cross origin access. (You may use `start-browser` script to open Chrome)  
Then browse http://127.0.0.1:8080 and you should see example crawling script running.

## API
The backend APIs documentation can be found [here](backend/README.md).  
The frontend APIs documentation can be found [here](frontend/README.md).

## Known Problems
* Sending message from server to client sometimes doesn't work. (Something wrong with SSE?)
* Currently console doesn't ignore errors and logs generated within the iframe, which makes output messy and confused.  
A workaround is to print crawling output directly on the webpage.
* Even if cross-origin access is enabled from command line, Chrome still blocks some pages which enables X-Frame-Options protection.  
To allow these pages to be loaded you will need to install some Chrome extensions.

## License
The whold project is licensed under 3-clause BSD license.
