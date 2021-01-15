from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import os




executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
browser.visit(url)


# In[4]:


html=browser.html
soup = BeautifulSoup(html, 'html.parser')

news_title=soup.find_all("div", class_="content_title")[0].text
news_p=soup.find_all("div", class_="article_teaser_body")[0].text 

print(news_title)

print(news_p)


# In[5]:


# JPL MARS SPACE IMAGES

image_url="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(image_url)


# In[6]:


# xpath="//*[@id="__layout"]/div/main/div[2]/div[2]/div[2]/div/section/div[1]/div/a/div/div[3]/div/div/div/img"

xpath="/html/body/div/div/div/main/div[2]/div[2]/div[2]/div/section/div[1]/div/a/div/div[3]/div/div/div/img"


# In[7]:


results= browser.find_by_xpath(xpath)
img= results[0]
img.click()


# In[17]:


image_html=browser.html
image_soup= BeautifulSoup(html, 'html.parser')
age_url=image_soup.find("img", {"id":"96342"})
# featured_image_url=age_url.find("src")
# featured_image_url


# In[ ]:


# Mars Facts
mars_url="https://space-facts.com/mars/"

tables = pd.read_html(mars_url)
tables


# In[ ]:


df = tables[0]
df


# In[ ]:


html_table = df.to_html()
html_table
html_table.replace('\n', '')


# In[ ]:


df.to_html('table.html')


# In[18]:


# Mars Hemispheres
hem_images_list=[]
Hemisphere_url= "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(Hemisphere_url)
hem_html = browser.html
hem_soup = BeautifulSoup(hem_html, 'html.parser')


# In[19]:


hemispheres=hem_soup.find_all('div', class_='item')


# In[ ]:


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
    


# In[ ]:


hem_images_list


# In[ ]:




