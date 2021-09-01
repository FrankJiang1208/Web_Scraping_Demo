import os
import requests
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape():
    url="https://redplanetscience.com/"
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url)
    html=browser.html
    soup = BeautifulSoup(html, 'html.parser')
    result=soup.find_all('div',class_='col-md-8')
    title=result[0].find("div",class_='content_title').text
    para=result[0].find("div",class_='article_teaser_body').text
    browser.quit()



    url1='https://galaxyfacts-mars.com/'
    tables = pd.read_html(url1)
    df=tables[0]
    html_table = df.to_html(header=False, index=False,border=5)
    html_table=html_table.replace('\n', '')


    urls=['https://marshemispheres.com/cerberus.html','https://marshemispheres.com/schiaparelli.html','https://marshemispheres.com/syrtis.html','https://marshemispheres.com/valles.html']
    hemisphere_image_urls=[]
    for i in range(4):
        browser = Browser('chrome', **executable_path, headless=False)
        browser.visit(urls[i])
        html=browser.html
        soup = BeautifulSoup(html, 'html.parser')
        dict={"title": soup.find('h2',class_='title').text[0:-9], "img_url": 'https://marshemispheres.com/'+soup.find('img',class_='wide-image')['src']}
        hemisphere_image_urls.append(dict)
        browser.quit()




    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit('https://spaceimages-mars.com/')
    html=browser.html
    soup = BeautifulSoup(html, 'html.parser')
    featured_image_url='https://spaceimages-mars.com/'+soup.find('img',class_='headerimage')['src']
    browser.quit()

    return {'news_title':title,'news_p':para,'table':html_table,'hemisphere_image_urls':hemisphere_image_urls,'featured_image_url':featured_image_url}