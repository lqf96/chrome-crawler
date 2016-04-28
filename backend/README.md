# Chrome Crawler Backend Documentation

## Note
* To start a crawling project you must define a custom file root for the crawling server, which should be a directory containing all your crawling scripts and data. You should also define an entry point, which is the filename of the AMD module that the framework will immediately load after the index page is opened in the browser.
* You can define extra JS AMD module path mapping so that your crawling script can use extra JS libraries for your crawling task.

## API
You can use `help(ChromeCrawler)` to show all available APIs and their usage.
