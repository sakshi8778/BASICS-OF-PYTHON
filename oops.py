#class->constructor(call class)->object->attributes(value)->
from sqlalchemy import null


class Student:#class
    #defaultconstructor
   # def __init__(self):

    #parameterized constructor
    #sef =(instant attribute )can be changed

    def __init__(self,name,marks):#constructor
        self.school = "xyz"
        self.age = 67# fixed value
        self.name = name#"pagal"    can be changed as constructor is used
        self.marks = marks
        print("constructor called")
        self.school = "xyz"

s1 = Student("l", 85)#object
print (s1.name)
print (s1.age)
print (s1.school)
print (s1.marks)
s2 = Student("kbhjvhgcvfgc",null)
print(s2.name)
print(s2.marks)#only tell position af data as nuul value

#practice
class Student:
    def __init__(self,fname,percent):
        self.fname = fname
        self.percent = percent
    def get_avg(self):
        sum = 0 
        for val in self.percent:
            sum += val
        print("hi",self.fname,"your average score is:",sum/3)

s3 = Student("k",[9,6,7])
s3.get_avg()
class acc:
    def __init__(self,accno,balance):
        self.accno = accno
        self.balance = balance
    
    def debit(self,amt):
        self.balance -= amt
        print(self.get__balance()) 
    def credit(self,amt):
        self.balance += amt
        print(self.get__balance()) 
    def get__balance(self):
        return self.balance
   # print(acc1.get_balance())
acc1 = acc(5678,900)
acc1.debit(600)
acc1.credit(700)



#for private class add__
class account:
    def __init__(self, accno, balance):
        self.accno = accno
        self.__balance = balance# private class attribute
    
    def reset_balance(self):
        self.__balance()

acc1 = account(6789,3000)
print(acc1.accno)
print(acc1.reset_balance())