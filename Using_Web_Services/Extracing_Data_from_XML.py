import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url-')

if url == '':
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
    #actual_data: http://py4e-data.dr-chuck.net/comments_372418.xml

xml = urllib.request.urlopen(url, context = ctx).read()

#print(xml)
commentinfo = ET.fromstring(xml)
#print(commentinfo)
comments = commentinfo.findall('comments/comment')
#print(comments)
counts = 0
for comment in comments:
    count = int(comment.find('count').text)
    counts += count

print(counts)
