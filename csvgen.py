#!/usr/bin/python3
import datetime
import csv

personName = input ("Enter your full name: ")
dt = datetime.datetime.now()
newrow = [str(dt), personName]
try:
    f = open ("book.csv", "a", newline='')
    cw = csv.writer(f)
    cw.writerow(newrow)
    f.close()
except:
    print ("Error while saving.")
print ("Success.")