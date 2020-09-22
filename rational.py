class Rational:

    __init__(self, p, q):
        self.p = p
        self.q = q

    __float__(self):
        return self.p/self.q
