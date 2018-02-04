from bs4 import BeautifulSoup
import pandas as pd
import requests
import mechanize
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

data = []
mfcode = pd.read_csv('mutual_fund_code - Sheet1.csv')
#print mfcode

#url = 'http://www.imdb.com/search/title?year='+str(movie_year)+','+str(movie_year)+'&title_type=feature&sort=moviemeter,asc&page=' + str(page) + '&ref_=adv_nxt'
#r  = requests.get(url)

page_links = []
links = []
fund_family = []
fund_class = []
plan = []
fund_type = []
Investment_plan = []
Asset_size = []
Min_Investment = []
Last_divident = []
Bonus = []
Entry_Load = []
Exit_Load = []
Benchmark = []
Launch_date = []
performance_returns_1_mth = []
performance_returns_3_mth = []
performance_returns_6_mth = []
performance_returns_1_year = []
performance_returns_2_year = []
performance_returns_3_year = []
performance_returns_5_year = []
performance_rank_1_mth = []
performance_rank_3_mth = []
performance_rank_6_mth = []
performance_rank_1_year = []
performance_rank_2_year = []
performance_rank_3_year = []
performance_rank_5_year = []
performance_absolute_returns_2017_Qtr1 = []
performance_absolute_returns_2016_Qtr1 = []
performance_absolute_returns_2015_Qtr1 = []
performance_absolute_returns_2014_Qtr1 = []
performance_absolute_returns_2013_Qtr1 = []
performance_absolute_returns_2017_Qtr2 = []
performance_absolute_returns_2016_Qtr2 = []
performance_absolute_returns_2015_Qtr2 = []
performance_absolute_returns_2014_Qtr2 = []
performance_absolute_returns_2013_Qtr2 = []
performance_absolute_returns_2017_Qtr3 = []
performance_absolute_returns_2016_Qtr3 = []
performance_absolute_returns_2015_Qtr3 = []
performance_absolute_returns_2014_Qtr3 = []
performance_absolute_returns_2013_Qtr3 = []
performance_absolute_returns_2017_Qtr4 = []
performance_absolute_returns_2016_Qtr4 = []
performance_absolute_returns_2015_Qtr4 = []
performance_absolute_returns_2014_Qtr4 = []
performance_absolute_returns_2013_Qtr4 = []
performance_absolute_returns_2017_annual = []
performance_absolute_returns_2016_annual = []
performance_absolute_returns_2015_annual = []
performance_absolute_returns_2014_annual = []
performance_absolute_returns_2013_annual = []
nav_52_week_high = []
#nav_52_week_high_date = []
nav_52_week_low = []
#nav_52_week_low_date = []
portfolio_equity_1 = []
portfolio_equity_2 = []
portfolio_equity_3 = []
portfolio_equity_4 = []
portfolio_equity_5 = []
portfolio_equity_6 = []
portfolio_equity_7 = []
portfolio_equity_8 = []
portfolio_equity_9 = []
portfolio_equity_10 = []
portfolio_sector_1 = []
portfolio_sector_2 = []
portfolio_sector_3 = []
portfolio_sector_4 = []
portfolio_sector_5 = []
portfolio_sector_6 = []
portfolio_sector_7 = []
portfolio_sector_8 = []
portfolio_sector_9 = []
portfolio_sector_10 = []
portfolio_value_1 = []
portfolio_value_2 = []
portfolio_value_3 = []
portfolio_value_4 = []
portfolio_value_5 = []
portfolio_value_6 = []
portfolio_value_7 = []
portfolio_value_8 = []
portfolio_value_9 = []
portfolio_value_10 = []
portfolio_asset_1 = []
portfolio_asset_2 = []
portfolio_asset_3 = []
portfolio_asset_4 = []
portfolio_asset_5 = []
portfolio_asset_6 = []
portfolio_asset_7 = []
portfolio_asset_8 = []
portfolio_asset_9 = []
portfolio_asset_10 = []

portfolio_asset_allocation_eqity = []
portfolio_asset_allocation_others = []
portfolio_asset_allocation_debt = []
portfolio_asset_allocation_mutual_funds = []
portfolio_asset_allocation_money_market = []
portfolio_asset_allocation_cash_call = []

portfolio_concentration_holding_top5 = []
portfolio_concentration_holding_top10 = []
portfolio_concentration_sector_top3 = []

portfolio_sector_right_bottom_1 = []
portfolio_sector_right_bottom_2 = []
portfolio_sector_right_bottom_3 = []
portfolio_sector_right_bottom_4 = []
portfolio_sector_right_bottom_5 = []
portfolio_sector_right_bottom_6 = []

portfolio_sector_percentage_right_bottom_1 = []
portfolio_sector_percentage_right_bottom_2 = []
portfolio_sector_percentage_right_bottom_3 = []
portfolio_sector_percentage_right_bottom_4 = []
portfolio_sector_percentage_right_bottom_5 = []
portfolio_sector_percentage_right_bottom_6 = []

portfolio_sector_high_right_bottom_1 = []
portfolio_sector_high_right_bottom_2 = []
portfolio_sector_high_right_bottom_3 = []
portfolio_sector_high_right_bottom_4 = []
portfolio_sector_high_right_bottom_5 = []
portfolio_sector_high_right_bottom_6 = []

portfolio_sector_low_right_bottom_1 = []
portfolio_sector_low_right_bottom_2 = []
portfolio_sector_low_right_bottom_3 = []
portfolio_sector_low_right_bottom_4 = []
portfolio_sector_low_right_bottom_5 = []
portfolio_sector_low_right_bottom_6 = []

asset_size_1date = []
asset_size_1value = []
asset_size_2date = []
asset_size_2value = []
asset_size_3date = []
asset_size_3value = []
asset_size_4date = []
asset_size_4value = []
asset_size_5date = []
asset_size_5value = []
asset_size_6date = []
asset_size_6value = []
asset_size_7date = []
asset_size_7value = []
asset_size_8date = []
asset_size_8value = []
asset_size_9date = []
asset_size_9value = []
asset_size_10date = []
asset_size_10value = []
asset_size_11date = []
asset_size_11value = []
asset_size_12date = []
asset_size_12value = []
asset_size_13date = []
asset_size_13value = []
asset_size_14date = []
asset_size_14value = []
asset_size_15date = []
asset_size_15value = []
asset_size_16date = []
asset_size_16value = []
asset_size_17date = []
asset_size_17value = []
asset_size_18date = []
asset_size_18value = []
asset_size_19date = []
asset_size_19value = []
asset_size_20date = []
asset_size_20value = []
#asset_size_21date = []
#asset_size_21value = []


#for x in mfcode['code']:
x = 'SB'
print x
url = "http://nseindia.moneycontrol.com/mutualfundindia/advanced_search/commonsearch.php?head=&currentpage=0&pgno=1&fundFamily=" + x + "&invObj=all&"
r  = requests.get(url)
website = r.text
website_soup = BeautifulSoup(website)
temp = website_soup.find('div', attrs={'class':'FL paging'})
pages = temp.find_all('a')
count = int(0)
for page in pages:
	count += 1
	#if count < 4:
	if (count >=4)&(count < 8):
	#if (count >=8)&(count < 12):
	#if (count >=12)&(count < 16):
		url = page.get('href')
		if (url == 'javascript:void(0);'):
			url_final = "http://nseindia.moneycontrol.com/mutualfundindia/advanced_search/commonsearch.php?head=&currentpage=0&pgno=1&fundFamily=" + x + "&invObj=all&"
		else:
			url_final = "http://nseindia.moneycontrol.com" + url
		print url_final
		r = requests.get(url_final)
		data_temp = r.text
		data_temp_soup = BeautifulSoup(data_temp)
		fund_link_table = data_temp_soup.find('table', attrs={"bgcolor":"#ffffff"})
		fund_link_table_tr = fund_link_table.find_all('tr')
		for row in fund_link_table_tr:
			xa = row.find_all('a')
			if(len(xa) >= 1):
				#print xa[0].get('href')
				links.append(xa[0].get('href'))
			#temp_link = row.find('a', href=True)
			#links.append(temp_link["href"])

#print links
#links = ['/mutualfundindia/snapshot.php?im_id=MBS099']
for link in links:
	url = "http://nseindia.moneycontrol.com" + link
	print url
	#http://nseindia.moneycontrol.com/mutualfundindia/scheme_assets.php?im_id=MBS099
	r = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data)
	fund_plan_1 = soup.find('h1')
	try:
		plan.append(fund_plan_1.text)
	except:
		plan.append('-')
	fund_class_1 = soup.find('div', attrs={'class':'FL b_11 PL20'})
	temp_str = fund_class_1.text
	temp_str1 = temp_str.split(u'\xa0')
	try:
		fund_family.append(temp_str1[3][:-12])
	except:
		fund_family.append('-')
	try:
		fund_class.append(temp_str1[7])
	except:
		fund_class.append('-')
	table_data_1 = soup.find('div', attrs={'class':'MT20 brd', 'style':'width:752px'})
	data_table = table_data_1.find('div', attrs={'class':'PA10'})
	
	data_table1 = data_table.find('div', attrs={'class':'FL'})
	#print data_table1
	table_body = data_table1.find('table')
	rows = table_body.find_all('tr')
	temp_table = []
	for row in rows:
		cols = row.find_all('td')
		col_row = []
		for col in cols:
			col_row.append(col.text)
		temp_table.append(col_row)
	#print temp_table
	try:
		fund_type.append(temp_table[0][0])
	except:
		fund_type.append('-')
	try:
		Investment_plan.append(temp_table[1][0])
	except:
		Investment_plan.append('-')
	try:
		Asset_size.append(temp_table[2][0])
	except:
		Asset_size.append('-')
	try:
		Min_Investment.append(temp_table[3][1])
	except:
		Min_Investment.append('-')
	try:
		Last_divident.append(temp_table[4][1])
	except:
		Last_divident.append('-')
	try:
		Bonus.append(temp_table[5][1])
	except:
		Bonus.append('-')
	try:
		Entry_Load.append(temp_table[6][1])
	except:
		Entry_Load.append('-')
	try:
		Exit_Load.append(temp_table[7][1])
	except:
		Exit_Load.append('-')
	data_table1 = data_table.find('div', attrs={'class':'FR'})
	#print data_table1
	table_body = data_table1.find('table')
	rows = table_body.find_all('tr')
	temp_table = []
	for row in rows:
		cols = row.find_all('td')
		col_row = []
		for col in cols:
			col_row.append(col.text)
		temp_table.append(col_row)
	#print temp_table[3][0][15:]
	Benchmark.append(temp_table[2][0][13:])
	Launch_date.append(temp_table[3][0][15:])
	table_data_1 = soup.find_all('div', attrs={'class':'MT20'})
	
	data_table = table_data_1[1].find('div', attrs={'class':'FL'})
	#print data_table
	#data_table1 = data_table.find('div', attrs={'class':'FL'})
	table_body = data_table.find('table')
	rows = table_body.find_all('tr')
	temp_table = []
	for row in rows:
		cols = row.find_all('td')
		col_row = []
		for col in cols:
			col_row.append(col.text)
		temp_table.append(col_row)
	#print temp_table
	try:
		performance_returns_1_mth.append(temp_table[1][1])
		performance_rank_1_mth.append(temp_table[1][2])
		performance_returns_3_mth.append(temp_table[2][1])
		performance_rank_3_mth.append(temp_table[2][2])
		performance_returns_6_mth.append(temp_table[3][1])
		performance_rank_6_mth.append(temp_table[3][2])
		performance_returns_1_year.append(temp_table[4][1])
		performance_rank_1_year.append(temp_table[4][2])
		performance_returns_2_year.append(temp_table[5][1])
		performance_rank_2_year.append(temp_table[5][2])
		performance_returns_3_year.append(temp_table[6][1])
		performance_rank_3_year.append(temp_table[6][2])
		performance_returns_5_year.append(temp_table[7][1])
		performance_rank_5_year.append(temp_table[7][2])
	except:
		performance_returns_1_mth.append('-')
		performance_rank_1_mth.append('-')
		performance_returns_3_mth.append('-')
		performance_rank_3_mth.append('-')
		performance_returns_6_mth.append('-')
		performance_rank_6_mth.append('-')
		performance_returns_1_year.append('-')
		performance_rank_1_year.append('-')
		performance_returns_2_year.append('-')
		performance_rank_2_year.append('-')
		performance_returns_3_year.append('-')
		performance_rank_3_year.append('-')
		performance_returns_5_year.append('-')
		performance_rank_5_year.append('-')
	data_table = table_data_1[1].find('div', attrs={'class':'FR'})
	#print data_table
	#data_table1 = data_table.find('div', attrs={'class':'FL'})
	table_body = data_table.find('table')
	rows = table_body.find_all('tr')
	temp_table = []
	for row in rows:
		cols = row.find_all('td')
		col_row = []
		for col in cols:
			col_row.append(col.text)
		temp_table.append(col_row)
	#print temp_table
	try:
		performance_absolute_returns_2017_Qtr1.append(temp_table[1][1])
		performance_absolute_returns_2017_Qtr2.append(temp_table[1][2])
		performance_absolute_returns_2017_Qtr3.append(temp_table[1][3])
		performance_absolute_returns_2017_Qtr4.append(temp_table[1][4])
		performance_absolute_returns_2017_annual.append(temp_table[1][5])
	except:
		performance_absolute_returns_2017_Qtr1.append('-')
		performance_absolute_returns_2017_Qtr2.append('-')
		performance_absolute_returns_2017_Qtr3.append('-')
		performance_absolute_returns_2017_Qtr4.append('-')
		performance_absolute_returns_2017_annual.append('-')
	try:
		performance_absolute_returns_2016_Qtr1.append(temp_table[2][1])
		performance_absolute_returns_2016_Qtr2.append(temp_table[2][2])
		performance_absolute_returns_2016_Qtr3.append(temp_table[2][3])
		performance_absolute_returns_2016_Qtr4.append(temp_table[2][4])
		performance_absolute_returns_2016_annual.append(temp_table[2][5])
	except:
		performance_absolute_returns_2016_Qtr1.append('-')
		performance_absolute_returns_2016_Qtr2.append('-')
		performance_absolute_returns_2016_Qtr3.append('-')
		performance_absolute_returns_2016_Qtr4.append('-')
		performance_absolute_returns_2016_annual.append('-')
	try:
		performance_absolute_returns_2015_Qtr1.append(temp_table[3][1])
		performance_absolute_returns_2015_Qtr2.append(temp_table[3][2])
		performance_absolute_returns_2015_Qtr3.append(temp_table[3][3])
		performance_absolute_returns_2015_Qtr4.append(temp_table[3][4])
		performance_absolute_returns_2015_annual.append(temp_table[3][5])
	except:
		performance_absolute_returns_2015_Qtr1.append('-')
		performance_absolute_returns_2015_Qtr2.append('-')
		performance_absolute_returns_2015_Qtr3.append('-')
		performance_absolute_returns_2015_Qtr4.append('-')
		performance_absolute_returns_2015_annual.append('-')
	try:
		performance_absolute_returns_2014_Qtr1.append(temp_table[4][1])
		performance_absolute_returns_2014_Qtr2.append(temp_table[4][2])
		performance_absolute_returns_2014_Qtr3.append(temp_table[4][3])
		performance_absolute_returns_2014_Qtr4.append(temp_table[4][4])
		performance_absolute_returns_2014_annual.append(temp_table[4][5])
	except:
		performance_absolute_returns_2014_Qtr1.append('-')
		performance_absolute_returns_2014_Qtr2.append('-')
		performance_absolute_returns_2014_Qtr3.append('-')
		performance_absolute_returns_2014_Qtr4.append('-')
		performance_absolute_returns_2014_annual.append('-')
	try:
		performance_absolute_returns_2013_Qtr1.append(temp_table[5][1])
		performance_absolute_returns_2013_Qtr2.append(temp_table[5][2])
		performance_absolute_returns_2013_Qtr3.append(temp_table[5][3])
		performance_absolute_returns_2013_Qtr4.append(temp_table[5][4])
		performance_absolute_returns_2013_annual.append(temp_table[5][5])
	except:
		performance_absolute_returns_2013_Qtr1.append('-')
		performance_absolute_returns_2013_Qtr2.append('-')
		performance_absolute_returns_2013_Qtr3.append('-')
		performance_absolute_returns_2013_Qtr4.append('-')
		performance_absolute_returns_2013_annual.append('-')

	data_table = table_data_1[2].find('div', attrs={'class':'FL'})
	table_body = data_table.find('table')
	rows = table_body.find_all('tr')
	temp_table = []
	for row in rows:
		cols = row.find_all('td')
		col_row = []
		for col in cols:
			col_row.append(col.text)
		temp_table.append(col_row)
	#print temp_tab5e
	try:
		nav_52_week_low.append(temp_table[1][1])
		nav_52_week_high.append(temp_table[1][0])
	except:
		nav_52_week_low.append('-')
		nav_52_week_high.append('-')
	data_table = table_data_1[3].find('div', attrs={'class':'FL'})
	table_body = data_table.find('table', attrs={'class':'tbl_n'})
	#print table_body
	rows = table_body.find_all('tr')
	#print rows
	temp_table = []
	for row in rows:
		cols = row.find_all('td')
		col_row = []
		for col in cols:
			col_row.append(col.text)
		temp_table.append(col_row)

	#print temp_table
	try:
		portfolio_sector_1.append(temp_table[1][1])
		portfolio_value_1.append(temp_table[1][2])
		portfolio_asset_1.append(temp_table[1][3])
		portfolio_equity_1.append(temp_table[1][0])
	except:
		portfolio_equity_1.append('-')
		portfolio_sector_1.append('-')
		portfolio_value_1.append('-')
		portfolio_asset_1.append('-')
	try:
		portfolio_equity_2.append(temp_table[2][0])
		portfolio_sector_2.append(temp_table[2][1])
		portfolio_value_2.append(temp_table[2][2])
		portfolio_asset_2.append(temp_table[2][3])
	except:
		portfolio_equity_2.append('-')
		portfolio_sector_2.append('-')
		portfolio_value_2.append('-')
		portfolio_asset_2.append('-')
	try:
		portfolio_equity_3.append(temp_table[3][0])
		portfolio_sector_3.append(temp_table[3][1])
		portfolio_value_3.append(temp_table[3][2])
		portfolio_asset_3.append(temp_table[3][3])
	except:
		portfolio_equity_3.append('-')
		portfolio_sector_3.append('-')
		portfolio_value_3.append('-')
		portfolio_asset_3.append('-')
	try:
		portfolio_equity_4.append(temp_table[4][0])
		portfolio_sector_4.append(temp_table[4][1])
		portfolio_value_4.append(temp_table[4][2])
		portfolio_asset_4.append(temp_table[4][3])
	except:
		portfolio_equity_4.append('-')
		portfolio_sector_4.append('-')
		portfolio_value_4.append('-')
		portfolio_asset_4.append('-')
	try:
		portfolio_equity_5.append(temp_table[5][0])
		portfolio_sector_5.append(temp_table[5][1])
		portfolio_value_5.append(temp_table[5][2])
		portfolio_asset_5.append(temp_table[5][3])
	except:
		portfolio_equity_5.append('-')
		portfolio_sector_5.append('-')
		portfolio_value_5.append('-')
		portfolio_asset_5.append('-')
	try:
		portfolio_equity_6.append(temp_table[6][0])
		portfolio_sector_6.append(temp_table[6][1])
		portfolio_value_6.append(temp_table[6][2])
		portfolio_asset_6.append(temp_table[6][3])
	except:
		portfolio_equity_6.append('-')
		portfolio_sector_6.append('-')
		portfolio_value_6.append('-')
		portfolio_asset_6.append('-')
	try:
		portfolio_equity_7.append(temp_table[7][0])
		portfolio_sector_7.append(temp_table[7][1])
		portfolio_value_7.append(temp_table[7][2])
		portfolio_asset_7.append(temp_table[7][3])
	except:
		portfolio_equity_7.append('-')
		portfolio_sector_7.append('-')
		portfolio_value_7.append('-')
		portfolio_asset_7.append('-')
	try:
		portfolio_equity_8.append(temp_table[8][0])
		portfolio_sector_8.append(temp_table[8][1])
		portfolio_value_8.append(temp_table[8][2])
		portfolio_asset_8.append(temp_table[8][3])
	except:
		portfolio_equity_8.append('-')
		portfolio_sector_8.append('-')
		portfolio_value_8.append('-')
		portfolio_asset_8.append('-')
	try:
		portfolio_equity_9.append(temp_table[9][0])
		portfolio_sector_9.append(temp_table[9][1])
		portfolio_value_9.append(temp_table[9][2])
		portfolio_asset_9.append(temp_table[9][3])
	except:
		portfolio_equity_9.append('-')
		portfolio_sector_9.append('-')
		portfolio_value_9.append('-')
		portfolio_asset_9.append('-')
	try:
		portfolio_equity_10.append(temp_table[10][0])
		portfolio_sector_10.append(temp_table[10][1])
		portfolio_value_10.append(temp_table[10][2])
		portfolio_asset_10.append(temp_table[10][3])
	except:
		portfolio_equity_10.append('-')
		portfolio_sector_10.append('-')
		portfolio_value_10.append('-')
		portfolio_asset_10.append('-')
	
	data_table = table_data_1[3].find_all('div', attrs={'class':'FL'})
	#print data_table[1]
	table_body = data_table[1].find_all('table', attrs={'class':'tbl_n2'})
	#print table_body[0]

	rows = table_body[0].find_all('tr')
	temp_table = []
	for row in rows:
		cols = row.find_all('td')
		col_row = []
		for col in cols:
			col_row.append(col.text)
		temp_table.append(col_row)
	#print temp_table
	try:
		portfolio_asset_allocation_eqity.append(temp_table[1][1])
		portfolio_asset_allocation_others.append(temp_table[2][1])
		portfolio_asset_allocation_debt.append(temp_table[3][1])
		portfolio_asset_allocation_mutual_funds.append(temp_table[4][1])
		portfolio_asset_allocation_money_market.append(temp_table[5][1])
		portfolio_asset_allocation_cash_call.append(temp_table[6][1])
	except:
		portfolio_asset_allocation_eqity.append('-')
		portfolio_asset_allocation_others.append('-')
		portfolio_asset_allocation_debt.append('-')
		portfolio_asset_allocation_mutual_funds.append('-')
		portfolio_asset_allocation_money_market.append('-')
		portfolio_asset_allocation_cash_call.append('-')

	rows = table_body[1].find_all('tr')
	temp_table = []
	for row in rows:
		cols = row.find_all('td')
		col_row = []
		for col in cols:
			col_row.append(col.text)
		temp_table.append(col_row)
	#print temp_table
	try:
		portfolio_concentration_holding_top5.append(temp_table[2][1])
	except:
		portfolio_concentration_holding_top5.append('-')
	try:
		portfolio_concentration_holding_top10.append(temp_table[3][1])
	except:
		portfolio_concentration_holding_top10.append('-')
	try:
		portfolio_concentration_sector_top3.append(temp_table[5][1])
	except:
		portfolio_concentration_sector_top3.append('-')

	rows = table_body[2].find_all('tr')
	temp_table = []
	for row in rows:
		cols = row.find_all('td')
		col_row = []
		for col in cols:
			col_row.append(col.text)
		temp_table.append(col_row)
	#print temp_table
	try:
		portfolio_sector_percentage_right_bottom_1.append(temp_table[2][1])
		portfolio_sector_high_right_bottom_1.append(temp_table[2][2])
		portfolio_sector_low_right_bottom_1.append(temp_table[2][3])
		portfolio_sector_right_bottom_1.append(temp_table[2][0])
	except:
		portfolio_sector_right_bottom_1.append('-')
		portfolio_sector_percentage_right_bottom_1.append('-')
		portfolio_sector_high_right_bottom_1.append('-')
		portfolio_sector_low_right_bottom_1.append('-')
	try:
		portfolio_sector_right_bottom_2.append(temp_table[3][0])
		portfolio_sector_percentage_right_bottom_2.append(temp_table[3][1])
		portfolio_sector_high_right_bottom_2.append(temp_table[3][2])
		portfolio_sector_low_right_bottom_2.append(temp_table[3][3])
	except:
		portfolio_sector_right_bottom_2.append('-')
		portfolio_sector_percentage_right_bottom_2.append('-')
		portfolio_sector_high_right_bottom_2.append('-')
		portfolio_sector_low_right_bottom_2.append('-')
	try:
		portfolio_sector_right_bottom_3.append(temp_table[4][0])
		portfolio_sector_percentage_right_bottom_3.append(temp_table[4][1])
		portfolio_sector_high_right_bottom_3.append(temp_table[4][2])
		portfolio_sector_low_right_bottom_3.append(temp_table[4][3])
	except:
		portfolio_sector_right_bottom_3.append('-')
		portfolio_sector_percentage_right_bottom_3.append('-')
		portfolio_sector_high_right_bottom_3.append('-')
		portfolio_sector_low_right_bottom_3.append('-')
	try:
		portfolio_sector_right_bottom_4.append(temp_table[5][0])
		portfolio_sector_percentage_right_bottom_4.append(temp_table[5][1])
		portfolio_sector_high_right_bottom_4.append(temp_table[5][2])
		portfolio_sector_low_right_bottom_4.append(temp_table[5][3])
	except:
		portfolio_sector_right_bottom_4.append('-')
		portfolio_sector_percentage_right_bottom_4.append('-')
		portfolio_sector_high_right_bottom_4.append('-')
		portfolio_sector_low_right_bottom_4.append('-')
	try:
		portfolio_sector_right_bottom_5.append(temp_table[6][0])
		portfolio_sector_percentage_right_bottom_5.append(temp_table[6][1])
		portfolio_sector_high_right_bottom_5.append(temp_table[6][2])
		portfolio_sector_low_right_bottom_5.append(temp_table[6][3])
	except:
		portfolio_sector_right_bottom_5.append('-')
		portfolio_sector_percentage_right_bottom_5.append('-')
		portfolio_sector_high_right_bottom_5.append('-')
		portfolio_sector_low_right_bottom_5.append('-')
	try:
		portfolio_sector_right_bottom_6.append(temp_table[7][0])
		portfolio_sector_percentage_right_bottom_6.append(temp_table[7][1])
		portfolio_sector_high_right_bottom_6.append(temp_table[7][2])
		portfolio_sector_low_right_bottom_6.append(temp_table[7][3])
	except:
		portfolio_sector_right_bottom_6.append('-')
		portfolio_sector_percentage_right_bottom_6.append('-')
		portfolio_sector_high_right_bottom_6.append('-')
		portfolio_sector_low_right_bottom_6.append('-')

	url1 = url.replace('snapshot.php','scheme_assets.php')
	print url1
	br = mechanize.Browser()
	br.open(url1)
	br.select_form(nr=1)
	items1 = br.form.find_control("from_mth").get_items()
	items2 = br.form.find_control("from_year").get_items()
	items3 = br.form.find_control("to_mth").get_items()
	items4 = br.form.find_control("to_year").get_items()

	br.form['from_mth'] = [items1[1].name]
	br.form['from_year'] = [items2[8].name]
	br.form['to_mth'] = [items3[1].name]
	br.form['to_year'] = [items4[13].name]
	req = br.submit()
	data = br.response().read()
	soup = BeautifulSoup(data)
	x1 = soup.find('table')
	rows = x1.find_all('tr')
	temp_table = []
	for row in rows:
		cols = row.find_all('td')
		col_row = []
		for col in cols:
			col_row.append(col.text)
		temp_table.append(col_row)
	#print temp_table #start-64;end84
	print len(temp_table)
	try:
		asset_size_1date.append(temp_table[20][0])
		asset_size_1value.append(temp_table[20][1])
	except:
		asset_size_1date.append('-')
		asset_size_1value.append('-')
	try:
		asset_size_2date.append(temp_table[19][0])
		asset_size_2value.append(temp_table[19][1])
	except:
		asset_size_2date.append('-')
		asset_size_2value.append('-')
	try:
		asset_size_3date.append(temp_table[18][0])
		asset_size_3value.append(temp_table[18][1])
	except:
		asset_size_3date.append('-')
		asset_size_3value.append('-')
	try:
		asset_size_4date.append(temp_table[17][0])
		asset_size_4value.append(temp_table[17][1])
	except:
		asset_size_4date.append('-')
		asset_size_4value.append('-')
	try:
		asset_size_5date.append(temp_table[16][0])
		asset_size_5value.append(temp_table[16][1])
	except:
		asset_size_5date.append('-')
		asset_size_5value.append('-')
	try:
		asset_size_6date.append(temp_table[15][0])
		asset_size_6value.append(temp_table[15][1])
	except:
		asset_size_6date.append('-')
		asset_size_6value.append('-')
	try:
		asset_size_7date.append(temp_table[14][0])
		asset_size_7value.append(temp_table[14][1])
	except:
		asset_size_7date.append('-')
		asset_size_7value.append('-')
	try:
		asset_size_8date.append(temp_table[13][0])
		asset_size_8value.append(temp_table[13][1])
	except:
		asset_size_8date.append('-')
		asset_size_8value.append('-')
	try:
		asset_size_9date.append(temp_table[12][0])
		asset_size_9value.append(temp_table[12][1])
	except:
		asset_size_9date.append('-')
		asset_size_9value.append('-')
	try:
		asset_size_10date.append(temp_table[11][0])
		asset_size_10value.append(temp_table[11][1])
	except:
		asset_size_10date.append('-')
		asset_size_10value.append('-')
	try:
		asset_size_11date.append(temp_table[10][0])
		asset_size_11value.append(temp_table[10][1])
	except:
		asset_size_11date.append('-')
		asset_size_11value.append('-')
	try:
		asset_size_12date.append(temp_table[9][0])
		asset_size_12value.append(temp_table[9][1])
	except:
		asset_size_12date.append('-')
		asset_size_12value.append('-')
	try:
		asset_size_13date.append(temp_table[8][0])
		asset_size_13value.append(temp_table[8][1])
	except:
		asset_size_13date.append('-')
		asset_size_13value.append('-')
	try:
		asset_size_14date.append(temp_table[7][0])
		asset_size_14value.append(temp_table[7][1])
	except:
		asset_size_14date.append('-')
		asset_size_14value.append('-')
	try:
		asset_size_15date.append(temp_table[6][0])
		asset_size_15value.append(temp_table[6][1])
	except:
		asset_size_15date.append('-')
		asset_size_15value.append('-')
	try:
		asset_size_16date.append(temp_table[5][0])
		asset_size_16value.append(temp_table[5][1])
	except:
		asset_size_16date.append('-')
		asset_size_16value.append('-')
	try:
		asset_size_17date.append(temp_table[4][0])
		asset_size_17value.append(temp_table[4][1])
	except:
		asset_size_17date.append('-')
		asset_size_17value.append('-')
	try:
		asset_size_18date.append(temp_table[3][0])
		asset_size_18value.append(temp_table[3][1])
	except:
		asset_size_18date.append('-')
		asset_size_18value.append('-')
	try:
		asset_size_19date.append(temp_table[2][0])
		asset_size_19value.append(temp_table[2][1])
	except:
		asset_size_19date.append('-')
		asset_size_19value.append('-')
	try:
		asset_size_20date.append(temp_table[1][0])
		asset_size_20value.append(temp_table[1][1])
	except:
		asset_size_20date.append('-')
		asset_size_20value.append('-')

df = pd.DataFrame(plan,columns=['Plan_name'])
df['fund_family'] = fund_family
df['fund_class'] = fund_class
df['fund_type'] = fund_type
df['investment_plan'] = Investment_plan
df['asset_size'] = Asset_size
df['minimum_investment'] = Min_Investment
df['last_divident'] = Last_divident
df['bonus'] = Bonus
df['entry_load'] = Entry_Load
df['exit_load'] = Exit_Load
df['benchmark'] = Benchmark
df['launch_date'] = Launch_date
df['performance_returns_1_mth'] = performance_returns_1_mth
df['performance_r16urns_3_mth'] = performance_returns_3_mth
df['performance_returns_6_mth'] = performance_returns_6_mth
df['performance_returns_1_year'] = performance_returns_1_year
df['performance_returns_2_year'] = performance_returns_2_year
df['performance_returns_3_year'] = performance_returns_3_year
df['performance_returns_5_year'] = performance_returns_5_year
df['performance_r15k_1_mth'] = performance_rank_1_mth
df['performance_rank_3_mth'] = performance_rank_3_mth
df['performance_rank_6_mth'] = performance_rank_6_mth
df['performance_rank_1_year'] = performance_rank_1_year
df['performance_rank_2_year'] = performance_rank_2_year
df['performance_rank_3_year'] = performance_rank_3_year
df['performance_r14k_5_year'] = performance_rank_5_year
df['performance_absolute_returns_2017_Qtr1'] = performance_absolute_returns_2017_Qtr1
df['performance_absolute_returns_2016_Qtr1'] = performance_absolute_returns_2016_Qtr1
df['performance_absolute_returns_2015_Qtr1'] = performance_absolute_returns_2015_Qtr1
df['performance_absolute_returns_2014_Qtr1'] = performance_absolute_returns_2014_Qtr1
df['performance_absolute_returns_2013_Qtr1'] = performance_absolute_returns_2013_Qtr1
df['performance_a13olute_returns_2017_Qtr2'] = performance_absolute_returns_2017_Qtr2
df['performance_absolute_returns_2016_Qtr2'] = performance_absolute_returns_2016_Qtr2
df['performance_absolute_returns_2015_Qtr2'] = performance_absolute_returns_2015_Qtr2
df['performance_absolute_returns_2014_Qtr2'] = performance_absolute_returns_2014_Qtr2
df['performance_absolute_returns_2013_Qtr2'] = performance_absolute_returns_2013_Qtr2
df['performance_absolute_returns_2017_Qtr3'] = performance_absolute_returns_2017_Qtr3
df['performance_a12olute_returns_2016_Qtr3'] = performance_absolute_returns_2016_Qtr3
df['performance_absolute_returns_2015_Qtr3'] = performance_absolute_returns_2015_Qtr3
df['performance_absolute_returns_2014_Qtr3'] = performance_absolute_returns_2014_Qtr3
df['performance_absolute_returns_2013_Qtr3'] = performance_absolute_returns_2013_Qtr3
df['performance_absolute_returns_2017_Qtr4'] = performance_absolute_returns_2017_Qtr4
df['performance_absolute_returns_2016_Qtr4'] = performance_absolute_returns_2016_Qtr4
df['performance_ab11lute_returns_2015_Qtr4'] = performance_absolute_returns_2015_Qtr4
df['performance_absolute_returns_2014_Qtr4'] = performance_absolute_returns_2014_Qtr4
df['performance_absolute_returns_2013_Qtr4'] = performance_absolute_returns_2013_Qtr4
df['performance_absolute_returns_2017_annual'] = performance_absolute_returns_2017_annual
df['performance_absolute_returns_2016_annual'] = performance_absolute_returns_2016_annual
df['performance_absolute_returns_2015_annual'] = performance_absolute_returns_2015_annual
df['performance_ab10lute_returns_2014_annual'] = performance_absolute_returns_2014_annual
df['performance_absolute_returns_2013_annual'] = performance_absolute_returns_2013_annual
df['nav_52_week_high'] = nav_52_week_high
#df['nav_52_week_high_date'] = nav_52_week_high_date
df['nav_52_week_low'] = nav_52_week_low
#df['nav_52_week_low_date'] = nav_52_week_low_date
df['portfolio_equity_1'] = portfolio_equity_1
df['portfolio_equity_2'] = portfolio_equity_2
df['portfolio_equity_3'] = portfolio_equity_3
df['portfolio_equity_4'] = portfolio_equity_4
df['portfolio_equity_5'] = portfolio_equity_5
df['portfolio_equity_6'] = portfolio_equity_6
df['portfolio_equity_7'] = portfolio_equity_7
df['portfolio_equity_8'] = portfolio_equity_8
df['portfolio_equity_9'] = portfolio_equity_9
df['portfolio_equity_10'] = portfolio_equity_10
df['portfolio_sector_1'] = portfolio_sector_1
df['portfolio_sector_2'] = portfolio_sector_2
df['portfolio_sector_3'] = portfolio_sector_3
df['portfolio_sector_4'] = portfolio_sector_4
df['portfolio_sector_5'] = portfolio_sector_5
df['portfolio_sector_6'] = portfolio_sector_6
df['portfolio_sector_7'] = portfolio_sector_7
df['portfolio_sector_8'] = portfolio_sector_8
df['portfolio_sector_9'] = portfolio_sector_9
df['portfolio_sector_10'] = portfolio_sector_10
df['portfolio_value_1'] = portfolio_value_1
df['portfolio_value_2'] = portfolio_value_2
df['portfolio_value_3'] = portfolio_value_3
df['portfolio_value_4'] = portfolio_value_4
df['portfolio_value_5'] = portfolio_value_5
df['portfolio_value_6'] = portfolio_value_6
df['portfolio_value_7'] = portfolio_value_7
df['portfolio_value_8'] = portfolio_value_8
df['portfolio_value_9'] = portfolio_value_9
df['portfolio_value_10'] = portfolio_value_10
df['portfolio_asset_1'] = portfolio_asset_1
df['portfolio_asset_2'] = portfolio_asset_2
df['portfolio_asset_3'] = portfolio_asset_3
df['portfolio_asset_4'] = portfolio_asset_4
df['portfolio_asset_5'] = portfolio_asset_5
df['portfolio_asset_6'] = portfolio_asset_6
df['portfolio_asset_7'] = portfolio_asset_7
df['portfolio_asset_8'] = portfolio_asset_8
df['portfolio_asset_9'] = portfolio_asset_9
df['portfolio_asset_10'] = portfolio_asset_10

df['portfolio_asset_allocation_eqity'] = portfolio_asset_allocation_eqity
df['portfolio_asset_allocation_others'] = portfolio_asset_allocation_others
df['portfolio_asset_allocation_debt'] = portfolio_asset_allocation_debt
df['portfolio_asset_allocation_mutual_funds'] = portfolio_asset_allocation_mutual_funds
df['portfolio_asset_allocation_money_market'] = portfolio_asset_allocation_money_market
df['portfolio_asset_allocation_cash_call'] = portfolio_asset_allocation_cash_call

df['portfolio_conc1tration_holding_top5'] = portfolio_concentration_holding_top5
df['portfolio_concentration_holding_top10'] = portfolio_concentration_holding_top10
df['portfolio_concentration_sector_top3'] = portfolio_concentration_sector_top3

df['portfolio_sector_right_bottom_1'] = portfolio_sector_right_bottom_1
df['portfolio_sector_right_bottom_2'] = portfolio_sector_right_bottom_2
df['portfolio_sector_right_bottom_3'] = portfolio_sector_right_bottom_3
df['portfolio_sector_right_bottom_4'] = portfolio_sector_right_bottom_4
df['portfolio_sector_right_bottom_5'] = portfolio_sector_right_bottom_5
df['portfolio_sector_right_bottom_6'] = portfolio_sector_right_bottom_6

df['portfolio_sector_percentage_right_bottom_1'] = portfolio_sector_percentage_right_bottom_1
df['portfolio_sector_percentage_right_bottom_2'] = portfolio_sector_percentage_right_bottom_2
df['portfolio_sector_percentage_right_bottom_3'] = portfolio_sector_percentage_right_bottom_3
df['portfolio_sector_percentage_right_bottom_4'] = portfolio_sector_percentage_right_bottom_4
df['portfolio_sector_percentage_right_bottom_5'] = portfolio_sector_percentage_right_bottom_5
df['portfolio_sector_percentage_right_bottom_6'] = portfolio_sector_percentage_right_bottom_6

df['portfolio_sector_high_right_bottom_1'] = portfolio_sector_high_right_bottom_1
df['portfolio_sector_high_right_bottom_2'] = portfolio_sector_high_right_bottom_2
df['portfolio_sector_high_right_bottom_3'] = portfolio_sector_high_right_bottom_3
df['portfolio_sector_high_right_bottom_4'] = portfolio_sector_high_right_bottom_4
df['portfolio_sector_high_right_bottom_5'] = portfolio_sector_high_right_bottom_5
df['portfolio_sector_high_right_bottom_6'] = portfolio_sector_high_right_bottom_6

df['portfolio_sector_low_right_bottom_1'] = portfolio_sector_low_right_bottom_1
df['portfolio_sector_low_right_bottom_2'] = portfolio_sector_low_right_bottom_2
df['portfolio_sector_low_right_bottom_3'] = portfolio_sector_low_right_bottom_3
df['portfolio_sector_low_right_bottom_4'] = portfolio_sector_low_right_bottom_4
df['portfolio_sector_low_right_bottom_5'] = portfolio_sector_low_right_bottom_5
df['portfolio_sector_low_right_bottom_6'] = portfolio_sector_low_right_bottom_6

df['asset_size_1date'] = asset_size_1date
df['asset_size_1value'] = asset_size_1value
df['asset_size_2date'] = asset_size_2date
df['asset_size_2value'] = asset_size_2value
df['asset_size_3date'] = asset_size_3date
df['asset_size_3value'] = asset_size_3value
df['asset_size_4date'] = asset_size_4date
df['asset_size_4value'] = asset_size_4value
df['asset_size_5date'] = asset_size_5date
df['asset_size_5value'] = asset_size_5value
df['asset_size_6date'] = asset_size_6date
df['asset_size_6value'] = asset_size_6value
df['asset_size_7date'] = asset_size_7date
df['asset_size_7value'] = asset_size_7value
df['asset_size_8date'] = asset_size_8date
df['asset_size_8value'] = asset_size_8value
df['asset_size_9date'] = asset_size_9date
df['asset_size_9value'] = asset_size_9value
df['asset_size_10date'] = asset_size_10date
df['asset_size_10value'] = asset_size_10value
df['asset_size_11date'] = asset_size_11date
df['asset_size_11value'] = asset_size_11value
df['asset_size_12date'] = asset_size_12date
df['asset_size_12value'] = asset_size_12value
df['asset_size_13date'] = asset_size_13date
df['asset_size_13value'] = asset_size_13value
df['asset_size_14date'] = asset_size_14date
df['asset_size_14value'] = asset_size_14value
df['asset_size_15date'] = asset_size_15date
df['asset_size_15value'] = asset_size_15value
df['asset_size_16date'] = asset_size_16date
df['asset_size_16value'] = asset_size_16value
df['asset_size_17date'] = asset_size_17date
df['asset_size_17value'] = asset_size_17value
df['asset_size_18date'] = asset_size_18date
df['asset_size_18value'] = asset_size_18value
df['asset_size_19date'] = asset_size_19date
df['asset_size_19value'] = asset_size_19value
df['asset_size_20date'] = asset_size_20date
df['asset_size_20value'] = asset_size_20value
df.to_csv('data8_2.csv', sep=',')