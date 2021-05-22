# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename,i):
    f = open('filename', 'rt')
    headers = next(f)
    cost=0
#headers'name,shares,price\n'
    for line in f:
    #print(line, end='')
        a,b,c=line.split(',')
        cost=cost+(float(c)*float(b)
    #f.close()
    return cost

cost = portfolio_cost('Data/portfolio.csv', 'rt')
print(f"Total cost: {cost}")
