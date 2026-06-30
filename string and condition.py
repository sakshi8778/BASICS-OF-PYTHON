str1 = "fmdfdjk kvjdnk. \n bhdjbh"
print(str1)
str2 = "k" + " "+"dvjhdvbhjbvjh"
str3 = 'd'
print(str2+str3)
print(len(str1))
print(str1[1])#indexing
print(str1[4:len(str1)])#slicing eg(4:7)
print(str2[-12:-7])
print(str2.endswith("vjh"))
print(str2.capitalize())
print(str1.replace("b","f"))#value exchange
print(str1.find("f"))# index num of letter present
print(str1.count("f"))#num of f
#conditional statement(if else)
age = 2

if(20 >= age >= 10):
    print("you are a teen")
elif(age <= 10):
    print("bachuu")
else:
    print ("old")#indentation(proper spacing)


marks = int(input("enter student marks:"))
if(marks >= 85):
    print("A")
elif(75 <= marks < 85):
    print("B")
elif(65 <= marks < 75):
    print("C")
else:
    print("D")

#even no & multiple
n = int(input("no.:"))
if (n%2 == 0):
        print("even and multiple of 2")
else:
        ("odd and not multiple of 2")

        #large no
a = int(input("no1.:"))
b = int(input("no2.:"))
c = int(input("no3.:"))
        
if(a>=b and a>=c):
   print("1 large no")
elif(b>=c):
   print("2 large no:")
else:
   print("3 large no:")
