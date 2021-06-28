
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import os

def browser():

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    news_title, news_paragraph = mars_news(browser)

    data={
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "hemispheres": hemispheres(browser),
        "last_modified": dt.datetime.now()
    }

    browser.quit()
    return data


def scrape_mars(browser):
    # browser = init_browser()
    # listings = {}
    
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    html=browser.html
    soup = BeautifulSoup(html, 'html.parser')

    news_title=soup.find_all("div", class_="content_title")[0].text
    news_p=soup.find_all("div", class_="article_teaser_body")[0].text 

    print(news_title)

    print(news_p)
    return news_title, news_p

    # JPL MARS SPACE IMAGES
def mars_image(browswer):

    image_url="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)
    xpath="/html/body/div/div/div/main/div[2]/div[2]/div[2]/div/section/div[1]/div/a/div/div[3]/div/div/div/img"

    results= browser.find_by_xpath(xpath)
    img= results[0]
    img.click()


    image_html=browser.html
    image_soup= BeautifulSoup(html, 'html.parser')
    featured_image_url=image_soup.find("img", {"id":"96342"})
    # featured_image_url=age_url.find("src")
    # featured_image_url
    return featured_image_url

def mars_facts(browser):
    # Mars Facts
    mars_url="https://space-facts.com/mars/"

    tables = pd.read_html(mars_url)
    tables.columns=['Description','Mars']
    tables.set_index('Description', inplace=True)
    return tables.to_html(classes="table table-stripped")

def mars_hemisphere(browser):

    # Mars Hemispheres
    hem_images_list=[]
    Hemisphere_url= "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(Hemisphere_url)
    hem_html = browser.html
    hem_soup = BeautifulSoup(hem_html, 'html.parser')
    hemispheres=hem_soup.find_all('div', class_='item')


    for hemisphere in hemispheres:
        title=hemisphere.find("h3").text
        end_url=hemisphere.find("a")["href"]
        hem_url= "https://astrogeology.usgs.gov/"+ end_url
        browser.visit(hem_url)
        hem_html= browser.html
        hem_soup = BeautifulSoup(hem_html, 'html.parser')
        downloads = hem_soup.find("div", class_="downloads")
        hem_image_url= downloads.find("a")["href"]
        hem_images_list.append({"title":title, "image_url":hem_url})
    
    
    return hem_images_list


    # mars_dict={
    #     "News Title":news_title,
    #     "News Paragraph":news_p,
    #     "Mars Facts": html_table,
    #     "hemisphere images": hem_images_list
    # }
    

    
    # return mars_data

if __name__ == "__main__":

