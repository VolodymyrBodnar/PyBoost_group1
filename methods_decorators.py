class A:

    def __init__(self, a):
        self.a = a

    @property
    def get_id(self):
        return id(self)


a = A(2)
print(a.get_id)