# pcost.py
#
# Exercise 1.27
import csv
import sys
def portfolio_cost(filename):
    f = open(filename, 'rt')
    headers = next(f)
    cost=0
    for line in f:
        try:
            row=csv.reader(f)
            row=line.split(',')
            share=row[1]
            sharecost=row[2]
            cost=cost+int(share)*float(sharecost)
        except ValueError:
            print("error in cost calculation")
    return cost

filename=sys.argv[1]
cost = portfolio_cost(filename)#, 'rt')
print(f"Total cost: {cost}")

