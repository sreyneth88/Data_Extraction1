import csv
import io
import re
import sys
reload(sys)
sys.setdefaultencoding("UTF8")

f1 = file('LInk&pro.csv', 'r')
f2 = file('charactor.csv', 'r')


c1 = csv.reader(f1)
c2 = csv.reader(f2)
fs = io.open('match_barcode.csv', 'a+', encoding='utf8')

masterlist = list(c2)
count = 0
# f2list = list(d2)
# count=0
# for byrow in d1:
#     r1 = byrow[0]
#     all_data = [i[0] for i in byrow if r1 in i[1]]
#     if all_data:
#         barcode = ",".join(all_data)
#         data = ",".join(r1)
#         result = data + ","+barcode+"\n"
#         result = result.decode()
#         fs.write(result)
#     else:
#         print "Not Match"
# print "Finished"

for hosts_row in c1:
    strtext=hosts_row[0]
    strtext=re.sub(r'\_',' ',strtext)
    tmp=[l[0] for l in masterlist if strtext in l[1]]
    if tmp:
        barcode=",".join(tmp)
        print barcode
        data=",".join(hosts_row)
        result=data+","+barcode+"\n"
        result=result.decode()
        fs.write(result)
    else:
        print "Not Match"
print "Finish Matching"