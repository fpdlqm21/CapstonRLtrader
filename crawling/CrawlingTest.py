#html문서를 가져올 때 사용하는 패키지(정적수집)
import requests

#chromedriver를 이용해 chrome을 제어하기 위해 사용하는 패키지(입력하거나 특정 버튼을 눌러야하는 경우), 동적수집
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #셀레니엄으로 입력하기 위한 import
import time #페이지 로딩을 기다리는데 사용할 time 모듈

#Beautifulsoup4
from bs4 import BeautifulSoup as bs #html문서를 잘 정리되고 쉬운 형태로 만들어 원하는 것만 가져올 때 사용

#requests 연습 코드
# url = 'https://www.naver.com'
# response = requests.get(url) #get함수를 이용해 해당 url로 부터 html이 담긴 자료를 받아옴
# print(response.status_code) #정상적으로 받아졌다면 200이라는 코드 반환
# html_text = response.text #우리가 얻고자하는 html문서가 이 변수에 저장

#selenium 연습 코드
driver = webdriver.Chrome('C:\\Users\\fpdlq\\Desktop\\Sol\\4-1\\rltrader-master\\chromedriver_win32\\chromedriver.exe')
#driver.get('https://www.naver.com/')
driver.get('https://google.co.kr/')
time.sleep(3) #페이지가 로딩되도록 3초 기다림, driver.implicitly_wait(time_to_wait=5) -> 5초동안 로드될 때까지 기다림, 이후에 계속 설정할 필요x
#search = driver.find_element_by_name('query') #검색어 창을 찾아 search 변수에 저장(네이버는 query, 구글은 q)
search = driver.find_element_by_tag_name('input')
search.send_keys('한성대')
time.sleep(1)
search.send_keys(Keys.ENTER) #search 변수에 저장된 곳에 엔터를 입력

#BeautifulSoup 연습 코드
# reponse = requests.get('https://www.google.co.kr')
# soup = bs(reponse.text, 'html.parser') #html을 잘 정리된 형태로 변환
# print(soup.p) #p태그와 내용 찾아서 출력, soup.p.string -> p태그는 빼고 내용만 출력
# print(soup.find_all('h2')) #h2태그들만 찾아서 모두 가져옴


