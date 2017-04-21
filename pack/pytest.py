'''
Created on Apr 20, 2017

@author: evan
'''
import urllib2

page=2
"http://www.qiushibaike.com/hot/page/2/?s=4975806"
# url='http://www.qiushibaike.com/hot/page/'+str(page)+'/?s=4975806'
# print url
url='http://www.baidu.com'
print url
# request = urllib2.Request(url)
respon = urllib2.urlopen(url)
print respon.read()
