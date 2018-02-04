# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import pandas as pd
import requests

links = []
url2 = 'http://www.moneycontrol.com/mf/mf_info/hist_tech_chart.php?im_id=MSB087&dd=01&mm=01&yy=2013&t_dd=21&t_mm=01&t_yy=2018&range=max'
r  = requests.get(url2)
website = r.text

file = open("testfile.csv","w") 
file.write(website)
file.close()
data = pd.read_csv("testfile.csv", header = None, names = ['date', 'nav', '1', '2', '3', '4'])
data2 = data.transpose()
data2.columns = data['date']
data2 = data2[:0][:]
#print data2

url = "http://www.moneycontrol.com/mutual-funds/amc-details/SB"
r  = requests.get(url)
website = r.text
soup = BeautifulSoup(website)
data1 = soup.find('div', attrs={'class':'boxBg FL MT10'})
# table_body = data1.find('tbody')

rows = data1.find_all('tr')
#print rows[1]
#cols = rows[1].find_all('td')
#count = 0
#print cols[0].find('a').get('href')

for row in rows:
	cols = row.find_all('td')
	col_row = []
	for col in cols:
		try:
			col_row.append(col.find('a').get('href'))
		except:
			col_row.append('-')
		col_row.append(col.text)
	#cols = [ele.text.strip() for ele in cols]
	
	#data.append([ele for le in cols if ele])
	links.append(col_row)

for link in links:
	if(link[0] != '-'):
		url = "http://www.moneycontrol.com" + link[0]
		fund_name = url.split('/')[5]
		fund_code = url.split('/')[6]
		url1 = 'http://www.moneycontrol.com/mf/mf_info/hist_tech_chart.php?im_id=' + fund_code + '&dd=01&mm=01&yy=2013&t_dd=21&t_mm=01&t_yy=2018&range=max'
		print url1
		r  = requests.get(url1)
		website = r.text

		file = open("testfile.csv","w") 
		file.write(website)
		file.close()
		data = pd.read_csv("testfile.csv", header = None, names = ['date', 'nav', '1', '2', '3', '4'])
		print data.shape[0]
		if (data.shape[0] > 0):
			temp_data = data.transpose()
			temp_data.columns = data['date']
			temp_data = temp_data[1:2][:]
			temp_data['fund_name'] = fund_name
			data2 = pd.concat([data2, temp_data], ignore_index=True)
			# print data2

		# for i in range(0,data.s)
data2.to_csv('SBI_NAV.csv', sep=',')