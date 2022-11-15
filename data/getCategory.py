from urllib import error
import requests
from urllib.request import urlopen
from lxml import etree
import pandas as pd


def find_category():
    category = list()
    category_id = list()

    url = "https://developer.foursquare.com/docs/legacy-venue-categories"
    header = {'User-Agent': 'Mozilla/5.0'}
    try:
        res = requests.get(url, headers=header)
        etree_html = etree.HTML(res.text)
        trs = etree_html.xpath('//*[@id="content-container"]/section[1]/div[1]/div/div/table/tbody/tr')
        for tr in trs:
            cate_id = tr[0].text
            category_path = tr[1].text
            category_id.append(cate_id)
            category.append(category_path)
        res.close()
    except error.HTTPError as e:
        print(e.code)
    except error.URLError as e:
        print(e.reason)

    df_category = pd.concat(
        [pd.DataFrame(category_id, columns=['CategoryId']), pd.DataFrame(category, columns=['CategoryPath'])],
        axis=1)
    df_category.to_csv("categories.csv", index=False)


df = pd.read_csv("categories.csv")
df = df.dropna()
category_dict = dict()
L2_categories = dict()
for c in df['CategoryPath']:
    c = str(c).split(' > ')
    category_dict[c[0]] = []
    if len(c) == 3:
        L2_categories[c[1]] = []

for c in df['CategoryPath']:
    c = str(c).split(' > ')
    if len(c) == 2:
        category_dict[c[0]].append(c[1])
    if len(c) == 3:
        L2_categories[c[1]].append(c[2])

print(category_dict)
print(L2_categories)





