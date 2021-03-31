'''
Created on 19.03.2021

@author: peter
'''
import re 

"""
(?=foo)    Lookahead    Asserts that what immediately follows the current position in the string is foo
(?<=foo)    Lookbehind    Asserts that what immediately precedes the current position in the string is foo
(?!foo)    Negative Lookahead    Asserts that what immediately follows the current position in the string is not foo
(?<!foo)    Negative Lookbehind    Asserts that what immediately precedes the current position in the string is not foo

"""




txt = '<!DOCTYPE html><html><head><meta charSet="utf-8"/><title>Sneaky Cat Illustration -Poster | JUNIQE</title><meta name="description" content="Sneaky Cat Illustration -Poster von Laura Graves | Kaufe online bei JUNIQE \xe2\x9c\x93 Zuverl\xc3\xa4ssige Lieferung \xe2\x9c\x93 Entdecke jetzt neue Designs bei JUNIQE!"/><meta name="thumbnail" content="https://product-image.juniqe-production.juniqe.com/media/catalog/product/seo-cache/x800/18/22/18-22-101P/Sneaky-Cat-Laura-Graves-Poster.jpg""""/><meta name="viewport" content="initial-scale=1.0, width=device-width"/><link rel="icon" href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAAAAABWESUoAAACcUlEQVQ4y4WTTWjTYBjHe23zPk+mHSmWNd2yiVgV53ZoBS+aycRehqwHYZSJ3Q6Cox5WdlGPQ/Bgve3gB+rFrVOHCiJrQUFxa8Ex0ZYxENOijKxhonY0bfqaJVs/YNX3mP8vPB//529h6x8iAGLDJ0udSoATPB6BA4K7AEjaA9FERpLS8VuD7TVkByB8OKVWlMziYkapFJNhN2kEQIyXldiIT3A6O32js0op0QcNQFAqzop2hqD+CGP3L1NpuA6AoKxEHKTWGXMmR+Vh2AGIKCmh2nT6NCxcrVDpNDEB5OfVSE1mHH4vC8dylCbcaAAkrMUc2wAQ18DjzXcuaEvJ78thsgVgR1IRzfoIRyY+FGhhshXdy6tD66'

txt +=  "https://another.jpgstr.bmphttpsky-Cat-Laura-Graves-Poster.bmp> https://another.jpgstr.jgpky-Cat-Laura-Graves-Poster.jpg"

must_find= "https://product-image.juniqe-production.juniqe.com/media/catalog/product/seo-cache/x800/18/22/18-22-101P/Sneaky-Cat-Laura-Graves-Poster.jpg"


# dunny why, the options must be combned in groups like that: (?:(?:jpg)|(?:bmp))
# .+? will take a longest possible match
 
pat = r'http[s]?[:]//.+?[.](?:(?:jpg)|(?:bmp))(?=["/>\s]|$)'


url_allowed = r"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~:/?#[]@!$&'()*+,;="

url_hexa = r'[%][0-9a-fA-F]+'


p = re.compile(pat)

res = p.findall(txt)

#a,b = res.span()

print('\n'.join(s for s in res))

#print(txt[a:b])

