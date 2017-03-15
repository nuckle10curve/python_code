import os 
import sqlite3


conn = sqlite3.connect('output/out_3_B.db')
stmnt = 'insert into target_actual (product,period,actual,target) \
values ('

def insert_row(line):
	
	prod = "'"+line[0]+"',"
	period = "'"+line[1]+"',"
	actual = line[2]+','
	target = line[3]+')'

	insert_stmnt = stmnt +prod + period + actual + target
	#print (insert_stmnt)
	conn.execute (insert_stmnt)


def read_file():
	x = 0
	with open('input/in_3_B.csv','r') as f:
		for line in f:
			x = x+1

			line = line.replace('\n','')
			
			if x>1:
				line_split = line.split(',')
				insert_row(line_split)
	return

if __name__ == "__main__":

	read_file()
	conn.commit()
	conn.close()
	

