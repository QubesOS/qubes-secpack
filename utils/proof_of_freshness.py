#!/usr/bin/python3

import sys
import datetime
import json
import urllib.request
import feedparser

def news():
    """
    Recent news articles.
    """

    count = 5
    urls = [
        "https://www.spiegel.de/international/index.rss",
        "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
        "https://feeds.bbci.co.uk/news/world/rss.xml"
    ]

    for url in urls:
        feed = feedparser.parse(url)

        if len(feed["items"]) < count:
            sys.exit("couldn't find {:d} items for source {:s}".format(count, url))

        print("Source: {:s} ({:s})".format(feed["feed"]["title"], url))

        for j in range(count):
            print(feed["items"][j]["title"])

        print()

def bitcoin():
    """
    Recent bitcoin block hash.
    """

    depth = 10
    height_url = "https://blockchain.info/q/getblockcount"
    block_url = "https://blockchain.info/block-height/{:d}?format=json"

    print("Source: Blockchain.info")

    height = int(urllib.request.urlopen(height_url).read())

    block_url = block_url.format(height-depth)
    blocks = json.loads(urllib.request.urlopen(block_url).read())
    print(blocks["blocks"][0]["hash"])

def date():
    """
    Print date in RFC 5322 format.
    """

    fmt = "%a, %d %b %Y %T %z"
    print(datetime.datetime.now(datetime.UTC).strftime(fmt))
    print()

if __name__ == "__main__":
    date()
    news()
    bitcoin()
