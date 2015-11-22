#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import json

def getrating(d):
	if "traffic" in d:
		return 2
	if "possession" in d:
		return 2
	if "theft" in d:
		if "petty" in d:
			return 3
		else:
			return 5
	if "rape" in d or "abuse" in d:
		return 8
	if "robbery" in d:
		return 6
	if "auto" in d or "moto" in d:
		return 4
	if "battery" in d or "assault" in d:
		return 7
	

def getdata():
	try:
		con = mdb.connect('localhost', 'root', 'root', 'crime');

		cur = con.cursor()
		cur.execute("select x, y from crime;")
		crime = cur.fetchall()
		cur.execute("select count(*) from crime;")
		count = len(crime)

	except mdb.Error, e:
	  
		print "Error %d: %s" % (e.args[0],e.args[1])
		sys.exit(1)
		
	finally:    
		data = []
		for x in enumerate(crime):
			temp = {}
			temp['lat'] = x[1][0]
			temp['lng'] = x[1][1]
			data.append(temp)
		return  json.dumps({'max' : count , 'data': data})

		if con:    
			con.close()
