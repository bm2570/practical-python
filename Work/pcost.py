# pcost.py
#
# Exercise 1.27
import csv
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

cost = portfolio_cost('Data/portfolio.csv')#, 'rt')
print(f"Total cost: {cost}")

