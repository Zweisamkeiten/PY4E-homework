from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url:')
if url == '':
    url = 'http://py4e-data.dr-chuck.net/comments_42.html'
    #actual_test_url = http://py4e-data.dr-chuck.net/comments_372416.html
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

#print(soup)
tags = soup('tr')
flag = 0
total = 0
for tag in tags:
    if flag == 0:
        flag = 1
        continue
    #print(tag)
    #print(tag.td.contents[0])
    #print(tag.span.get('class', None))
    #print(tag.span.contents[0])
    number = int(tag.span.contents[0])
    total += number
print(total)
