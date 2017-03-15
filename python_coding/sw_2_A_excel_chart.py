import xlsxwriter
import sys

import sys
output_file_name = 'rpt_2_A_chart_column.xlsx'

if len(sys.argv) == 2:
	output_file_name =sys.argv[1]






workbook = xlsxwriter.Workbook('output/'+output_file_name )
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': 1})

# Add the worksheet data that the charts will refer to.
headings = [ 'Period', 'Actual','Target']
data = [
    [2, 3, 4, 5, 6, 7],
    [10, 40, 50, 20, 10, 50],
    [30, 60, 70, 50, 40, 30],
]

data =  [
['1/1/16','2/1/16','3/1/16','4/1/16','5/1/16','6/1/16','7/1/16','8/1/16','9/1/16','10/1/16','11/1/16','12/1/16'],
[30,400,50,200,300,150,80,200,150,250,450,550],
[100,200,250,300,200,100,100,200,200,300,400,500],

]

worksheet.write_row('A1', headings, bold)
worksheet.write_column('A2', data[0])
worksheet.write_column('B2', data[1])
worksheet.write_column('C2', data[2])

#######################################################################
#
# Create a new column chart.
#
chart1 = workbook.add_chart({'type': 'column'})

# Configure the first series.
chart1.add_series({
    'name':       '=Sheet1!$B$1',
    'categories': '=Sheet1!$A$2:$A$13',
    'values':     '=Sheet1!$B$2:$B$13',
})

# Configure a second series. Note use of alternative syntax to define ranges.



chart1.add_series({
    'name':       ['Sheet1', 0, 2],
    'categories': ['Sheet1', 1, 0, 12, 0],
    'values':     ['Sheet1', 1, 2, 12, 2],
})

# Add a chart title and some axis labels.
chart1.set_title ({'name': 'Monthly comparison target vs actual'})
chart1.set_x_axis({'name': 'Months'})
chart1.set_y_axis({'name': 'Qty of Products '})

# Set an Excel chart style.
chart1.set_style(11)

# Insert the chart into the worksheet (with an offset).
worksheet.insert_chart('D20', chart1, {'x_offset': 25, 'y_offset': 10})



headings = [ 'Period', 'Actual','Actual-Target']

data =  [
['1/1/16','2/1/16','3/1/16','4/1/16','5/1/16','6/1/16','7/1/16','8/1/16','9/1/16','10/1/16','11/1/16','12/1/16'],
[30,400,50,200,300,150,80,200,150,250,450,550],
[-70,200,-200,-100,100,50,-20,0,-50,-50,50,50]

]

worksheet.write_row('F1', headings, bold)
worksheet.write_column('F2', data[0])
worksheet.write_column('G2', data[1])
worksheet.write_column('H2', data[2])

chart1 = workbook.add_chart({'type': 'column'})

chart1.add_series({
    'name':       '=Sheet1!$H$1',
    'categories': '=Sheet1!$F$2:$F$13',
    'values':     '=Sheet1!$H$2:$H$13',
})

chart1.set_title ({'name': 'Monthly comparison actual minus target'})
chart1.set_x_axis({'name': 'Months'})
chart1.set_y_axis({'name': 'Difference '})

# Set an Excel chart style.
chart1.set_style(13)

# Insert the chart into the worksheet (with an offset).
worksheet.insert_chart('D35', chart1, {'x_offset': 25, 'y_offset': 10})



workbook.close()