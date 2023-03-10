#1challenge
class var:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def  sqsum(self):
       self.x=self.x*self.x
       self.y=self.y*self.y
       self.z=self.z*self.z
       return self.x+ self.y+ self.z
        
result=var(1,3,5)   
print(result.sqsum())
#2challenge
class calulator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2
    def subtract(self):
        if self. num1>self.num2:
           return  self.num1-self.num2
        else:
             return self.num2-self.num1
    def multiply(self):
        return  self.num1*self.num2
    def div(self):
        if self. num1>self.num2:
           return  self.num1/self.num2
        else:
           return  self.num2/self.num1
result=calulator(10,94)  
print(result.add())
print(result.subtract())
print(result.multiply())
print(result.div())         
