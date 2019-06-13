
Matrix_python
=============
Make a matrix fast, and operate it easily by python(For Linear Algebra Students)
---------
    
### Introduction.
    
I used Sympy as a tool for Matrix operations  
<https://www.sympy.org/en/index.html>
    
You have to install Sympy in your desktop first
    
In terminal(for python 3)    
>pip3 install sympy
    
And then open python3 with terminal in the folder where this **ma.py** downloaded, and import ma.py
    
>python3  
>from ma.py import *
    
#### That's all! Use Functions for matrix operations.
    
### Functions
    
Functions | Features | Declaration 
---|---|---
**new( )**|make new matrix|A = new()
ef(matrix)|make matrix ' A ' as Echelon form|E = ef(A)
**rf(matrix)**|make matrix ' A ' as Reduced Echelon form|R = rf(A)
**ran(number)**|check Image Vectors range|ran(3)
**char2(matrix)**|make ' A-LI matrix ', and show Characteristic equation and solution|M = char2(A)
**sol(matrix)**|make a solution for bigger than 2 by 2 ' A-LI matric ' determinant|M = sol(A)
    
### Instructions
    
#### 1. new( ):  
*    When you make a mistake, just enter 'Enter'. **It will make new matrix**
*   You can use any type of componenent(int,float,string), even a fraction like 1/2    
#### 2. ran( ):  
*    First you have to find echelon form of linear combination's agmented coefficient matrix
*    Put coefficients of the range. 
     Ex) If the range is ax-by-cz = 0 -> enter a,-b,-c
    
#### 3. char2( ) and sol( ):  
*    Put 2 by 2 matrix **' A '** as input of **char2( )**, not **' A - LI matrix '**
*    In the case of sol( ),  you have to put **' A - LI matrix '** ( L is lamda,eigenvalue )