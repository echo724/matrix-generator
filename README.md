
Matrix_python
=============
Make a matrix fast, and operate it easily by python(For Linear Algebra Students)
---------
    
## Introduction.
    
I used Sympy as a tool for Matrix operations  
<https://www.sympy.org/en/index.html>

#### Guide to start  
1. First install Pip in your enviroment.    
    follow this link for installation
    <https://pip.pypa.io/en/stable/installing/>     
2. Download **ma.py** in this page

3. In terminal ( for python 3 )    
>$ pip3 install sympy       
4. And then open python3 with terminal in the folder where this **ma.py** downloaded, and import ma.py

    in python
>   $ from ma.py import *

#### That's all! Use Functions for matrix operations.
    
## Functions.
    
Functions | Features | Declaration 
---|---|---
**new( )**|make new matrix|A = new()
**ef(matrix)**|make matrix ' A ' as Echelon form|E = ef(A)
**rf(matrix)**|make matrix ' A ' as Reduced Echelon form|R = rf(A)
**ran(number)**|check Image Vectors range|ran(3)
**char(matrix,num)**|make ' A-LI matrix ', and show Characteristic equation and solution|M = char(A,3)
    
## Instructions.
    
#### 1. new( ):  
*    When you make a mistake, just enter 'Enter'. **It will make new matrix**
*   You can use any type of componenent(int,float,string), even a fraction like 1/2    
#### 2. ran( ):  
*    First you have to find echelon form of linear combination's agmented coefficient matrix
*    Put coefficients of the range. 
     Ex) If the range is ax-by-cz = 0 -> enter a,-b,-c
    
#### 3. char( ):  
*    Put a Matrix and number of the matrix dimension ( if 2 by 2 matrix, enter 2 )