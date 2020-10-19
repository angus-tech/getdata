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

sys.stdout = Logger("test.txt")

print('Enter your URL:')
url = raw_input()
compare = re.compile('https://v.qq.com/x/cover/'+r'(\w+?)'+'/'+r'(\w+?)'+'.html')
menu = compare.findall(url)
if menu != []:
    html = urllib2.urlopen(url).read()
    
    compare = re.compile('x/cover/'+menu[0][0]+'/'+r'(\w+?)'+'.html')
    org_result = compare.findall(html)
    if org_result != []:
        result = list(set(org_result))
        result.sort(key=org_result.index)
        length = len(result)
        for i in range(0, length): 
            print('URL-%d: https://v.qq.com/x/cover/%s/%s.html'%(i+1, menu[0][0], result[i]))
else:
    print('Invalid URL.')



