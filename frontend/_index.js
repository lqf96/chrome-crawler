//Index.js: Program entry for "index.html"
"use strict";

define(["jquery"], function($)
{   //Fetch configuration from server
    $.get("/bknd/config", function(conf)
    {   //Custom entry point given
        if (("custom_root" in conf)&&("entry" in conf))
        {   require(["custom/"+conf["entry"]]);
        }
        //Not given, prompt a warning
        else
            alert("Custom root and JS entry point not given.\n"+
                "No crawling work will be carried out.");
    })
})
