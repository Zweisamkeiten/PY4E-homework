#不要取与包名相同的文件名
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
print(type(fhand))
#fhand不read的类型为<class 'http.client.HTTPResponse'>
#print(fhand.read()) 这样可以直接从句柄直接读取完全部

for line in fhand:
    print(line.decode().strip())
