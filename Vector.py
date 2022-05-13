# Diego Velasco
# Last modified 22 April 2022
import math

import sympy
from sympy import *
x, y, z = symbols('x y z')
init_printing(use_unicode=True)


class Vector:
    def __init__(self, i, j, k):
        self.__iComp = i
        self.__jComp = j
        self.__kComp = k
# The boring stuff.
# Accessor and mutator methods

    def get_i(self):
        return self.__iComp

    def get_j(self):
        return self.__jComp

    def get_k(self):
        return self.__kComp

    def set_i(self, i):
        self.__iComp = i

    def set_j(self, j):
        self.__jComp = j

    def set_k(self, k):
        self.__kComp = k

    def to_string(self):
        return "Vector = " + str(self.get_i()) + "i + " + str(self.get_j()) + "j + " + str(self.get_k()) + "k "

    def display(self):
        print(self.to_string())


# Vector calculus operations

    def add(self, b):
        vec_sum = Vector(0, 0, 0)
        vec_sum.set_i(sympy.Add(self.get_i(), b.get_i()))
        vec_sum.set_j(sympy.Add(self.get_j(), b.get_j()))
        vec_sum.set_k(sympy.Add(self.get_k(), b.get_k()))
        return vec_sum

    def dotproduct(self, b):
        return self.get_i()*b.get_i() + self.get_j()*b.get_j() + self.get_k()*b.get_k()

    def crossproduct(self, b):
        axb = Vector(0, 0, 0)
        axb.set_i(self.get_j() * b.get_k() - self.get_k() * b.get_j())
        axb.set_j(-1*self.get_i() * b.get_k() + self.get_k() * b.get_i())
        axb.set_k(self.get_i() * b.get_j() - self.get_j() * b.get_i())
        return axb

    def magnitude(self):
        return math.sqrt(pow(self.get_i(), 2) + pow(self.get_j(), 2) + pow(self.get_k(), 2))

    def is_normal(self, b):
        return self.crossproduct(b) == 0

    def scale(self, factor):
        self.set_i(factor*self.get_i())
        self.set_j(factor*self.get_j())
        self.set_k(factor*self.get_k())
        return self

    def gradient(self):
        grad_a = Vector(0, 0, 0)
        grad_a.set_i(diff(self.get_i(), x))
        grad_a.set_j(diff(self.get_j(), x))
        grad_a.set_k(diff(self.get_k(), x))
        return grad_a


'''
A = Vector(1, 1, 1)
B = Vector(1, 1, 10)
C = A.crossproduct(B)
print(A.magnitude())
print(A.dotproduct(B))
C.display()

B.scale(2)
B.display()


helix = Vector(sin(x), cos(x), x)
grad = helix.gradient()
helix.display()
grad.display()

print(diff(x, x))
print(helix.get_i())

minusB = 
minusB.display()

testSum = B.add(minusB)
testSum.display()
'''

