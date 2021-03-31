'''
https://stackoverflow.com/questions/2146383/https-connection-python
https://docs.python.org/3/library/http.client.html

@author: peter
'''

import socket

print(socket)

try:
    import ssl
    print ("there is ssl support")
except ImportError:
    print ("error: no ssl support")
    
    

import requests
r = requests.get("https://stackoverflow.com") 
data = r.content  # Content of response

print (r.status_code)  # Status code of response
print (data[:1000])



import http.client as httplib

#httplib.HttpConnection takes the host and port of the remote URL in its constructor, and not the whole URL.
#also must be without ttps:// since : is interpreted as port 

uri = "yandex.ru"
get_req = "/turbo?text=https%3A%2F%2Fitsmycity.ru%2F2015-03-19%2Fv-ekaterinburge-pokazhut-luchshie-roliki-mezhdunarodnogo-festivalya-kannskie-lvy" 




conn = httplib.HTTPSConnection(uri)
conn.request("GET", get_req)
r = conn.getresponse()
print (r.status, r.reason)
data = r.read()
print (data[:1000])




