import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='
query = input('검색할 키워드를 입력:')
url += '%s'%query
news = []

reponse = requests.get(url) #html받아옴
html_text = reponse.text #html문서를 변수에 저장
html = bs(html_text, 'html.parser') #html을 잘 정리된 형태로 저장
#print(html.select_one('a,news_tit').get_text()) #선택자 개념을 이용해서 뉴스기사 제목을 하나 가져온다
titles = html.select('a.news_tit') #뉴스기사 제목을 모두 가져온다

for i in titles:
    title = i.get_text()
    news.append([title])
    #print(title)

data = pd.DataFrame(news)
data.columns = ['title']
#data.to_csv('Crawling_Test.csv', encoding='cp949')
data.to_csv('Crawling_Test_Ver_UTF-8.csv', encoding='utf-8')
print(data.head())