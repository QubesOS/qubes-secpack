#!/usr/bin/python3
# Made by InnovativeInventor, MIT license applies

from xml.etree.ElementTree import fromstring, ElementTree
import requests

# There are some DOS vulnerabilities listed here:
# https://docs.python.org/3/library/xml.html#xml-vulnerabilities

nist_beacon = requests.get('https://beacon.nist.gov/rest/record/last.xml')
tree = ElementTree(fromstring(nist_beacon.content))
root = tree.getroot()

print("Unix time: " + root[2].text)
print("Seed: " + root[3].text)
print("Output: " + root[6].text)
