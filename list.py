sentence="the quick brown fox jump over the lazy dog"
words=sentence.split()
print(words)
print([len(word) for word in words if word != "the"])

print("")

numbers=[34.6, -203.4, 4409, 68.3, -12.2, 44.6, 12.7]
print([number for number in numbers if number >=0])

numbers1 = [12, 54, 33, 67, 24, 89, 11, 24, 47]
print([number for number in numbers1 if number %2==0])

print("")


words1= ["hello", "my", "name", "is", "Sam"]
cap= [(word.upper(),len(word)) for word in words1]
#lenth=[len(word) for word in words1]
print (cap)