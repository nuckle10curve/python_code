from openpyxl import load_workbook
from datetime import datetime
import sys,os



os.system('export PYTHONIOENCODING=UTF-8')
print (sys.getdefaultencoding())

wb2 = load_workbook('input/ganesh.xlsx')


sheet = wb2.get_sheet_by_name('Sheet1')

for xxx in range (1,14):
	if xxx == 1:
		heading_A = sheet['A'+str(xxx)].value
		heading_B = sheet['B'+str(xxx)].value
		heading_C = sheet['C'+str(xxx)].value
		heading_D = sheet['D'+str(xxx)].value

		heading = heading_A+','+ heading_B +',' +heading_C +','+ heading_D +'\n'
		table = heading

	if xxx>1:
		
		product = sheet['A'+str(xxx)].value

		date_str = sheet['B'+str(xxx)].value
		actual = sheet['C'+str(xxx)].value
		target =sheet['D'+str(xxx)].value
		dt_formatted = str(date_str.month)+'/'+str(date_str.day)+'/'+str(date_str.year)
		
		row = product +','+ dt_formatted + ',' + str(actual) + ',' +str(target) +'\n'
		
		table += row

	f = open ('output/rpt_3_F.csv','w')
	f.write(table)
	f.close()
	