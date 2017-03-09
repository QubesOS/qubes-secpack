#!/bin/sh


export PS4="\n$ "
set -x

date -R -u

feedstail -1 -n5 -f {title} -u https://www.spiegel.de/international/index.rss

feedstail -1 -n5 -f {title} -u http://rss.nytimes.com/services/xml/rss/nyt/World.xml

feedstail -1 -n5 -f {title} -u http://feeds.bbci.co.uk/news/world/rss.xml

feedstail -1 -n5 -f {title} -u http://feeds.reuters.com/reuters/worldnews

curl -s http://blockchain.info/blocks/?format=json | python3 -c "import sys, json; print(json.load(sys.stdin)['blocks'][10]['hash'])"
