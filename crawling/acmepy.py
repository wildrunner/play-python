#!/usr/bin/env python
# -*- coding:utf-8 -*-

import SimpleHTTPServer
import SocketServer
import json
from pyquery import PyQuery as pq
from urlparse import urlparse

#f = open("target.html")
#html = f.read()
#f.close()
#html = unicode(html, 'utf-8')
DOMAIN = 'http://www.acmeshop.co.kr'
TOP_URL = DOMAIN + '/front/php/category.php?cate_no=25&page='
BOTTOM_URL = DOMAIN + '/front/php/category.php?cate_no=45&page='
BAG_URL = DOMAIN + '/front/php/category.php?cate_no=24&page='
SHOES_URL = DOMAIN + '/front/php/category.php?cate_no=26&page='
CAP_URL = DOMAIN + '/front/php/category.php?cate_no=117&page='
EYEWEAR_URL = DOMAIN + '/front/php/category.php?cate_no=161&page='
ACC_URL = DOMAIN + '/front/php/category.php?cate_no=27&page='

PRODUCT_IDENTIFIER = 'table[border="0"][cellspacing="0"][cellpadding="0"][width="100%"]'

categoryDic = dict(top=TOP_URL, bottom=BOTTOM_URL, bag=BAG_URL, shoes=SHOES_URL,
				cap=CAP_URL, eyewear=EYEWEAR_URL, acc=ACC_URL)
categoryCount = dict(top=80, bottom=20, bag=80, shoes=20, cap=40, eyewear=32, acc=48)


def createModel(el):
	product = pq(el)
	img = product('img').attr('src')
	url = product('td[align="center"][valign="top"][width="800"][style="padding: 1, 1, 1, 1;"] a').attr('href')
	url = DOMAIN + str(url)
	name = product('font[style="color:#000000;font-size:11px;font-style:normal;font-weight:normal"]').text()
	price = product('font[style="color:#008BCC;font-size:12px;font-style:;font-weight:bold"]').text()
	brand = product('font[style="color:#000000;font-size:12px;font-style:;font-weight:bold"]').text()
	model = dict(img=img, url=url, name=name, price=price, brand=brand)

	return model

class AcmeHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		out = self.wfile

		modelList = []
		query = urlparse(self.path).query
		try:
			params = dict([p.split('=') for p in query.split('&')])
		except:
			params = {}
		category = params['category']
		page = params['page']

		url = categoryDic[category] + page
		q = pq(url=url)

		for i in range(categoryCount[category]+1):
			model = createModel(q(PRODUCT_IDENTIFIER).eq(i))
			modelList.append(model)

		jsonData = json.dumps(modelList)
		out.write(jsonData)

if __name__ == '__main__':
	httpd = SocketServer.TCPServer(('', 8000), AcmeHandler)
	#print 'serving at port', 8000
	httpd.serve_forever()
