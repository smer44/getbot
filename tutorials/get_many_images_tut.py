
'''
Created on 19.03.2021

@author: peter
'''
import http.client as ht

uri ="https://nobelpfoten.de/products/die-prinzessin-haustier-poster?variant=31944576499786&currency=EUR&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&gclid=CjwKCAjw9MuCBhBUEiwAbDZ-7vuJWQycto7R1_vALs_KuaYRdBD_5q8S_4JpTso5KrWfQINk7IciWxoC7k0QAvD_BwE"
# why denied
uri = "https://www.juniqe.de/sneaky-cat-premium-poster-portrait-2077819.html?gclid=CjwKCAjw9MuCBhBUEiwAbDZ-7tauONz8arvUmAlChO7y9AYzgRoi98gsrcFipp3HY38cFgSabcnaThoClgMQAvD_BwE#step=design&productId=2077855"


uri = "https://www.juniqe.de/sneaky-cat-premium-poster-portrait-2077819.html?gclid=CjwKCAjw9MuCBhBUEiwAbDZ-7tauONz8arvUmAlChO7y9AYzgRoi98gsrcFipp3HY38cFgSabcnaThoClgMQAvD_BwE#step=design&productId=3365989&frameId=false"

uri = "https://www.catslove.com/"

ur = "https://sam-cat.fandom.com/de/wiki/Cat_Valentine"

def uri_to_host_and_get(uri):
    '''
    makes from common http or https uri (<host> ,<get request>) tuple
    '''    
    prot, uri = uri.split('://')    
    return uri.split('/',1)

uri, get_req = uri_to_host_and_get(uri)

print(uri, get_req )

conn = ht.HTTPSConnection(uri)
conn.request("GET", '/' + get_req)
r = conn.getresponse()
print (r.status, r.reason)
data = r.read().decode()

# get all images:

import re 

uri_forbiden= r'"<>\\^`{|}'


pat = r'http[s]?[:]//.+?[.](?:(?:jpg)|(?:bmp))(?=["<>/\s\\^`{|}]|$)'
p = re.compile(pat)

res = set(p.findall(data))# so the entries do not repeat

print('\n'.join(s for s in res))


#download images into files:

count = 0
filename = f'./many_images_tut/{count}.jpg'

import urllib.request

import os
#from tutorials.os_tut import ensureFolder

os.makedirs('./many_images_tut/', exist_ok = True)

#ensureFolder('./many_images_tut/')

for uri in res: 
    print(f'Beginning file download with urllib.request... : {uri}')
    urllib.request.urlretrieve(uri, filename)
    count += 1
    filename = f'./many_images_tut/{count}.jpg'





