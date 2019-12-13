# coding=utf-8
"""
@File    :   demo.py    
@Contact :   13132515202@163.com

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2019/12/13 21:44   LiuHe      1.0         None
"""
# 服务端代码，环境Mac
#!/usr/bin/env python


# 导入库
import socket, threading, os

SIZE = 1024*1024

# 检查当前目录下是否有等下要命名的图片,有的话删除之
def checkFile():
    list = os.listdir('.')
    for iterm in list:
        if iterm == 'image.bmp':
            os.remove(iterm)
            print('remove')
        else:
            pass

# 接受数据线程
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send('Welcome from server!')
    print('receiving, please wait for a second ...')
    while True:
        data = sock.recv(SIZE)
        if not data :
            print('reach the end of file')
            break
        else:
            with open('./image.bmp', 'ab') as f:
                f.write(data)
    sock.close()
    print('receive finished')
    print ('Connection from %s:%s closed.' % addr)


# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口（这里的ip要在不同的情况下更改）
s.bind(('127.0.0.1', 9999))
# 每次只允许一个客户端接入
s.listen(1)
print('Waiting for connection...')
while True:
    sock, addr = s.accept()
    # 建立一个线程用来监听收到的数据
    t = threading.Thread(target = tcplink, args = (sock, addr))
    # 线程运行
    t.start()