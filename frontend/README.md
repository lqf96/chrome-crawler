# Chrome Crawler Frontend Documentation

## Note
* You should define all your crawling scripts as AMD modules. You can use `require.js` to do that, which is provided by default in the framework.
* The base URL for `require.js` is `/custom`.
* To use extra 3rd party JS AMD modules, call `require.config` to update module path mapping. Alternatively you can define the mapping at server side.
* We recommend you to put custom HTML content in element `#custom-area`.

## API
* Class `crawler`:
  - `crawler([options])`: Constructor of the crawler class.
    + `options`: Options for creating a crawler instance. May include:
      * `max_count`: Maximum amount of pages a single `<iframe />` element can display. (To avoid sudden crash problem of Chrome browser.)
  - `crawler#crawl(url, cb)`: Open up a web page by URL and execute function `cb` in the web page environment.
    + `url`: The URL of the web page.
    + `cb`: Callback function taking the crawler instance as the only parameter. Note that the callback function will be executed in the web page environment so you can't capture external variables in the callback functions. You should instead put all shared variables in the crawler instance.
    + The function returns a promise that will be resolved after callback function is executed.
  - `crawler#on(event, cb)`: Add a callback for a specific event from server.
    + `event`: Event name.
    + `cb`: Callback function taking received data as the only parameter.
  - `crawler#emit(event, data)`: Send a message with given event type to server.
    + `event`: Event name.
    + `data`: Data to be sent to server. Any object capable of converting to JSON format is allowed.
  - `crawler#inject(w, url)`: Inject script into given window.
    + `w`: Window object of document to inject script into.
    + `url`: URL of the script.
    + The function returns a promise that will be resolved after the script is loaded.
