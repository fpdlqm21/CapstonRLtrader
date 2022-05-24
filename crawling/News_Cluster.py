import requests
import time
import pandas as pd
import re
from bs4 import BeautifulSoup as bs

keyword = input('키워드 입력: \n')
start = 1 #url에서 page넘길 때마다 바뀌는 옵셋
result_df = pd.DataFrame()
now1 = time.strftime('%Y.%m.%d', time.localtime(time.time())) #기간 설정 시 url에 맞는 타입으로 저장
now2 = time.strftime('%Y%m%d', time.localtime(time.time()))
for_url = int(time.strftime('%Y', time.localtime(time.time()))) - 2 #2년전 날짜를 저장위해 정수로 바꾼 후, 저장
for_url_now1 = str(for_url)+'.' + time.strftime('%m.%d', time.localtime(time.time())) #2년전 날짜
for_url_now2 = str(for_url)+time.strftime('%m%d', time.localtime(time.time()))

#url얻어와서 뉴스기사 타이틀만 뽑아오는 메소드
while True:
    try:
        url = 'https://search.naver.com/search.naver?where=news&sm=tab_pge&query={0}&sort=0&photo=0&field=0&pd=3&ds={1}&de={2}&cluster_rank=74&mynews=0&office_type=0&' \
      'office_section_code=0&news_office_checked=&nso=so:r,p:from{3}to{4},a:all&start={5}'.format(keyword, for_url_now1, now1, for_url_now2, now2, start)

        #headers = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'}
        response = requests.get(url)
        soup = bs(response.text, 'lxml')
        news_title = [title['title'] for title in soup.find_all('a', attrs={'class': 'news_tit'})] #뉴스기사 제목 뽑아 저장한 리스트
        #dates = [date.get_text() for date in soup.find_all('span', attrs={'class': 'info'})]
        #news_date = []

        # for date in dates:
        #     if re.search(r'\d+.\d+.\d+.', date) != None:
        #         news_date.append(date)
        df = pd.DataFrame({'기사제목': news_title}) #pandas로 기사제목열을 추가
        result_df = pd.concat([result_df, df], ignore_index=True) #pandas에 뉴스기사제목 내용 추가
        start += 10 #url변경을 위함
        if len(result_df) == 100: #test로 100까지만 저장되게 함 -> 720까지
            result_df.to_csv('CrawlingTest.csv', encoding='cp949') #csv파일로 저장
            print(result_df) #잘 출력되는지 확인위해
            break

    except:
        print(start)
        break

#news_cluster = soup.find('ul', class_ = 'list_cluster').find_all('a', class_= 'elss sub_tit')
# news_cluster = soup.find('a', class_ = 'news_tit').text

#print(news_cluster)