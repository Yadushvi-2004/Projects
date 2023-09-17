from math import sqrt

class Quadratic():

  def __init__(self, a , b , c ):
    self.a=a
    self.b=b
    self.c=c

  def __str__(self):
    if self.b < 0 and self.c < 0:
      return f"{self.a} x^2  {self.b} x {self.c}"
    elif self.b < 0 and self.c > 0:
      return f"{self.a} x^2  {self.b} x +{self.c}"
    elif self.b > 0 and self.c < 0:
      return f"{self.a} x^2  + {self.b} x {self.c}"
    return f"{self.a} x^2  + {self.b} x + {self.c}"

  def __add__(self,eq):
    return Quadratic(self.a + eq.a , self.b + eq.b , self.c + eq.c)

  def __sub__(self,eq):
    return Quadratic(self.a + eq.a , self.b + eq.b , self.c + eq.c)

  def solutions(self):
    sol1= (-self.b - sqrt((self.b ** 2)-4*self.a*self.c))/(2*self.a)
    sol2= (-self.b + sqrt((self.b ** 2)-4*self.a*self.c))/(2*self.a)
    return(sol1, sol2)


eq=Quadratic(1, 7, 9)
print(eq, eq.solutions(), sep='\n')