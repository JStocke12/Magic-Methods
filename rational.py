from math import gcd

class Rational:

    def __init__(self, p, q):
        if q == 0:
            raise Exception("Cannot divide by 0")
        if (not type(p) is int) or (not type(q) is int):
            raise TypeError("p and q must both be integers")
        if p == 0:
            self.p = 0
            self.q = 1
        else:
            self.p = p//gcd(p,q)
            self.q = q//gcd(p,q)

    def __float__(self):
        return self.p/self.q

    def __str__(self):
        return str(self.p)+"/"+str(self.q)

    def __add__(self, other):
        return Rational(self.p*other.q+other.p*self.q, self.q*other.q)

    def __sub__(self, other):
        return Rational(self.p*other.q-other.p*self.q, self.q*other.q)

    def __mul__(self, other):
        return Rational(self.p*other.p, self.q*other.q)

    def __truediv__(self, other):
        return Rational(self.p*other.q, self.q*other.p)

"""a = Rational(1,2)
b = Rational(1,3)
print("a = 1, b = 1/3")
print("a + b = "+str(a+b))
print("a - b = "+str(a-b))
print("a * b = "+str(a*b))
print("a / b = "+str(a/b))"""

cfracarr = [1,1,1,1]
cfrac = Rational(cfracarr[0], 1)
for i in cfracarr:
    cfrac = Rational(i, 1) + Rational(1, 1)/cfrac

print(cfrac)
