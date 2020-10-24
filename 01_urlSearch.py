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

sys.stdout = Logger("02_urlBuffer.txt")                             #将终端打印信息缓存到该文件中

print('Enter your vedio weblink:')
url = raw_input()
# "data":{},"firstClipListVid":"x3021vdyca7"}
# var LIST_INFO = {"vid":["e00327xsru8","o0032y6w6pz","l0032vjulbs","t0032m0ciip","j0032p20tyv","x3021vdyca7","f302135mqwe","d30209hx5fi","z0032pcbqld:
compare = re.compile('https://v.qq.com/x/cover/'+r'(\w+?)'+'/'+r'(\w+?)'+'.html')
menu = compare.findall(url)
if menu != []:
    html = urllib2.urlopen(url).read()                               #读取网站源码
    # print('begin source code')
    # print(html)
    # print('end source code')
    compare = re.compile('x/cover/'+menu[0][0]+'/'+r'(\w+?)'+'.html')#设定正则条件，获取视频编码
    org_result = compare.findall(html)                               #根据正则条件遍历符合条件视频编码
    if org_result != []:
        result = list(set(org_result))                               #列表元素去重
        result.sort(key=org_result.index)                            #根据原列表重新排列
        length = len(result)                                         #获取最新列表长度
        for i in range(0, length): 
            print('URL-%d: https://v.qq.com/x/cover/%s/%s.html'%(i+1, menu[0][0], result[i]))
    print('Finish search!')
else:
    print('Invalid URL!')



