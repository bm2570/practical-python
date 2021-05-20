# pcost.py
#
# Exercise 1.27

f = open('Data/portfolio.csv', 'rt')
headers = next(f)
cost=0
#headers'name,shares,price\n'
for line in f:
    #print(line, end='')
   a,b,c=line.split(',')
   cost=cost+(float(c)*float(b))
f.close()
print(f"Total cost: {cost}")
