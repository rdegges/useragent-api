# useragent-api

A free, publicly available, user agent API service.


![Cthulu's Head](https://github.com/rdegges/useragent-api/raw/master/assets/cthulu-head.jpg)


## Purpose

I was building this web scraper recently, and needed to make the scraper's
traffic look legitimate.

This is apparently much harder than I initially thought.

Sure, you can spoof your user agent to the latest Firefox release or whatever,
but that only works so well.  To be truly fool-proof with your scraping you
often need to spoof many valid user agents.

This way -- the server can't detect a single bot, and it makes blocking you that
much harder.

So I was looking for a simple way to spoof my user agent to any valid,
relatively modern browser, but couldn't find a way!

This API service does one thing, and only one thing: it gives you a random,
relatively modern web browser user agent that you can use to make web requests,
without worrying about raising suspicion.


## How it Works

I'm basically running a cron task which periodically scrapes *all* known user
agents from here: http://www.useragentstring.com/

This list then gets pruned down to only modern browsers (no weird, obscure
stuff), to avoid suspicion.

This list is then loaded into the application, and randomly served up when you
make API requests, like so: http://api.useragent.io

And...  That's it!

I'll keep this thing maintained over time, and pay for hosting out of my pocket,
so no need to worry about the site or project going down over time.  Feel free
to plug this into whatever projects you have.


## Questions?

Got questions?  Email me: r@rdegges.com
