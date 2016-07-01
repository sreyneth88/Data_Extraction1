import xlrd
import csv

def csv_from_excel():

    wb = xlrd.open_workbook('AllKyan.xlsx')
    sh = wb.sheet_by_name('Sheet1')
    AllKyan = open('AllKyan.csv', 'wb')
    wr = csv.writer(AllKyan, quoting=csv.QUOTE_ALL)

    for rownum in xrange(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    AllKyan.close()