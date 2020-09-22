from math import gcd

class Rational:

    __init__(self, p, q):
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

    __float__(self):
        return self.p/self.q

    __str__(self):
        return str(self.p)+"/"+str(self.q)
