class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def output(self):
        print(self.a)

    @classmethod
    def jaja(cls, z, a):
        return '{} * {} = {}'.format(z, a, z * a)
