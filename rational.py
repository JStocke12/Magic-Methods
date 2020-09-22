class Rational:

    __init__(self, p, q):
        self.p = p
        self.q = q

    __float__(self):
        return self.p/self.q

    __str__(self):
        return str(self.p)+"/"+str(self.q)
