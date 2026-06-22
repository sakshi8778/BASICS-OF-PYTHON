marks = [34.5,67.5,24,90.4]
#marks = ['str','raj','dah']
print (marks)
print(type(marks))
marks[0] = 12
marks.append(67)
print(marks)
marks.sort()# also works for letter
print(marks)
marks.sort(reverse = True)
print(marks)
marks.reverse()
print(marks)
marks.insert(2,45)
print(marks)
#print(marks.append(67))
#string= immutable(no change),list = mutable(change)
str = "hello"
#str[0] = "y"# not possible
print(str)

#tuple(immutable)
tup = (2,1,4,6,544)
tuo1 = (9,)#for 1 value , is necessary or it will be int


