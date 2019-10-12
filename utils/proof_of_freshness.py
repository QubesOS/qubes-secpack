#!/usr/bin/python3

import sys
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
        "https://feeds.bbci.co.uk/news/world/rss.xml",
        "http://feeds.reuters.com/reuters/worldnews"
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
    print("{:s}".format(blocks["blocks"][0]["hash"]))

if __name__ == "__main__":
    news()
    bitcoin()
