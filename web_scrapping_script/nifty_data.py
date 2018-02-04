from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import csv

from_dates = ["01-01-2013","01-04-2013","01-07-2013", "01-10-2013", "01-01-2014","01-04-2014","01-07-2014", "01-10-2014", "01-01-2015","01-04-2015","01-07-2015", "01-10-2015", "01-01-2016","01-04-2016","01-07-2016", "01-10-2016", "01-01-2017","01-04-2017","01-07-2017", "01-10-2017", "01-01-2018"]
to_dates = ["01-04-2013","01-07-2013", "01-10-2013", "01-01-2014","01-04-2014","01-07-2014", "01-10-2014", "01-01-2015","01-04-2015","01-07-2015", "01-10-2015", "01-01-2016","01-04-2016","01-07-2016", "01-10-2016", "01-01-2017","01-04-2017","01-07-2017", "01-10-2017", "01-01-2018", "23-01-2018"]

driver = webdriver.Firefox()
driver.get('https://www.nseindia.com/products/content/equities/indices/historical_index_data.htm')
index = Select(driver.find_element_by_id("indexType"))
fromdate = driver.find_element_by_id("fromDate")
todate = driver.find_element_by_id("toDate")
options = index.options
for option in options[1:]:
	# option = options[1]
	print option.text
	temp_table = []
	index.select_by_visible_text(option.text)
	for i in range(21):
		fromdate.clear()
		todate.clear()
		fromdate.send_keys(from_dates[i])
		todate.send_keys(to_dates[i])
		driver.find_element_by_id("get").click()
		temp = driver.find_element_by_class_name("tabular-data-historic")
		time.sleep(1)
		soup = BeautifulSoup(temp.get_attribute('innerHTML'))
		table = soup.find("table")
		# print table
		try:
			rows = table.find_all('tr')
		except:
			time.sleep(5)
			soup = BeautifulSoup(temp.get_attribute('innerHTML'))
			table = soup.find("table")
			rows = table.find_all('tr')
		for row in rows:
			cols = row.find_all('td')
			col_row = []
			for col in cols:
				col_row.append(col.text)
			if len(col_row)>2:
				temp_table.append(col_row)
	print temp_table
	filename_csv = option.text + ".csv"
	with open(filename_csv,"w+") as my_csv:
		csvWriter = csv.writer(my_csv,delimiter=',')
		csvWriter.writerows(temp_table)
		# time.sleep(5)
		# driver.close()

# index = selenium.find_element_by_id("indexType")
# fromdate = selenium.find_element_by_id("fromDate")
# todate = selenium.find_element_by_id("toDate")
#password = selenium.find_element_by_id("password")

#username.send_keys("YourUsername")
#password.send_keys("Pa55worD")

#selenium.find_element_by_name("submit").click()