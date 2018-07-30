class node(object):

    def __init__(self, name, n, e, s, w):
        self.N = n
        self.E = e
        self.S = s
        self.W = w
        self.name = name

    def getN(self):
        return self.N

    def getE(self):
        return self.E

    def getW(self):
        return self.W

    def getS(self):
        return self.S

    def getName(self):
        return self.name