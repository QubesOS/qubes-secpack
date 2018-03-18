#!/bin/bash


export PS4="\n$ "
set -x

date -R -u

feedstail -1 -n5 -f {title} -u https://www.spiegel.de/international/index.rss

feedstail -1 -n5 -f {title} -u https://rss.nytimes.com/services/xml/rss/nyt/World.xml

feedstail -1 -n5 -f {title} -u https://feeds.bbci.co.uk/news/world/rss.xml

feedstail -1 -n5 -f {title} -u http://feeds.reuters.com/reuters/worldnews

curl -s https://blockchain.info/blocks/?format=json | python3 -c "import sys, json; print(json.load(sys.stdin)['blocks'][10]['hash'])"

python3 nist_beacon.py
