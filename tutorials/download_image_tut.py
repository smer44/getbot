
'''
File download tutorial with 
https://stackabuse.com/download-files-with-python/

'''
url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'


import urllib.request

print('Beginning file download with urllib.request...')


urllib.request.urlretrieve(url, './download_image_tut_urllib.jpg')



import requests



print('Beginning file download with requests module')
r = requests.get(url)

with open('./download_image_tut_requests.jpg', 'wb') as f:
    f.write(r.content)

# Retrieve HTTP meta-data
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)


import wget

print('Beginning file download with wget module')


wget.download(url, './download_image_tut_wget.jpg')


