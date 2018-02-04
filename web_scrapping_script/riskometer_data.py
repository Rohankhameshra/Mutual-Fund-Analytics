from bs4 import BeautifulSoup
import pandas as pd
import requests

plan = []
riskometer = []
data = []

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
	data.append(col_row)

for link in data:
	if(link[0] != '-'):
		url = "http://www.moneycontrol.com" + link[0]
		print url
		r  = requests.get(url)
		website = r.text
		soup = BeautifulSoup(website)
		data = soup.find('div',attrs={'class':'toplft_cl3'})
		data1 = data.find('span', attrs={'class':'FL UC'})
		data2 = soup.find('h1')
		#print data2.text
		#print data1.text
		plan.append(data2.text)
		riskometer.append(data1.text)
df = pd.DataFrame(plan,columns=['Plan_name'])
df['riskometer'] = riskometer
df.to_csv('data8_risk.csv', sep=',')
