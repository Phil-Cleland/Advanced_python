names = ["sam", "john", "james"]
map(len,names)
print (list(map(len,names)))

def sqr(x): return x**2
print(list(map(sqr,map(len,names))))

