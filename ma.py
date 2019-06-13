import sympy as sy
def make(row,col):
    while True:
        count_column = 0
        count_row = 0
        M = [[0 for i in range(col)] for j in range(row)]
        while count_row < row:
                while count_column < col:
                    print('Index: ',count_row + 1,count_column + 1)
                    c = input('components ')
                    if c is ' ':
                        malfunction = True
                        break
                    elif isinstance(c,str):
                        M[count_row][count_column]= c
                    else:  
                        M[count_row][count_column]= float(c)
                    count_column += 1
                if malfunction:
                    break
                else:
                    count_row += 1
                    count_column = 0
        if malfunction:
            continue
        else:
            return sy.Matrix(M)
def new():
    while True:
        row = int(input('Matrix Row: '))
        col = int(input('Matrix Col: '))
        count_column = 0
        count_row = 0
        malfunction = False
        M = [[0 for i in range(col)] for j in range(row)]
        while count_row < row:
            while count_column < col:
                print('Index: ',count_row + 1,count_column + 1)
                c = input('components ')
                if c is '':
                    malfunction = True
                    break
                elif isinstance(c,str):
                    M[count_row][count_column]= c
                else:  
                    M[count_row][count_column]= float(c)
                count_column += 1
            if malfunction:
                break
            else:
                count_row += 1
                count_column = 0
        if malfunction:
            continue
        else:
            return sy.Matrix(M)
def ef(mat1):
    return mat1.echelon_form()
def rf(mat2):
    return mat2.rref()
def ran(num):
    count = 0
    coeff = [0 for i in range(num)]
    for count in range(num):
        coeff[count] = float(input('Write down Coefficient '))
    while True:
        count = 0
        s = 0
        for count in range(num):
            vector = float(input('Write down Vector '))
            s += coeff[count]*vector
        print(s)
        sentinel = int(input('Enter "-1" to terminate(if not Enter) '))
        if sentinel is -1:
            break

#sol is solution of equation of determinant matrix for eigenvalues
#which is charateristic equation
def char2(ma):
    #to make Matrix as A-LI
    B = sy.Matrix([['L',0],[0,'L']])
    C = ma - B
    eq = C.det()
    print("Characteristic Equation:")
    print(eq)
    print("Solution of Char_Equation")
    print(sy.solve(eq,'L'))
    return C
#More than 2 dimensional Matrix
def sol(ma):
    eq = ma.det()
    return sy.solve(eq,'L')