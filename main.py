# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import requests
import bs4
import re

def grabPage(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	return requests.get(url, headers=headers)

def findItemPage(barCode):
	url = "https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Dstripbooks&field-keywords={}".format(barCode)
	res = grabPage(url)
	page = bs4.BeautifulSoup(res.text, 'lxml')
	itemNum = re.findall('/dp/(\S+)/', str(page.select('.a-col-right')))[0].partition('/')[0]
	return 'https://www.amazon.com/dp/{}'.format(itemNum)

def stripNumber(string, index=0):
	return str(re.findall('(\d+)', string)[index])

def returnTitle(page):
	try:
		return page.select("#productTitle")[0].getText()
	except:
		return ""

def returnReviewCount(page):
	try:
		return stripNumber(page.select('#acrCustomerReviewText')[0].getText())
	except:
		return ""

def returnUsedPrice(page):
	try:
		return str(page.select(".olp-used .a-link-normal")[0].getText()).partition('$')[2]
	except:
		return ""

def returnNewPrice(page):
	try:
		return str(page.select('.olp-new .a-link-normal')[0].getText()).partition('$')[2]
	except:
		return ""

def returnProductDetails(page):
	try:
		return page.select('#productDetailsTable')[0]
	except:
		return ""

def returnTradeIn(page):
	try:
		return page.select("#tradeInButton_tradeInValue")[0].getText().strip().replace('$', '')
	except:
		return ""

def returnAuthor(page):
	try:
		return page.select('.contributorNameID')[0].getText()
	except:
		return ""

def returnPageCount(page):
	try:
		return stripNumber(returnProductDetails(page).select('li')[0])
	except:
		return ""

def returnPublisher(page):
	try:
		info = returnProductDetails(page).select('li')[1]
		return str(info).partition('/b>')[2].partition('</l')[0].strip()
	except:
		return ""

def returnWeight(page):
	try:
		info = str(returnProductDetails(page).select('li'))
		return re.findall('\d+', str(info.partition("Shipping Weight")[2].partition('(<a')[0]))[0]
	except:
		return ""

def returnOverallSalesRank(page):
	try:
		return str(page.select('#SalesRank')[0]).partition(' in ')[0].partition('#')[2]
	except:
		return ""

def returnSpecificSalesRank(page):
	try:
		return str(page.select('#SalesRank')[0]).partition('_item">')[2].partition('#')[2].partition('</')[0]
	except:
		return ""

def returnInfo(barCode):
	amazonURL = findItemPage(barCode)
	page = bs4.BeautifulSoup(grabPage(amazonURL).text, 'lxml')
	information = {}
	information['itemNumber'] = amazonURL.partition('/dp/')[2]
	information['bookTitle'] = returnTitle(page).strip()
	information['usedPrice'] = returnUsedPrice(page).strip()
	information['newPrice'] = returnNewPrice(page).strip()
	information['reviewCount'] = returnReviewCount(page).strip()
	information['bookPublisher'] = returnPublisher(page).strip()
	information['itemWeight'] = returnWeight(page).strip()
	information['salesRank'] = returnOverallSalesRank(page).strip()
	information['bookRank'] = returnSpecificSalesRank(page).strip()
	return information


while True:
	barCode = raw_input("Enter Barcode: ")
	print returnInfo(barCode)
