import requests
import time
import pandas as pd
import re
from bs4 import BeautifulSoup as bs

start = 1
keyword = input('키워드 입력: \n')
now1 = time.strftime('%Y.%m.%d', time.localtime(time.time()))
now2 = time.strftime('%Y%m%d', time.localtime(time.time()))
for_url = int(time.strftime('%Y', time.localtime(time.time()))) - 2
for_url_now1 = str(for_url)+'.' + time.strftime('%m.%d', time.localtime(time.time()))
for_url_now2 = str(for_url)+time.strftime('%m%d', time.localtime(time.time()))

url = 'https://search.naver.com/search.naver?where=news&sm=tab_pge&query={0}&sort=0&photo=0&field=0&pd=3&ds={1}&de={2}&cluster_rank=74&mynews=0&office_type=0&' \
      'office_section_code=0&news_office_checked=&nso=so:r,p:from{3}to{4},a:all&start={5}'.format(keyword, for_url_now1, now1, for_url_now2, now2, start)
response = requests.get(url)
soup = bs(response.text, 'lxml')
news_title = [title['title'] for title in soup.find_all('a', attrs={'class': 'news_tit'})]
dates = [date.get_text() for date in soup.find_all('span', attrs={'class': 'info'})]
news_date = []

for date in dates:
    if re.search(r'\d+.\d+.\d+.', date) != None:
        news_date.append(date)

print(news_date, news_title)