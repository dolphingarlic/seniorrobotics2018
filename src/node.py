class node(object):

    def __init__(self, name, n, e, s, w):
        self.N = n
        self.E = e
        self.S = s
        self.W = w
        self.name = name

    def get_n(self):
        return self.N

    def get_e(self):
        return self.E

    def get_w(self):
        return self.W

    def get_s(self):
        return self.S

    def get_name(self):
        return self.name
