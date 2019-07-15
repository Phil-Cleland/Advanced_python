from functools import reduce
total = reduce(lambda item, running_total: item + running_total, [1, 2, 3, 4, 5])
print (total)

def join_strings(joinwords):
    return reduce(lambda item, running_total: item + running_total, joinwords)
words=["My ", "name ", "is ", "Philemon."]
u = join_strings(words)
print (u)