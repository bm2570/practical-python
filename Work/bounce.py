# bounce.py
#
# Exercise 1.5

height=100

for i in range(10):
    new_height=height*(3./5)
    print i+1,round(new_height,4)
    height=new_height
    i=+1
