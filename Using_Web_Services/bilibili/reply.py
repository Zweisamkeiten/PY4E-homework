import urllib.request, urllib.parse, urllib.error
import json
import ssl

page = 1
server_url_reply ='http://api.bilibili.com/x/v2/reply?jsonp=jsonp&;pn='
server_url_video = 'https://api.bilibili.com/x/web-interface/view?bvid='

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    bvid = input('Enter BV:')
    if len(bvid) < 1:
        print('Invalid BV')
        continue

    url_video = server_url_video + bvid
    uh_video = urllib.request.urlopen(url_video, context = ctx)
    data_video = uh_video.read().decode()
    js_video = json.loads(data_video)
    avid = str(js_video['data']['aid'])

    max_pages = int(js_video['data']['stat']['reply']) // 20
    for page in range(1, max_pages):
        url_reply = server_url_reply+str(page)+'&type=1&oid=' + avid
        uh = urllib.request.urlopen(url_reply, context = ctx)
        data = uh.read().decode()
        if(len(data) < 1): break
        #print(data)
        js = json.loads(data)
        #print(json.dumps(js, indent = 4))
        for count in range(0, 19):
            print('id:', js['data']['replies'][count]['member']['uname'])
            print('comment:', js['data']['replies'][count]['content']['message'])
