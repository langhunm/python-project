'''
Created on Apr 21, 2017

@author: jerry
'''
import urllib2Bn
try:
    respon = urllib2.urlopen("http://139.217.5.19")
    print respon.read()
except urllib2.URLError,e:
    print e.code
# pattern=respon.compile()

'学习正则表达式 匹配需要的内容'
