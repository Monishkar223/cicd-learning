import math
class Calculator:

    def _validate(self,args):
        if not args:
            raise ValueError("Please enter atleast one value")
        if not all(isinstance(x,(int,float)) for x in args):
            raise TypeError("Only Number are allowed here")


    def add(self,*args):
        self._validate(args)
        return sum(args)
    
    def sub(self,*args):
        self._validate(args)      
        result=args[0]
        for num in args[1:]:
            result-=num
        return result
    
    def mul(self,*args):
        self._validate(args)   
        result=args[0]
        for num in args[1:]:
            result*=num
        return result

if __name__=="__main__":
    obj1=Calculator()
    print(obj1.add(1,2,3,4,-5))
    print(obj1.sub(-1,-2,-3,-4,-5,1234,1234))
    print(obj1.mul(12,12,1,1,23,12,234,123,1234))
