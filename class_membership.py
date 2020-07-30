class A:
    pass
class B:
    pass
class C:
    pass
a = A()
b = B()
c = C()
print isinstance(a, A)
print isinstance(b, A)
print isinstance(c, A)
print isinstance(b, B)
print isinstance(c, C)

