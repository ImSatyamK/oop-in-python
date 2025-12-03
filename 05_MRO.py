class A:
    def show(self): print("A")

class B(A):
    def show(self): print("B")

class C(A):
    pass

class D(B):
    pass

class E(C):
    def show(self): print("E")

class F(C):
    def show(self): print("F")

class G(E, F):
    pass

class X(D, G):
    pass

x = X()
x.show()
print(X.mro())