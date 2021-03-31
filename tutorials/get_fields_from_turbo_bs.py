'''
Created on 27.03.2021

@author: peter
'''
import requests 

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://yandex.ru/turbo?text=https%3A%2F%2Fitsmycity.ru%2F2012-04-09%2Fbiznes-lanch-nedeli-seazone"



#load data 


#get fields:

#header : div class = "cover grid grid_unwrap unit unit_tect"
# header inside: cover__content grid grid_wrap 
# title: 
#h1 class = "turbo-title 
#span itemprop ='name' class = turbo-author__name

#image: span class = "turbo-image turbo-image_type_block turbo-external-ressource unit unit_rect turbo-image_loaded turbo-imate_style_edge"
#  -- inside - imt src = "url"

# then, content in paragraphs 
#each paragraph is separate   
#text = 'paragraph unit_text_m'
#data -src for image 




options = webdriver.ChromeOptions()
options.headless = True

driver_path = r'../webdriver/chromedriver.exe'
driver  = webdriver.Chrome(executable_path = driver_path, options = options)

print(f'requested: {url}')

driver.get(url)

author_class = 'turbo-author__name'
text_class  = 'paragraph unit_text_m'


print(f'got response')
elements = driver.findAll('body')
for el in elements:
    print(el)

def list_inner(e):
    inner = e.get_attribute("innerHTML")
    for el in inner.children:
        print(el)     


driver.quit()


