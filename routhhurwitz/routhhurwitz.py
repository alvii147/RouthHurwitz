import math
import urllib.parse
import numpy as np
import numpy.typing as npt
from sympy import simplify, Expr, latex, parse_expr, Poly, symbols

MATH_LATEX_URL = 'https://math.now.sh'


def get_expr(raw_expr: str) -> Expr:
    """
    Convert string to SymPy expression.
    """

    return simplify(parse_expr(raw_expr))

def table_to_latex_table(table: npt.NDArray) -> npt.NDArray:
    """
    Transform expressions in Routh-Hurwitz table to latex strings.
    """

    return np.vectorize(latex)(table)

def latex_to_url(latex: str) -> str:
    """
    Convert latex string to latex image URL.
    """

    url_enc_latex = urllib.parse.quote_plus(latex)

    return f'{MATH_LATEX_URL}?color=white&from=\\Large%20{url_enc_latex}'

def latex_table_to_html(table: npt.NDArray) -> str:
    """
    Convert latex table to HTML table.
    """

    html = '<table style="width:100%">'
    for r in range(table.shape[0]):
        html += '<tr>'
        for c in range(table.shape[1]):
            html += '<td style="padding-top: 20px; padding-bottom: 20px" align="center">'
            html += f'<img src="{latex_to_url(table[r, c])}" />'
            html += '</td>'

        html += '</tr>'

    html += '</table>'

    return html

def display_table(table: npt.NDArray) -> str:
    """
    Sets up Routh-Hurwitz table for displaying.
    """

    return latex_table_to_html(table_to_latex_table(table))

def display_polynomial(polynomial: Expr) -> str:
    """
    Sets up polynomial expression for displaying.
    """

    return latex(polynomial)

def get_polynomial(coeffs: list[str]) -> Expr:
    """
    Get expression from polynomial coefficients.
    """

    return Poly(reversed(coeffs), symbols('s')).as_expr()

def generate_table(polynomial: list[str]) -> npt.NDArray:
    """
    Generate Routh Hurwitz table from list of expressions representing polynomial
    coefficients.
    """

    degree = len(polynomial) - 1
    n_rows = degree + 1
    n_cols = math.ceil((degree + 1) / 2) + 1
    table = np.full((n_rows, n_cols), get_expr('0'), dtype=object)

    table[0, 0] = get_expr(f's ** {degree}')
    for c, coeff_idx in enumerate(range(degree, -1, -2), start=1):
        table[0, c] = get_expr(polynomial[coeff_idx])

    table[1, 0] = get_expr(f's ** {degree - 1}')

    for c, coeff_idx in enumerate(range(degree - 1, -1, -2), start=1):
        table[1, c] = get_expr(polynomial[coeff_idx])

    for r, exp in enumerate(range(degree - 2, -1, -1), start=2):
        table[r, 0] = get_expr(f's ** {exp}')

        for c in range(1, n_cols):
            r1c1 = 0
            r1c2 = 0
            r2c1 = 0
            r2c2 = 0

            try:
                r1c1 = table[r - 2, 1]
            except IndexError:
                pass

            try:
                r1c2 = table[r - 2, c + 1]
            except IndexError:
                pass

            try:
                r2c1 = table[r - 1, 1]
            except IndexError:
                pass

            try:
                r2c2 = table[r - 1, c + 1]
            except IndexError:
                pass

            table[r, c] = simplify(((r1c1 * r2c2) - (r2c1 * r1c2)) / (-r2c1))

    return table
