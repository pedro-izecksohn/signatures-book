import datetime
import csv

personName = input ("Enter your full name: ")
dt = datetime.datetime.now()
#print (dt)
allrows = []
try:
  f = open ("book.csv", "r", newline='')
  cr = csv.reader (f)
  for row in cr:
      allrows.append(row)
  f.close()
except:
  print ("I could not read book.csv .\nI'll create a new book.csv .")
newrow = [str(dt), personName]
allrows.append(newrow)
#print (allrows)
try:
    f = open ("book.csv", "w", newline='')
    cw = csv.writer(f)
    for row in allrows:
        cw.writerow(row)
    f.close()
except:
    print ("Error while saving.")
print ("Success.")