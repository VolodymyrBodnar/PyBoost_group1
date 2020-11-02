class Spy:
    pub = 1
    _prot = 2
    __privat = 3

inst = Spy()
print(inst.pub)
print(inst._prot)
print(inst._Spy__privat)

