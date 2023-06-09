def add(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y != 0:
        z = x / y
    else:
        z = "Infinite"
    
    return z

def exponent(x,y):
    return x**y

def percentage(x,y):
    if y >= x or y != 0:
        z = (x / y) * 100
    else:
        z = "Invalid Input!!!"
    
    return z

'''class Calculator:
    x = 0 
    y = 0
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def add(self):
        sum = self.x + self.y
        return sum
    
    def subtraction(self):
        sub = self.x - self.y
        return sub
    
    def multiply(self):
        mul = self.x * self.y
        return mul
    
    def divide(self):
        if self.y != 0:
            div = self.x / self.y
        else:
            div = "Infinite"
        
        return div
    
    def exponent(self):
        exp = self.x ** self.y
        return exp
    
    def percentage(self):
        if self.y >= self.x or self.y != 0:
            per = (self.x / self.y) * 100
        else:
            per = "Invalid Input!!!"
        
        return per

obj = Calculator()'''