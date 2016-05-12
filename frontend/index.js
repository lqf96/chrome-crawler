//Index.js: Program entry for "index.html"
"use strict";

define(["jquery"], function($)
{   //Fetch server data (configuration) from server
    $.get("/bknd/data", function(conf)
    {   //Extra library address mapping
        if ("amd_mapping" in conf)
            require.config({
                "paths": conf.amd_mapping
            });

        //Custom entry point given
        if (("custom_root" in conf)&&("entry" in conf))
            require([conf["entry"]]);
        //Not given, prompt a warning
        else
            console.warn("Custom root or JS entry point not given.");
    })
})
