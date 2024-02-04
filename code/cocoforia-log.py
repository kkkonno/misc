import sys
from bs4 import BeautifulSoup

args = sys.argv
html_file_name = args[1]

# open cocoforia log file
with open(html_file_name, encoding='utf-8') as f:
    html_files = f.read()

# import cocoforia log
soup = BeautifulSoup(html_files, "html.parser")

# delete line break from html
[tag.extract() for tag in soup(string='\n')]

# list for fumbles and criticals
fumble = []
critical = []

# parse cocoforia log
for chat in soup.find_all('p'):
    tab = chat.contents[0].text.replace('\n','').replace(' ','')
    name = chat.contents[1].text.replace('\n','').replace(' ','')
    dice = chat.contents[3].text.replace('\n','').replace(' ','')
    
    if ('致命的失敗' in dice): # if the string '致命的失敗' is in dice log
        fumble.append([tab, name, dice])
    if ('決定的成功' in dice): # if the string '決定的成功' is in dice log
        critical.append([tab, name, dice])

# sort list by character name
fumble = sorted(fumble, key=lambda x: x[1])
critical = sorted(critical, key=lambda x: x[1])

# print results
print("======ファンブル======")
for i in range(len(fumble)):
    print (fumble[i][1] + ", " + fumble[i][0] + ", " + fumble[i][2])
print("======クリティカル======")
for i in range(len(critical)):
    print (critical[i][1] + ", " + critical[i][0] + ", " + critical[i][2])


