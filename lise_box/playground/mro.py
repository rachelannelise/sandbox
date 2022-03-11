# %%
#  Method Resolution Order
class Base:
    def yow(self):
        print("Base.yow")


class A(Base):
    def yow(self):
        print("A.yow")
        super().yow()


class B(Base):
    def yow(self):
        print("B.yow")
        super().yow()


class C(A, B):
    def yow(self):
        print("C.yow")
        super().yow()

c = C()
print(C.__mro__)
c.yow()

class C(B, A):
    def yow(self):
        print("C.yow")
        super().yow()

c = C()
print(C.__mro__)
c.yow()