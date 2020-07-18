# matrix-generator

This is a python program that helps you to make a sympy matrix easily. This module uses [sympy](https://www.sympy.org/en/index.html), python library for simbolic mathmatics. 

By using this generator, you can create a new sympy matrix with only entering the dimension size and elements.

## Dependencies

The following dependencies are required

- [sympy](https://www.sympy.org/en/index.html)

## Download

 ``` bash
  $ pip install mgenerator
  ```

## Example
```python
    from mgenerator import *
    
    foo = new() # makes new sympy Matrix object. You will enter elements
    foo = new(1,2) # makes new sympy Matrix with 1 raw and 2 column
    
    ef(foo) # makes foo as Echelon form
    rf(foo) # makes foo as Reduced Echelon form
    
    num = 3
    ran(num) #finds image num elements vector range
    
    #used in finding eigenvalues
    char(foo, 3) #makes characteristic polynomial equation, and finds soluton with 3*3 matrix
    
    orthon(foo) #makes orthogonal basis matrix
    
    vec(2,1) #makes the vector (2,1)
```

## Instructions

1. `new( )`:

- When you make a mistake, just enter 'Enter'. **It will make new matrix**
- You can use any type of componenent(int,float,string), even a fraction like 1/2

2. `ran( )`:

- First you have to find echelon form of linear combination's agmented coefficient matrix
- Put coefficients of the range. Ex) If the range is ax-by-cz = 0 -> enter a,-b,-c

3. `char( )`:

- Put a Matrix and number of the matrix dimension ( if 2 by 2 matrix, enter 2 )
