'''
#Parent class
class Animal:
    def speak(self):
        print('animal is speaking')

#child class
class Lion(Animal):
    def roar(self):
        print("lion is roaring")

simba=Lion()
simba.roar()
print(dir(simba))
simba.speak()
#multi level inheritance

class Cub(Lion):
    def walk(self):
        print("walking")

b=Cub()
b.walk()
b.roar()
b.speak()


#Multiple inheritance

class Calc1:
    def addition(self,a,b):
        return a+b

class Calc2:
    def multiplication(self,a,b):
        return a*b

class Calc3(Calc1,Calc2):
    def subtraction(self,a,b):
        return a-b

a=Calc3()
print(a.subtraction(5,3))
print(a.multiplication(5,3))
print(a.addition(5,3))

'''
'''
class A:
    def mk(self):
        print("i am from class A")

class B:
    def mk(self):
        print("i am from class B")

class C(A,B):
    def __init__(self):
        print("class C is getting constructed")

f=C()
f.mk()

print(C,mro())

class D(A):
    def mk(self):
        print('i am from class D')
        
g=D()

g.mk()
'''
#DATA ABSTRACTION

class Student:
    __count=0

    def __init__(self):
        Student.__count +=1

    def printCount(self):
        print("Count is",Student.__count)

stud1= Student()
stud1.printCount()
print(stud1.count)