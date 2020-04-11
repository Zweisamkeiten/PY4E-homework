import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# cmd 为byte类型，encode将string转为utf-8
# byte类型在socket中传输给服务器。服务器将返回转换为utf-8传回主机
# python3中unicode与string都为string类型
# utf-8是一种动态的协议1 - 4bytes utf-32固定4bytes utf-16固定2bytes asscii 1bytes
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
    # 解码utf-8

mysock.close()
