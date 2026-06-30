#i = 1
#while i <= 10:
 #   print(i)
 #   i += 1

n = [1,4,9,16,25,36,75,100]# words allow
idx = 0
while idx < len(n):
    print(n[idx])
    idx += 1
    #tuble find ele
#c = (1,4,9,16,25,36,75,100)

#x = 9
#hile i < len(c):
    #if(c[i] == x):
       # print("found at index", i)
      #  i += 1
i = 0
while i <= 10:
        
        if(i%2==0):
            i += 1
            continue#skip
           # break
        print(i)
        i += 1




max = ["jlk","lkk","poi"]
for val in max:#f0r loop
 print(val)
 str = "prettyplease"
for char in str:
 #print(char)
#else:
   # print("end")
    if(char == 'y'):
        print("found")
        break
    print(char)
#else  no need whwen loop is break
print("end")
for b in range(7, 10):#index printbetween 7 to 11
    print(b)
for v in range(4, 10, 2):#increae with 2 dif
    print(v)


n =8#6 int (input("enter input"))
#for i in range(1,11):
   # print(n*i)
   # pass#for null statment
sum = 0
for i in range(1, n+1):
    sum += i


print("sum total",sum)