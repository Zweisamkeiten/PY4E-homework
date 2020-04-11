#South Federal University
#actual_place Spiru Haret University
import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter address:')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    #print(url)
    
    print('Retriving', url)
    urlhandle = urllib.request.urlopen(url, context = ctx).read().decode()
    #urlhandle2 = urllib.request.urlopen(url, context = ctx).read()
    #print(type(urlhandle), type(urlhandle2))      结果 <class 'str'> <class 'bytes'>

    #print(type(json_data))
    try:
        js = json.loads(urlhandle)
    except:
        js = None
    #这里很奇怪的是str 和bytes类型都可以成功解码
    #print(type(js))

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failur To Retrieve ====')
        print(data)
        continue

    #print(json.dumps(js, indent = 4))

    print('PlaceID', js['results'][0]['place_id'])



