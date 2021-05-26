# report.py
#
# Exercise 2.4

import csv
import sys
def read_portfolio(filename,rt):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            info = { 'name':row[0],'shares':int(row[1]),'price':float(row[2]) }
            portfolio.append((info))

    return portfolio
filename=sys.argv[1]
name = read_portfolio(filename,'rt')

for i in range(len(name)):
    print (name[i])
