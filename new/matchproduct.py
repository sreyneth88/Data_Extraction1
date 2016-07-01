import csv
import io
import re
import sys
reload(sys)
sys.setdefaultencoding("UTF8")

f1 = file('link_product.csv', 'r')
f2 = file('safir_product_collected.csv', 'r')


c1 = csv.reader(f1)
c2 = csv.reader(f2)
fs = io.open('match_link.csv', 'a+', encoding='utf8')

masterlist = list(c2)
count=0
for hosts_row in c1:
    strtext=hosts_row[0]
    strtext=re.sub(r'\_',' ',strtext)
    tmp=[l[0] for l in masterlist if strtext in l[1]]
    if tmp:
        Link=",".join(tmp)
        data=",".join(hosts_row)
        result=data+","+Link+"\n"
        result=result.decode()
        fs.write(result)
    else:
        print "Not Match"
print "Finish Matching"