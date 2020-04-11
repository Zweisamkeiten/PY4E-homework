from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter -')
if url == '':
    url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
    #Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
#Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
    #actual problem 'http://py4e-data.dr-chuck.net/known_by_Kelam.html'
    #Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
#Hint: The first character of the name of the last page that you will load is: N

#print(soup)
#print(tags)
for i in range(7):
    html = urlopen(url, context = ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    print(tags[17].contents[0])
    url = tags[17].get('href', None)
    #print(url)
#for tag in tags:
    #print(tag.get('href', None))

