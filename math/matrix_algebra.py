# Matrix Algebra

import numpy as np
from scipy import linalg

A = np.array([[1,2,3],[2,7,4]])
B = np.array([[1,-1],[0,1]])
C = np.array([[5,-1],[9,1],[6,0]])
D = np.array([[3,-2,-1],[1,2,3]])

u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])
w = np.array([[1],[8],[0],[5]])

alpha = 6

two_point_one = u + v
two_point_two = u - v
two_point_three = alpha * u
two_point_four = u.dot(v)
two_point_five = np.sqrt((u[0]**2+u[1]**2+u[2]**2+u[3]**2))

#three_point_one = A + C <--- This cannot be done because matrices don't have
#same dimensions! So I comment it out so my code compiles

three_point_two = A - C.transpose()
three_point_three = C.transpose() + 3*D
three_point_four = np.dot(B,A)

#three_point_five = np.dot(B,A.transpose()) <--- B has 2 columns, and A.transpose
#has three rows, meaning they cannot be multiplied together! A.transpose B would work
#but is an entirely different problem.

#three_point_six = np.dot(B,C) <-- this also doesn't work for the same reason as 3.5

three_point_seven = np.dot(C,B)
three_point_eight = np.dot(np.dot(np.dot(B,B),B),B)
three_point_nine = np.dot(A,A.transpose())
three_point_ten = np.dot(D.transpose(),D)


print two_point_one
print "**********"
print two_point_two
print "**********"
print two_point_three
print "**********"
print two_point_four
print "**********"
print two_point_five
print "**********"
#print three_point_one
print three_point_two
print "**********"
print three_point_three
print "**********"
print three_point_four
print "**********"
#print three_point_five
print three_point_seven
print "**********"
print three_point_eight
print "**********"
print three_point_nine
print "**********"
print three_point_ten
print "**********"
