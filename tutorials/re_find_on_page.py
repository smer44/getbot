
import re 

url = "https://yandex.ru/turbo?text=https%3A%2F%2Fitsmycity.ru%2F2012-04-09%2Fbiznes-lanch-nedeli-seazone"

url = 'https://itsmycity.ru/2019-09-13/7-prichin-pobyvat-na-festivale-love-your-health-v-ekaterinburg'


#class = turbo-author__name


author_re = r'<span itemProp\=\"name\" class\=\"turbo-author__name\">[^<]*?</span>'







# grou 0  - all grp, then 1- n for groups in brackets

author_re_in = r'([^<]*?)' 

field_in = r'([^<]*?)' 



author_pre =r'<span itemProp\=\"name\" class\=\"turbo-author__name\">'

author_suf =r'</span>'

time_pre = r'<time[^>]*?>'

time_suf = r'</time>'

#titel_re='<title>Бизнес-ланч недели: «SeaZone»</title>'

titel_pre= '<title>'


titel_suf = '</title>'


#1 - titel
#2 - sub title 
#3 - author
#4 - date 
#5 - picture and download pic 
#6 - text in paragraphs 



#author_re= f'(?<={author_re_before}){author_re_in}(?={author_re_after})'



all_re =  f'(?<={titel_pre}){field_in}(?:{titel_suf})(?:.*?)(?:{author_pre}){field_in}(?:{author_suf})' +\
f'(?:.*?)(?:{time_pre}){field_in}(?={time_suf})'

#lets generate this pattern:


def to_pat(*bs):
    field_in = r'([^<]*?)' 
    between = r'(?:.*?)'
    ex_ln = len(bs)
    assert ex_ln%2 == 0, 'to_pat: there must be even bracket parameters'
    assert ex_ln > 0 , 'to_pat: there must be at least 2 parameters'
    
    if ex_ln  == 2:
        return f'(?<={bs[0]}){field_in}(?={bs[1]})'
    
    s = f'(?<={bs[0]}){field_in}(?:{bs[1]}){between}'
    
    for x in range(2,ex_ln-2,2):
        s+= f'(?:{bs[x]}){field_in}(?:{bs[x+1]}){between}'
    
    s+= f'(?:{bs[ex_ln-2]}){field_in}(?={bs[ex_ln-1]})'
    
    return s
    

all_to_pat = to_pat(titel_pre, titel_suf, author_pre, author_suf, time_pre, time_suf)

print(all_re)
print(all_to_pat)

assert  all_to_pat == all_re



#all_re =  f'(?<={author_pre}){field_in}(?:{author_suf})(?:.*?)(?:{titel_pre})'#{field_in}(?={author_suf})'


#author_re = r'<span itemProp\=\"name\" class\=\"turbo-author__name\">[^<]*?</span>'


file_name = 'get_fields_from_turbo_save'

#file_name = 'save_page_2' 


savefile = f'./{file_name}.txt'




f = open(savefile, 'r', encoding="utf-8")

data = f.read()
#print(data)
f.close()




m = re.search(all_re, data,re.DOTALL)



print('regex found:')

if m :
    print(m.group(1))
    print(m.group(2))
    print(m.group(3))
else:
    print('no pattern found')



#print('\n'.join(s for s in res))