class Adder:
    SEVEN = 7
    FIVE = 5

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        res = self.a + self.b
        print(res)

    @classmethod
    def seven_and_five(cls):
        res = cls.SEVEN + cls.FIVE
        print(res)

    @staticmethod
    def addition_static(a, b):
        res = a + b
        print(res)

