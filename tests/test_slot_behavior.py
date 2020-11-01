# https://stackoverflow.com/questions/1816483/how-does-inheritance-of-slots-in-subclasses-actually-work


class A:
    __slots__ = ["a"]


class B(A):
    b: int


def test_slot_ineritance():
    b = B()
    b.a = b.b = 3
