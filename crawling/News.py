import time
import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys

def select_date_naver_news(year, month, day):
    '''네이버뉴스에서 원하는 날짜의 뉴스를 검색해서 네이버뉴스 링크를 리스트로 return.'''

    # 연(year) 클릭하기
    elem_year = driver.find_element_by_xpath(
        f'//*[@id="snb"]/div[2]/ul/li[2]/div/div[3]/div[2]/div[1]/div/div/div/ul/li[{year - 1989}]')
    elem_year.click()

    # 월(month) 클릭하기
    elem_month = driver.find_element_by_xpath(
        f'//*[@id="snb"]/div[2]/ul/li[2]/div/div[3]/div[2]/div[2]/div/div/div/ul/li[{month}]')
    elem_month.click()

    # # 날짜(day) 클릭하기
    elem_day = driver.find_element_by_xpath(
        f'//*[@id="snb"]/div[2]/ul/li[2]/div/div[3]/div[2]/div[3]/div/div/div/ul/li[{day}]')
    elem_day.click()

    # 끝나는 날짜 클릭하기
    driver.find_element_by_xpath('//*[@id="snb"]/div[2]/ul/li[2]/div/div[3]/div[1]/span[3]/a').click()

    # 연(year) 클릭하기
    elem_year = driver.find_element_by_xpath(
        f'//*[@id="snb"]/div[2]/ul/li[2]/div/div[3]/div[2]/div[1]/div/div/div/ul/li[{year - 1989}]')
    elem_year.click()

    # 월(month) 클릭하기
    elem_month = driver.find_element_by_xpath(
        f'//*[@id="snb"]/div[2]/ul/li[2]/div/div[3]/div[2]/div[2]/div/div/div/ul/li[{month}]')
    elem_month.click()

    # # 날짜(day) 클릭하기
    elem_day = driver.find_element_by_xpath(
        f'//*[@id="snb"]/div[2]/ul/li[2]/div/div[3]/div[2]/div[3]/div/div/div/ul/li[{day}]')
    elem_day.click()

    # 적용 클릭
    driver.find_element_by_xpath('//*[@id="snb"]/div[2]/ul/li[2]/div/div[3]/div[3]/button').click()

    naver_news_link = driver.find_elements_by_link_text('네이버뉴스')
    links = [link.get_attribute('href') for link in naver_news_link]

    # 옵션 초기화 버튼 클릭
    driver.find_element_by_xpath('//*[@id="snb"]/div[2]/ul/li[6]/div/div/a[1]').click()

    time.sleep(2)

    # 직접입력 클릭.
    elem_input = driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div/div[1]/div[1]/div[2]/ul/li[2]/div/div[1]/a[9]')
    elem_input.send_keys(Keys.ENTER)

    return links

keyword = input('키워드 입력: ')
driver = webdriver.Chrome('C:\\Users\\fpdlq\\Desktop\\Sol\\4-1\\rltrader-master\\chromedriver_win32\\chromedriver.exe')

#입력한 키워드로 검색
driver.get('https://search.naver.com/search.naver?query='+keyword+'&where=news&ie=utf8&sm=nws_hty')

# 옵션 클릭.
elem_option = driver.find_element_by_xpath('//*[@id="snb"]/div[1]/div/div[2]/a')
elem_option.send_keys('\n')
elem_option.send_keys(Keys.ENTER)

# # 직접입력 클릭.
elem_input = driver.find_element_by_xpath('//*[@id="snb"]/div[2]/ul/li[2]/div/div[1]/a[9]')
elem_input.send_keys('\n')

naver_news_link = []

# 2020년 1월부터 ~ 2021 11월 현재까지 2년치 네이버 뉴스데이터 기사 크롤링
for year in tqdm(range(2020,2022),desc='preprocessing year'): #2022
    for month in tqdm(range(1,13),desc='preprocessing month'): #13
        for day in tqdm(range(1,32),desc='preprocessing day'):
            try:
                res = select_date_naver_news(year=year,month=month,day=day)
                naver_news_link.append(res)
            except:
                pass

#  가상 크롬 드라이버를 불러옴
driver = webdriver.Chrome("C:\\Users\\fpdlq\\Desktop\\Sol\\4-1\\rltrader-master\\chromedriver_win32\\chromedriver.exe")

result_df = pd.DataFrame()
naver_news_title = []
naver_news_content = []

for n in tqdm(range(len(naver_news_link)), desc='preprocessing'):
    news_page_title = []
    news_page_content = []

    for idx in range(len(naver_news_link[n])):

        ######## 긁어온 URL로 접속하기 ########
        try:
            driver.get(naver_news_link[n][idx])
        except:
            print("Time Out!")
            continue

        ######## 접속한 URL에서 page_source받아오기 ########
        try:
            response = driver.page_source
        except UnexpectedAlertPresentException:
            driver.switch_to_alert().alert()
            print("게시글이 삭제된 경우입니다.")
            continue
        soup = BeautifulSoup(response, 'html.parser')

        ##### 뉴스 타이틀 긁어오기 #####
        title = None
        try:
            item = soup.find('div', class_='article_info')
            title = item.find('h3', class_='tts_head').get_text()
        except:
            title = "OUT_LINK"

        news_page_title.append(title)

        ###### 뉴스 본문 긁어오기 #####
        # doc = None
        # text = ''
        #
        # data = soup.find_all("div", {"class": "_article_body_contents"})
        # if data:
        #     for item in data:
        #         if item.find('script', type='text/javascript'):
        #             item.find('script', type='text/javascript').decompose()
        #         elif item.find('span', 'end_photo_org'):
        #             item.find('span', 'end_photo_org').decompose()
        #         text = item.get_text()
        #         doc = ''.join(text)
        # else:
        #     doc = "OUT_LINK"
        #
        # news_page_content.append(doc.replace('\n', ' '))

    naver_news_title.append(news_page_title)
    #naver_news_content.append(news_page_content)

    time.sleep(2)

df = pd.DataFrame({'기사제목': naver_news_title})
result_df = pd.concat([result_df, df], ignore_index=True)
result_df.to_csv('News.csv', encoding='cp949')