//Index.js: Program entry for "index.html"
"use strict";

define(["jquery"], function($)
{   //Fetch configuration from server
    $.get("/bknd/config", function(conf)
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
