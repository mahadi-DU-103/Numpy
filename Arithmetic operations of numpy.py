#1. addition(+):
import numpy as np
x = np.array([[1,2],
              [2,3]]) #during arithmetic operations the matrices must be of same dimension.
y = np.array([[4,5],
              [5,6]])
z = x+y
print("the addition of these 2 matrices are:",z)

#2. substraction(-):
w1 = x-y
w2 = y-x
print("the substraction of thr two matrices are:",w1)
print("the substraction of thr two matrices are:",w2)

#3. multiplication(*): for element wise multiplication
mul1 = x*y
print("the multiplication of the two matrices are:",mul1)

#for matrix multiplication(@):
mul2 = x@y
mul3 = y@x
print("the matrix multiplication of the two matrices are:",mul2)
print("the matrix multiplication of the two matrices are:",mul3)

#4. division(/): 
div1 = x/y
div2 = y/x
print("the division of the 2 matrixes are:",div1)
print("the division of the 2 matrixes are:",div2)

#5. floor div(//):
div3 = x//y
div4 = y//x
print("the floor division of the 2 matricces are:",div3)
print("the floor division of the 2 matricces are:",div4)

#6. exponensiation(**):
expo = x**y
print("x to the power y is:",expo)

#7. remainder(%):
rem = x%y
print("the remainder is:",rem)

#8. transpose:
transpose = np.transpose(x)
print("the transpose matrix of x is:",transpose)