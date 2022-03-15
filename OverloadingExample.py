'''

#overloading==> for a same method(function)/ operator ,will have different behaviour
print(2+3)

print('hi'+'hello')

#method overloading
class A:
    def myCalculate(self,x=None,y=None):
        if x!=None and y!=None:
            return x+y
        elif x!=None:
            return x**2
        else:
            return 0

res=A()
print('zero',res.myCalculate())
print('one arg',res.myCalculate(5))
print('two arg',res.myCalculate(3,4))

obj1=A()
obj2=A()

print([1,2]+[3,4])
print(obj1+obj2)
'''

class A:

    def __init__(self,num):
        self.num=num
    def __add__(self,other):
        return self.num+other.num

obj1=A(3)
obj2=A(6)

print(obj1.num)
print(obj2.num)
print(obj1+obj2)
