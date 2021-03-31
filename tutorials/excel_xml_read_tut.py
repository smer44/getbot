'''

https://gist.github.com/hellpanderrr/f5bc0f70ccb637d6fe78

@author: peter


if:
bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: xml. Do you need to install a parser library?

https://stackoverflow.com/questions/24398302/bs4-featurenotfound-couldnt-find-a-tree-builder-with-the-features-you-requeste

pip install lxml


'''
from bs4 import BeautifulSoup
 
path = '../data/imc-urls.numbers'

path = '../data/excel_xml_example.xml'
 
 
def read_excel_xml(path):
    file = open(path).read()
    soup = BeautifulSoup(file,'xml')
    table = []
    #in this version i do not check f all fields mach
    fields = []
    for sheet in soup.findAll('data-set'): 
        #print('data-set:' , sheet)
        sheet_as_list = []
        for row in sheet.findAll('record'):
            print('row: ' , row)
            row_as_list = []
            children = row.findChildren()
            #in this version i do not check f all fields mach
            
            if  not fields:
                for cell in children:
                    fields.append(cell.name)                
            
               
            for cell in children:#findAll('*'):
                print('cell: ', cell, 'cell.name: ' , cell. name , 'cell.text: ' , cell. text )
                #cell is for example <LastName>Johnson</LastName>
                print('cell: ', cell.text)
                row_as_list.append(cell.text)
            sheet_as_list.append(row_as_list)
        table.append(sheet_as_list)
    return fields, table


fields, table = read_excel_xml(path)
print('fields:')
print(fields)
print('table:')
print(table)
