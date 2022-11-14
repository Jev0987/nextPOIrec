from urllib import error

import requests
from urllib.request import urlopen
from lxml import etree
import pandas as pd
from bs4 import BeautifulSoup as bf
url = "https://developer.foursquare.com/docs/legacy-venue-categories"

header = {'User-Agent': 'Mozilla/5.0'}

# res = requests.get(url, headers=header)
#
# etree_html = etree.HTML(res.text)
#
# categories = etree_html.xpath('//*[@id="content-container"]/section[1]/div[1]/div/div/table')
#
# for i in categories:
#     print(i.tr)
#
# res.close()
try:
    res = requests.get(url, headers=header)
    etree_html = etree.HTML(res.text)
    categories = etree_html.xpath('//*[@id="content-container"]/section[1]/div[1]/div/div/table/tbody/tr/td')
    for i in categories:
        print(i)
    res.close()
except error.HTTPError as e:
    print(e.code)
except error.URLError as e:
    print(e.reason)