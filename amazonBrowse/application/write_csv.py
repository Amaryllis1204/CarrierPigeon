import urllib.request, urllib.response
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime
import pandas as pd
import re

def ama(keyword):
    uri = "https://www.amazon.co.jp/s?k=amazon限定"
    url = uri + '+' + keyword + "&__mk_ja_JP=カタカナ&ref=nb_sb_noss_2"
    text = ''
    #ヘッドレスモードでブラウザを起動
    options = Options()
    options.add_argument('--headless')
    
    #ブラウザを起動
    driver = webdriver.Chrome('/usr/bin/chromedriver')
    driver.get(url)
    driver.implicitly_wait(10)
    text = driver.page_source
    
    #ブラウザの停止
    driver.quit()
    
    soup = BeautifulSoup(text, 'html.parser')
    time.sleep(2)
    
    return soup

def get_info(ele):
    lst = []
    lst2 = []
    lst3 = []
    lst4 = []
    
    goods = ele.find_all('div', class_ = 's-expand-height s-include-content-margin s-latency-cf-section s-border-bottom s-border-top')

    for i in goods:
        try:
            title = i.find('span', class_ = 'a-size-base-plus a-color-base a-text-normal').getText()
            price = i.find('span', class_ = 'a-price-whole').getText()
            image = i.find('img', class_ = 's-image').get('src')
            link = i.find('a', class_ = 'a-link-normal a-text-normal').get('href')
            lst.append(title)
            lst2.append(price)
            lst3.append(image)
            lst4.append('https://www.amazon.co.jp/' + link)
        except AttributeError:
            title = ''
            price = ''
            image = ''
            link = ''
        
    df = pd.DataFrame({'title':lst,
                     'price':lst2,
                     'image':lst3,
                      'link':lst4})
    
    return df

def write_csv(df):
    df.to_csv('test.csv')