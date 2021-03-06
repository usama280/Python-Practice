def fil(x):
    return x > 0 and isinstance(x, int)

lst = [4, 5.6, -1, 3.14, -2, 3]
#lst = [i for i in lst if i >0 and isinstance(i, int)]      -- Also filters


filteredList = list(filter(lambda i: i>0 and isinstance(i, int), lst)) #with lambda
filteredL2 = list(filter(fil, lst)) #w/o lambda

print(filteredList)
print(filteredL2)

print(list(map(lambda x: x*x, filteredList)))
