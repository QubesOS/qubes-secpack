#!/bin/sh


export PS4="\n$ "
set -x

date -R -u

feedstail -1 -n5 -f {title} -u https://www.spiegel.de/international/index.rss

feedstail -1 -n5 -f {title} -u http://rss.nytimes.com/services/xml/rss/nyt/InternationalHome.xml

feedstail -1 -n5 -f {title} -u http://feeds.bbci.co.uk/news/world/rss.xml
