import sys
import csv

import psycopg2

def insert(fname):
	dbconn=psycopg2.connect("dbname=superheroes")
	curs=dbconn.cursor()
	
	fil=open(fname)
	val=csv.reader(fil)
	for name,gender in val:
		curs.execute("insert into heroes(name,gender) values(%s,%s)",(name,gender))
		
	dbconn.commit()

def main():
	fname=sys.argv[1]
	insert(fname)
main()
