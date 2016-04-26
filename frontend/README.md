# Chrome Crawler Frontend Documentation

## Note
* The entry point defined in server side will be used as the execution entry point of custom scripts. For example, if the entry point is `index`, then script `/custom/index.js` will be executed when index page is opened.
* You should define all your scripts as AMD modules. `Require.js` is recommended.
* `jquery`, `co` and `crawler` module are currently provided and can be imported with `require` or `define` function.

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
