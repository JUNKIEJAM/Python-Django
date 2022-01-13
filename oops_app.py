#class MyClass:
 #   x=5
    
    
#p1=MyClass()
#print(p1.x)

#class Person:
 #   def __init__(self,name,age):
  #     self.name=name
   #    self.age=age
       
       

#p1=Person('John',87)
#print(p1.name)
#del p1
#print(p1) #error


#### INHERITANCE #####

from new import Student

class Person(Student):
    pass
    
p1=Person()
print(p1.name)
    