//Crawler.js: Proof-of-concept Chrome-based crawler implementation
"use strict";

//Crawler class
define(["jquery"], function($)
{   //Crawler class
    function crawler(options)
    {   //Not initialized with new
        if (this.constructor!=crawler)
        {   var instance = Object.create(crawler.prototype);
            crawler.apply(instance, arguments);
            return instance;
        }
        //Current crawler instance
        var self = this;

        //Options
        options = options||{};
        //Page containers / Frames
        this.__frames = [];
        //Maximum page count for a single frame
        this.max_count = options.max_count||500;
        //Event handlers
        this.__handlers = {};

        //Event source
        var event_src = new EventSource("/bknd/poll");
        //Add event listener
        event_src.addEventListener("message", function(e)
        {   var data_obj = JSON.parse(decodeURIComponent(atob(e.data)));
            //Call event handlers
            if (data_obj.event in self.__handlers)
            {   var handlers = self.__handlers[data_obj.event];
                for (var i=0;i<handlers.length;i++)
                    handlers[i](data_obj.data);
            }
        });
    };

    //Crawl given page
    crawler.prototype.crawl = function(url, callback)
    {   //Current crawler instance
        var self = this;

        //Find a spare iframe
        var spare_frame = null;
        for (var i=0;i<this.__frames.length;i++)
            if (this.__frames[i].available)
            {   spare_frame = this.__frames[i];
                break;
            }
        //No spare iframe, create a new one
        if (spare_frame==null)
        {   //Create new iframe and attach to page
            var new_iframe = $("<iframe />")
                .attr("src", "about:blank")
                .css("display", "none");
            $("body").append(new_iframe);
            //Generate new frame
            spare_frame = {
                "cb": null,
                "count": 0,
                "iframe": new_iframe,
                "available": true,
                "deferred": $.Deferred()
            };

            //Add event listener
            new_iframe.load(function()
            {   //Call callback
                if (($(this).attr("src")!="about:blank")&&(spare_frame.cb))
                {   var _cb = this.contentWindow.eval("("+spare_frame.cb.toString()+")");
                    _cb(self);
                }

                //Unlock the frame
                spare_frame.available = true;
                //Update page count
                spare_frame.count++;

                //Replace old deferred object with new one
                var old_deferred = spare_frame.deferred;
                spare_frame.deferred = $.Deferred();

                //Destroy frame when count exceeded maximum page count
                //(To avoid sudden crash of the browser)
                if (spare_frame.count>=this.max_count)
                {   $(this).remove();
                    self.__frames.splice(self.__frames.indexOf(spare_frame), 1);
                }

                //Resolve old promise
                old_deferred.resolve();
            });

            //Add frame to frame collection
            this.__frames.push(spare_frame);
        }

        //Lock the frame
        spare_frame.available = false;
        //Set callback and URL
        spare_frame.cb = callback;
        spare_frame.iframe.attr("src", url);
        //Return current promise
        return spare_frame.deferred.promise();
    };

    //Handle messages from server
    crawler.prototype.on = function(event, handler)
    {   if (!(event in this.__handlers))
            this.__handlers[event] = [];
        //Add handler to handler collections
        this.__handlers[event].push(handler);
    };

    //Send message to server
    crawler.prototype.emit = function(event, data)
    {   var data_encoded = btoa(encodeURIComponent(JSON.stringify({"event": event, "data": data})));
        return $.post("/bknd/msg", {"data": data_encoded});
    };

    //Inject script into page
    crawler.inject = crawler.prototype.inject = function(w, url)
    {   //Create deferred object
        var d = $.Deferred();
        //Create script element
        var script_element = w.document.createElement("script");
        script_element.setAttribute("src", url);
        script_element.addEventListener("load", d.resolve);
        //Append script element to document body
        w.document.body.appendChild(script_element);
        return d.promise();
    };

    return crawler;
});
