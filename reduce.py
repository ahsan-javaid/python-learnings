from functools import reduce

lst = [5,10,15,20,25]

reduce(lambda x,y: x+ y, lst)