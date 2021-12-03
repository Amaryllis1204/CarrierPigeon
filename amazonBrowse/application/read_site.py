import urllib.request, urllib.response
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime
import sqlite3
from django.shortcuts import redirect

def amazon_only(keyword):
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
    
    return soup

def amazon_domain_only(keyword):
    uri = "https://www.amazon.co.jp/s?k=Amazon.co.jp限定"
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

def amazon_only_brand(keyword):
    uri = "https://www.amazon.co.jp/s?k=Amazon限定ブランド"
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

def get_info(ele, dbname):
    lst = []
    tpl = ()
    goods = ele.find_all('div', class_ = 's-expand-height s-include-content-margin s-latency-cf-section s-border-bottom s-border-top')
    db = sqlite3.connect("db.sqlite3")
    c = db.cursor()
    insert_sql = 'insert into ' + dbname +' (title, price, image, link, pub_date) values (?,?,?,?,?)'
    delete_sql = 'delete from ' + dbname
    for i in goods:
        try:
            title = i.find('span', class_ = 'a-size-base-plus a-color-base a-text-normal').getText()
            price = i.find('span', class_ = 'a-price-whole').getText()
            image = i.find('img', class_ = 's-image').get('src')
            link = i.find('a', class_ = 'a-link-normal a-text-normal').get('href')
            link = 'https://www.amazon.co.jp/' + link
            pub_date = datetime.datetime.now()
            lst.append((title, price, image, link, pub_date))

            # lst.append((title, price, image, link))
        except AttributeError:
            title = ''
            price = ''
            image = ''
            link = ''
            pub_date = ''
    c.execute(delete_sql)
    c.executemany(insert_sql, lst)
    db.commit()
    db.close()