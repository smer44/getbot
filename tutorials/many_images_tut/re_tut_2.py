'''
Created on 29.03.2021

@author: peter
'''
import re 

#The final metacharacter in this section is ..
# It matches anything except a newline character, 
# and there’s an alternate mode (re.DOTALL) 
# where it will match even a newline. . 
# is often used where you want to match “any character”.

text = " <title> funny stuff </title>\n\n trololo <tro> trololo </tro><author> booba </author>"

field_in = r'([^<]*?)' 

titel_pre= '<title>'


titel_suf = '</title>'

author_pre= '<author>'


author_suf = '</author>'

all_re =  f'(?<={titel_pre}){field_in}(?:{titel_suf})(?:.*?)(?:{author_pre}){field_in}(?={author_suf})'

print(all_re)


m = re.search(all_re, text, re.DOTALL)

print('regex found:')

if m :
    #print(m.group(0))
    print(m.group(1))
    print(m.group(2))
else:
    print('no pattern found')
    
    
    
    