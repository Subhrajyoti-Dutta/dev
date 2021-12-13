class Triangle():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
    def is_valid(self):
        if (self.a+self.b>self.c) and (self.b+self.c)>self.a and (self.a+self.c)>self.b:
            return 'Valid'
        else:
            return 'Invalid'
            
    def Side_Classification(self):
        if self.is_valid() == 'Valid':
            if self.a == self.b:
                if self.c == self.a:
                    return 'Equilateral'
                else:
                    return 'Isosceles'

            elif self.c == self.a or self.b == self.c:
                return 'Isosceles'

            else:
                return 'Scalene'
        return 'Invalid'
    
    def Angle_Classification(self):
        if self.is_valid() == 'Valid':
            min,mid,max = sorted((self.a**2,self.b**2,self.c**2))
            if min+mid == max: return 'Right'
            elif min+mid > max: return 'Acute'
            else: return 'Obtuse'
        return 'Invalid'
    
    def Area(self):
        if self.is_valid() == 'Valid':
            s = (self.a+self.b+self.c)/2
            return (s*(s-a)*(s-b)*(s-c))**0.5
        return 'Invalid'
        
a=int(input())
b=int(input())
c=int(input())
T=Triangle(a,b,c)
print(T.is_valid())
print(T.Side_Classification())
print(T.Angle_Classification())
print(T.Area())