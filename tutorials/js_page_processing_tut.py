'''
tutorial how to execute javascript content on web page with selenium :

https://selenium-python.readthedocs.io/installation.html


https://chromedriver.chromium.org/getting-started


phantomjs binary:
https://phantomjs.org/download.html

phantomjs is deprecated

custom scripts can be executed 

install selenum module:

pip3 install selenium




@author: peter
'''


from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.biodiversitylibrary.org/item/99488#page/587/mode/1up"

#myscript = settings.get_js_code() # here I get content of *.js file
#driver = webdriver.PhantomJS()

options = webdriver.ChromeOptions()
options.headless = True

driver_path = r'../webdriver/chromedriver.exe'
#driver_path = r'../webdriver/phantomjs/bin/phantomjs.exe'

driver  = webdriver.Chrome(executable_path = driver_path, options = options)
#driver  = webdriver.PhantomJS(executable_path = driver_path)


driver.get(url)
print('got uri')

#prints raw page source:
#print(driver.page_source)

#execute all pages javascript:
#html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
#print (html)

elements = driver.find_elements(By.TAG_NAME, 'script')
for e in elements:
    print (e)
    print ('element.text:',format(e.text))
    print ('element.get_attribute(\'value\'):', format(e.get_attribute('value')))
    inner = e.get_attribute("innerHTML")#  -> inner is string 
    print ('element.get_attribute(\'innerHTML\'):',  type(inner) , inner)
    
#result = driver.execute_script(myscript)
driver.quit()