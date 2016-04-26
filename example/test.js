//Test.js: Chrome crawler example project
"use strict";

require(["crawler"], function(crawler)
{   //Create a new crawler
    var c = new crawler();

    //Prompt any message from server to user
    c.on("data", function(text)
    {   alert(text);
    });

    //Crawl Baidu index page
    c.crawl("https://www.baidu.com", function(c)
    {   //Save all hot news titles
        var hot_news_title = [];
        $(".title-content").each(function(i, elem)
        {   hot_news_title.push($(elem).text());
        });
        //Send titles to server
        c.emit("data", hot_news_title);
    });
});
