# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    total_cost = 0.0

    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')

    return total_cost

	
	
	

filename=sys.argv[1]
cost = portfolio_cost(filename)#, 'rt')
print(f"Total cost: {cost}")

