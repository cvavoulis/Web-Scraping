
# coding: utf-8

# In[36]:


# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
import re
import time
import pandas as pd

def scrape():
        mars={}


# In[38]:



        url = 'https://mars.nasa.gov/news'

        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'lxml')


        # In[39]:


        # print(soup.prettify())


        # In[42]:


        titles=soup.find("div", class_="content_title")
        news_title=titles.a.text.strip()
        news_title
        mars["news_title"]=news_title

        # In[43]:


        paragraphs=soup.find("div", class_="rollover_description_inner")
        news_p=paragraphs.text.strip()
        news_p

        mars["news_p"]=news_p
        # In[7]:


        browser=Browser("chrome", headless=False)
        mars_url="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
        browser.visit(mars_url)
        time.sleep(5)

        # In[8]:


        mars_images_html = browser.html
        mars_soup = BeautifulSoup(mars_images_html, 'html.parser')


        # In[9]:


        mars_url=mars_soup.find_all("div", class_="carousel_items")
        print(mars_url)


        # In[10]:


        

        # text = 'gfgfdAAA1234ZZZuijjk'

        # m = re.search('AAA(.+?)ZZZ', text)
        # if m:
        #     found = m.group(1)

        for x in mars_url:
                article=x.find("article")
                # print(image)
                image=article.get("style")
                print(image)
                url_only=re.search("'(.+?)'", image)
                if url_only:
                        found = url_only.group(1)
                        print(found)
                


        # In[11]:


        featured_image_url="https://www.jpl.nasa.gov"+found 
        print(featured_image_url)
        mars["featured_image_url"]=featured_image_url

        # In[24]:



        url = "https://twitter.com/marswxreport?lang=en"
        browser.visit(url)
        html=browser.html
        # response = requests.get(url)

        soup = BeautifulSoup(html, 'html.parser')


        # In[25]:


        tweets=soup.find_all("div", class_="js-tweet-text-container")
        tweet_list=[]
        for tweet in tweets:
                mars_weather=tweet.p.text
                tweet_list.append(mars_weather)
                # print(tweet_list)
                first_tweet=tweet_list[0]
                print(first_tweet)
                element=first_tweet[0]
                print(element)
       

        # In[30]:


        mars_tweet = [x for x in tweet_list if (x[0]=="S" and x[1]=="o" and x[2]=="l")]
        mars_weather=mars_tweet[0]
        mars_weather

        mars["mars_weather"]=mars_weather
        # In[15]:



        url = "https://space-facts.com/mars/"

        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'lxml')


        # In[16]:


        
        # facts=soup.find("tbody")
        # table_rows=facts.find_all("tr")

        # l = []
        # for tr in table_rows:
        #         td = tr.find_all('td')
        #         row = [tr.text for tr in td]
        #         l.append(row)
        #         mars_table=pd.DataFrame(l, columns=["Category","Statistic"])
        #         mars_table
        # mars_table.set_index("Category", inplace=True)
        
        # # In[17]:


        # mars_html_table=mars_table.to_html()
        # print(mars_html_table)
        # mars["mars_html_table"]=mars_html_table
        # mars["mars_table"]=mars_table

        # day 2 activtiy 9, week 15


        # In[18]:


        # mars_hemisphere=Browser("chrome", headless=False)
        hem_url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        browser.visit(hem_url)


        # In[19]:


        mars_hem_html = browser.html
        hem_soup = BeautifulSoup(mars_hem_html, 'html.parser')


        # In[20]:


        hemisphere_images=hem_soup.find_all("div", class_="description")
        hemisphere_images
        

        # In[21]:


        indiv_url_list=[]
        for x in hemisphere_images:
                info=x.find('a')
                url=info.get("href")
                indiv_url="https://astrogeology.usgs.gov"+url
                indiv_url_list.append(indiv_url)
                print(indiv_url_list)    


        # In[22]:


        hemisphere_images_dict={}
        hemisphere_image_urls=[]
        

        # In[23]:




        for x in indiv_url_list:
                # mars_images=Browser("chrome", headless=False)
                browser.visit(x)
                indiv_html = browser.html
                indiv_soup = BeautifulSoup(indiv_html, 'html.parser')
                image=indiv_soup.find("a", text="Sample")
                image_link=image.get("href")
                title=indiv_soup.find("h2", class_="title").text.replace("Enhanced","")
                hemisphere_images_dict["Title"]=title
                hemisphere_images_dict["Image_Url"]=image_link
                hemisphere_image_urls.append(hemisphere_images_dict)
                print(hemisphere_image_urls)
                
        mars["hemisphere_images_dict"]=hemisphere_images_dict
        mars["hemisphere_image_urls"]=hemisphere_image_urls

        # In[24]:


        # get_ipython().system(' jupyter nbconvert --to script --template basic mission_to_mars.ipynb --output scrape_mars')


        # In[ ]:
        return(mars)



