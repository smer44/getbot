"""
A comma-separated values (CSV) file is a delimited text file that uses a 
comma to separate values. Each line of the file is a data record.
 Each record consists of one or more fields, separated by commas. 
 The use of the comma as a field separator is the source of the name 
 for this file format. A CSV file typically stores tabular data 
 (numbers and text) in plain text, in which case each line will 
 have the same number of fields.

The CSV file format is not fully standardized. The basic idea of 
separating fields with a comma is clear, but the situation gets 
complicated when field data also contain commas or embedded line
breaks. CSV implementations may not handle such field data, or 
they may use quotation marks to surround the field. Quotation does
not solve everything: some fields may need embedded quotation marks,
so a CSV implementation may include escape characters or escape sequences.
"""

import csv
import pprint as pp


class xAny:
    
    def __init__(self, fields, values):
        assert len(fields) == len(values)
        for field,value in zip(fields, values):
            #print(field,value )
            setattr(self, field, value)
        
    """    
    def fields(self):
        return (a for a in dir(self) if not a.startswith('__'))    
    """
    
    def __str__(self):
        s = '{'
        for k,v in self.__dict__.items():
            s += str(k) + ' : ' + str(v) + '\n '
        return s + '}'
    

      
        
            



url = '../data/urls.csv'


csvfile= open(url, encoding='utf-8')

spamreader = csv.reader(csvfile)


columns = next(spamreader) 

print(columns)

rows = [ tuple(row) for row in spamreader]


objs = [xAny(columns, row) for row in rows[:10]]

## traing to get this address 

turbo = 'https://yandex.ru/turbo?text='

test_page = 'https://itsmycity.ru/2019-09-13/7-prichin-pobyvat-na-festivale-love-your-health-v-ekaterinburgitsmycity.ru/дата/url'

## load address: 

import requests


def get_content(obj):
    url = turbo + obj.url if obj.turboPage else obj.url 
    print('conneting to:' , url)
    r = requests.get(url)
    print(r.status_code)
    data = r.content
    print (data[:100])
    return data

obj = objs[2]

print(obj)

get_content(obj)
    

