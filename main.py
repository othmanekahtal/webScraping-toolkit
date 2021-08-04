from bs4 import BeautifulSoup
from Helpers.rsw import open_html, save_html
from Helpers.fetcher import fetch
from Helpers.get_agreeance import get_agreeance
from time import sleep
from tqdm import tqdm_notebook
import json

urls = [
    'https://www.allsides.com/media-bias/media-bias-ratings',
    # 'https://www.allsides.com/media-bias/media-bias-ratings?page=1',
    # 'https://www.allsides.com/media-bias/media-bias-ratings?page=2'
]
data = []
for i, url in enumerate(urls):
    # print(i,url)
    r = fetch(url)
    # # parsing data :
    soup = BeautifulSoup(r['content'], 'html.parser')
    # print(soup.prettify())
    #
    # # So to get each row, we just select all <tr> inside <tbody>:

    rows = soup.select('tbody tr')
    for row in rows:
        d = dict()
        d['name'] = row.select_one('.source-title').text.strip()
        d['allsides_page'] = 'https://www.allsides.com' + row.select_one('.source-title a')['href']
        d['bias'] = row.select_one('.views-field-field-bias-image a')['href'].split('/')[-1]
        d['agree'] = int(row.select_one('.agree').text)
        d['disagree'] = int(row.select_one('.disagree').text)
        d['agree_ratio'] = d['agree'] / d['disagree']
        d['agreeance_text'] = get_agreeance(d['agree_ratio'])
    #     #getting link of the web site
        link = fetch(d['allsides_page'])
        soup = BeautifulSoup(link['content'], 'html.parser')
        # print('fetching link page',soup)
        try:
            website = soup.select_one('body > div.full-news-source > div > div > div.span4 > div > a')['href']
            print(website)
            d['website'] = website
        except TypeError:
            pass
        sleep(10)
        print(d)
        data.append(d)
    with open('content/allsides' + str(i) + '.json', 'w') as f:
        json.dump(data, f)
