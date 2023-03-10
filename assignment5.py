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
