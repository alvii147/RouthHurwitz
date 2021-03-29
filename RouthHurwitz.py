from sympy import simplify
from sympy import latex
from sympy.parsing.sympy_parser import parse_expr

def getExpr(raw_expr):
    parsed_expr = parse_expr(str(raw_expr))
    simplified_expr = simplify(parsed_expr)
    return simplified_expr

def determinant(r1c1, r1c2, r2c1, r2c2):
    det = simplify((r1c1 * r2c2) - (r2c1 * r1c2))
    return det

def printRouthArray(RouthArray):
    for row in RouthArray:
        print(str(row[0]), end = '')
        print('\t | \t', end = '')
        for colNum in range(1, len(row)):
            print(str(row[colNum]), '\t\t', end = '')
        print('')

def exprArrToStrArr(expr_arr):
    str_arr = expr_arr.copy()
    for i in range(len(str_arr)):
        for j in range(len(str_arr[i])):
            str_arr[i][j] = str(str_arr[i][j]).replace('**', '^')
    return str_arr

def ToLaTeX(str_arr):
    latex_arr = str_arr.copy()
    for i in range(len(latex_arr)):
        for j in range(len(latex_arr[i])):
            latex_arr[i][j] = '$$' + latex(latex_arr[i][j]) + '$$'
    return latex_arr

def RouthHurwitz(polynomial):
    degree = len(polynomial) - 1

    row1 = []
    expr = getExpr(f's ** {degree}')
    row1.append(expr)

    for i in range(degree, -1, -2):
        expr = getExpr(polynomial[i])
        row1.append(expr)

    row2 = []
    expr = getExpr(f's ** {degree - 1}')
    row2.append(expr)

    for i in range(degree - 1, -1, -2):
        expr = getExpr(polynomial[i])
        row2.append(expr)

    if len(row1) > len(row2):
        row2.append(getExpr(0))

    cols = len(row1)
    RouthArray = [row1, row2]

    rowIndex = 2
    for i in range(degree - 2, -1, -1):
        row = [0] * (cols)
        row[0] = getExpr(f's ** {i}')

        for colIndex in range(1, cols):
            try:
                r1c1 = RouthArray[rowIndex - 2][1]
            except IndexError:
                r1c1 = 0

            try:
                r1c2 = RouthArray[rowIndex - 2][colIndex + 1]
            except IndexError:
                r1c2 = 0

            try:
                r2c1 = RouthArray[rowIndex - 1][1]
            except IndexError:
                r2c1 = 0

            try:
                r2c2 = RouthArray[rowIndex - 1][colIndex + 1]
            except IndexError:
                r2c2 = 0

            b = determinant(r1c1, r1c2, r2c1, r2c2) / (-r2c1)
            b = simplify(b)
            row[colIndex] = b

        RouthArray.append(row)
        rowIndex += 1

    return RouthArray

if __name__ == '__main__':
    # (K * a) + (K + 6)s + 11s^2 + 6s^3 + s^4
    arr = ['K * a', 'K + 6', '11', '6', '1']
    # K - 18 + 9s + 8s^2 + s^3
    arr2 = ['K - 18', 9, 8, 1]
    RouthHurwitz(arr2)