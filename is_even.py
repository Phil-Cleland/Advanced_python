from functools import reduce
def is_even(number):
    return number %2==0
numbers= [1,56,234,87,4,76,24,69,90,135]
print ([number for number in numbers if is_even(number)])

print ([number for number in numbers if number %2==1 ])
print()

print ([number for number in numbers if not number %2==0])

print ()
squares= list(filter(lambda x:(x %2==0), numbers))
print (squares)

