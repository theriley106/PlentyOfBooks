import requests
import bs4
import re


def findItemPage(barCode):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	url = "https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Dstripbooks&field-keywords={}".format(barCode)
	res = requests.get(url, headers=headers)
	page = bs4.BeautifulSoup(res.text, 'lxml')
	itemNum = re.findall('/dp/(\S+)/', str(page.select('.a-col-right')))[0].partition('/')[0]
	return 'https://www.amazon.com/dp/{}'.format(itemNum)

findItemPage('9780470769058')