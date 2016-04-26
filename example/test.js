require(["crawler"], function(crawler)
{   var c = new crawler();

    c.on("data", function(text)
    {   alert(text);
    });

    c.crawl("https://www.baidu.com", function(c)
    {   var hot_news_title = [];
        $(".title-content").each(function(i, elem)
        {   hot_news_title.push($(elem).text());
        });
        c.emit("data", hot_news_title);
    });
});
