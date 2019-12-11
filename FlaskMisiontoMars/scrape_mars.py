# Dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import requests
import pandas as pd

def scrape(info,url):
    dg = []
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    if info == "News":
        news = soup.find_all('ul', class_='item_list')
        for new in news:
            dic = {}
            dic['title'] = new.find('div', class_='content_title').text
            dic['p'] = new.find('a').text
            dg.append(dic)
    elif info == "Images":
        featured_mars_image = soup.find_all('div', class_='img')
        for i in range(len(featured_mars_image)):
            dic = {}
            dic['img'] = featured_mars_image[i].img["src"]
            dg.append(dic)
    elif info == 'Weather':
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        dic = {}
        dic['wea']= soup.find('p', class_ = "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text.strip()
        dg.append(dic)
    elif info == 'Facts':
        mars_tables = pd.read_html(url)
        mars_tables_df = mars_tables[0]
        mars_tables_df.columns = ['Description', 'Value']
        dg = mars_tables_df
    elif info == 'Hemis':
        hemisphere_list=['Cerberus','Schiaparelli','Syrtis','Valles']
        for hemi in hemisphere_list:
            dic = {}
            browser.visit(url)
            browser.click_link_by_partial_text(hemi)
            html = browser.html
            soup = BeautifulSoup(html,'html.parser')
            dic['image'] = soup.find('a',target="_blank")['href']
            dic['title'] = soup.find('h2',class_="title").text
            dg.append(dic)
    browser.quit()
    return dg




    



