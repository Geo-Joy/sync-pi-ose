#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This script is used to monitor ON&OFF of RPI
# db = onoff.db
# db columns are
# id = unique identifier.
# ONtime = RPI on time logger - create each time rpi starts.
# OFFtime = RPI off time logger - update datatimestamp every 60 secs.
# CPU_temp  = log max temp during each db update. 
# CPU_usage 
# DISK_free 
# RAM_free 


################
### run main ###
################

import threading
import os 
import uuid
import logging
import sqlite3
#import datetime
#import time
from time import localtime, strftime

global ts
#ts = time.time()

DATABASE_LOCATION = "/home/pi/.sync/timekeeper.db"

	
# Return CPU temperature as a character string                                      
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

# Return RAM information (unit=kb) in a list                                        
# Index 0: total RAM                                                                
# Index 1: used RAM                                                                 
# Index 2: free RAM                                                                 
def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i==2:
            return(line.split()[1:4])

# Return % of CPU used by user as a character string                                
def getCPUuse():
    return(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip(\
))

# Return information about disk space as a list (unit included)                     
# Index 0: total disk space                                                         
# Index 1: used disk space                                                          
# Index 2: remaining disk space                                                     
# Index 3: percentage of disk used                                                  
def getDiskSpace():
    p = os.popen("df -h /")
    i = 0
    while 1:
        i = i +1
        line = p.readline()
        if i==2:
            return(line.split()[1:5])

def getAll():
	
	getCPUtemperature()
	getRAMinfo()
	getCPUuse()
	getDiskSpace()
	
	# CPU informatiom
	global CPU_temp 
	CPU_temp = getCPUtemperature()
	global CPU_usage 
	CPU_usage = getCPUuse()
	#print(CPU_usage)
	# RAM information
	# Output is in kb, here I convert it in Mb for readability
	RAM_stats = getRAMinfo()
	#RAM_total = round(int(RAM_stats[0]) / 1000,1)
	#RAM_used = round(int(RAM_stats[1]) / 1000,1)
	global RAM_free
	RAM_free	= round(int(RAM_stats[2]) / 1000,1)

	# Disk information
	DISK_stats = getDiskSpace()
	#DISK_total = DISK_stats[0]
	global DISK_free
	DISK_free = DISK_stats[1]
	#DISK_perc = DISK_stats[3]


def getTime():	
	return(strftime("%Y-%m-%d %H:%M:%S", localtime()))	

def pushToDB(ID, ONN, OFF, TEMP, USAGE, DISK, RAM):
	conn=sqlite3.connect(DATABASE_LOCATION, timeout=5)
	curs=conn.cursor()
	try:
		print(USAGE)
		curs.execute("INSERT or REPLACE into onoff values (?, ?, ?, ?, ?, ?, ?)",(ID, ONN, OFF, TEMP, USAGE, DISK, RAM))
		conn.commit()
	except sqlite3.OperationalError, msg:
		print(msg)
	finally: 
		# commit the changes
		curs.close()
		conn.close()

def main(mUUID, ONtime):
	getAll()
	OFFtime = getTime()
	pushToDB(mUUID, ONtime, OFFtime, CPU_temp, CPU_usage, DISK_free, RAM_free)
	threading.Timer(30, main(mUUID, ONtime)).start()


# check for main funtion and start or log exception
if __name__ == "__main__":
    try:
		#generate session id
		global mUUID
		mUD = str(uuid.uuid4())
		mUUID = mUD.replace('-', '')
		#call main only once from here
		print(mUUID)
		global ONtime
		ONtime = getTime()
        	main(mUUID, ONtime)
    except:
        logging.exception("monitor > onoff.py crashed")
        raise
