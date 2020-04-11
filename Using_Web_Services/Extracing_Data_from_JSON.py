import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url-')
if url == '':
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'
    #actual_data http://py4e-data.dr-chuck.net/comments_372419.json

json_data = urllib.request.urlopen(url, context = ctx).read()
#print(type(json_data))  请求url返回的值为utf-8 bytes类型
#print(type(json_data.decode())) 解码之后类型为str
#decode之后数据格式更整齐
data = json.loads(json_data)
#print(type(data)) json加载后类型为字典
#print(type(json.dumps(data, indent=4))) dumps将对象转为json字符串，缩进为4
#print(data['comments'])
counts = 0
for item in data['comments']:
    count = int(item['count'])
    counts += count

print(counts)

