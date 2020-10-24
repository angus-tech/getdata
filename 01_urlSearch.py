# -*- coding:utf-8 -*-

import urllib2
import re
import sys

class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

sys.stdout = Logger("02_urlBuffer.txt")                                         #将终端打印信息缓存到该文件中

print('Enter your vedio weblink:')
set_url = raw_input()
compare = re.compile('.*?'+'x/cover/'+r'(\w+?)'+'/'+r'(\w+?)'+'.html')          #根据输入网址检索关键字
menu = compare.findall(set_url)
if menu != []:
    org_url = ('https://v.qq.com/x/cover/%s/%s.html'%(menu[0][0], menu[0][1]))  #组装链接进行网站访问
    html = urllib2.urlopen(org_url).read()                                      #读取网站源码
    compare = re.compile('LIST_INFO = {"vid":\['+r'(.*?)'+r'],'+'.*?'+'"firstClipListVid":"'+r'(.*?)'+'"}')#读取list info数据
    list_all = compare.findall(html)
    compare = re.compile('"'+r'(.*?)'+'"')                                      #提取有效视频编号
    list_cod = compare.findall(list_all[0][0])
    length = len(list_cod)
    for i in range(0, length):
        if list_cod[i] != list_all[0][1]:                                       #排除干扰视频源
            print('URL-%d: https://v.qq.com/x/cover/%s/%s.html'%(i+1, menu[0][0], list_cod[i]))
        else:
            break
    print('Finish search!')
else:
    print('Invalid URL!')
