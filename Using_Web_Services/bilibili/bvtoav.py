import urllib.request, urllib.error, urllib.parse
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

server_url = 'https://api.bilibili.com/x/web-interface/view?bvid='

while True:
    bvid = input('Enter BV:')
    if len(bvid) < 1:
        print('Invalid BV')
        continue
    url = server_url + bvid
    try:
        uh = urllib.request.urlopen(url, context = ctx)
    except:
        print('Request ERROR')
        continue

    data = uh.read().decode()
    js = json.loads(data)
    #print(json.dumps(js, indent = 4))
    #print(js['data'])
    print('AV:', str(js['data']['aid']))
    print('分区:', js['data']['tname'])
    print('标题:', js['data']['title'])
    print('简介:', js['data']['desc'])
    print('播放量:', js['data']['stat']['view'])
    print('弹幕数:', js['data']['stat']['danmaku'])
    print('回复:', js['data']['stat']['reply'])
    print('收藏:', js['data']['stat']['favorite'])
    print('硬币:', js['data']['stat']['coin'])
    print('分享:', js['data']['stat']['share'])
    print('点赞:', js['data']['stat']['like'])

