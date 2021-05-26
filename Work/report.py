# report.py
#
# Exercise 2.4

import csv
import sys
import numpy as np
def read_portfolio(filename1,rt):
    portfolio = []
    with open(filename1) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            info = { 'name':row[0],'shares':int(row[1]),'price':float(row[2]) }
            portfolio.append((info))

    return portfolio
 
def read_prices(filename2):

    prices = {}
    with open(filename2) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices 
 
# def read_prices(filename2):
    # prices=[]
    # with open(filename2) as f:
        # rows = csv.reader(f)
        # for row in rows:

			# prices.append((row))

    # return prices

filename1=sys.argv[1]
name1 = read_portfolio(filename1,'rt')

# for i in range(len(name1)):
    # print (name1[i])
	
filename2=sys.argv[2]
name2=read_prices(filename2)


cost_portfolio=0.0
for i in name1:
    cost_portfolio=cost_portfolio+i['shares']*i['price']
print(f"amount originally paid: {cost_portfolio}")

cost_price=0.0
for i in name1:
    cost_price=cost_price+i['shares']*name2[i['name']]
print(f"value currently: {cost_price}")

print(f"current worth: {round(cost_price-cost_portfolio,2)}")
# pricename=np.zeros(30)
# currentprice=np.zeros(30)
# for i in range(len(name2)):
	# if name[i]==str('):
		# print name[i]
# for i in range(len(name2)):
    # print (name2[i])

	
headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %8s %8s' % headers)
print(('-' * 10 + ' ') * len(headers))
for row in name1:
    print (f"\t{row['name']}\t{row['shares']}\t  {row['price']}\t  {round(row['price']-name2[row['name']],2)}")

	