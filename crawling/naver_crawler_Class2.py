from ast import keyword
import tkinter.ttk as ttk
from tkinter import*
from datetime import *
import datetime
import time
import tkinter.messagebox as msgbox
from tokenize import String
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver

class NaverMainCrawler:
    select_id = 0
    hds_count = 0
    titles=[]
    search_keyword = input("검색 키워드를 입력하세요.\n")
    search_date = input("날짜를 입력하세요. 예)2022.04.05\n")

    def set_url(self): #네이버의 각 테마별 메인 뉴스를 가져옴
        url = "https://search.naver.com/search.naver?where=news&query={0}&sm=tab_opt&sort=0&photo=0&field=0&pd=3&ds={1}&de=2022.04.29&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Ar%2Cp%3Afrom20220428to20220429&is_sug_officeid=0".format(self.search_keyword, self.search_date)
        return url

    def get_main_title(self):
        url = self.set_url()
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        hds = soup.find_all("a", class_="news_tit")
        self.titles.clear()
        self.hds_count = 0

        for hd in hds:
            title = hd.text
            self.titles.insert(0, title)
            # print("기사 제목: ", title)
            self.hds_count += 1

        self.titles.reverse()
        return self.titles
    


crawler = NaverMainCrawler()
titles = crawler.get_main_title()

for title in titles:
    print(title)