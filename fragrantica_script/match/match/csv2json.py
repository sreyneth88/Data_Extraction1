import csv
import json

csvfile = open('new.csv', 'r')
jsonfile = open('new.json', 'w+')

fieldnames = ("itemname")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')
