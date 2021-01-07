
import ply.lex as lex
import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'NUMBER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS',
    'LPAREN', 'RPAREN', 'POWER',
)

# Tokens

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_POWER = r'\^'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Ignored characters
t_ignore = " \t"


def t_continue(t):
    r'\\\n'
    # print(t)
    pass


def t_comment(t):
    r'\#(\\\n|.)*'
    pass


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count()


def t_error(t):
    print(f"Illegal character {t.value[0]!r}")
    t.lexer.skip(1)


# Build the lexer
lex.lex()

# Precedence rules for the arithmetic operators
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('nonassoc', 'NEGNUM', 'NEG', 'NEGWYK'),
    ('right', 'POWER'),

)

# dictionary of names (for storing variables)
names = {}

RING_VALUE = 1234577
EULER_RING = 1234576
NORMAL_RING = 1234577


def ring(value):
    return value % RING_VALUE


def p_statement_expr(p):
    'statement : expression'
    if p[1] < 0:
        print("\nWynik ", ring(p[1]),)
    else:
        print("\nWynik: ", p[1], )


def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression POWER wyk
                  | expression DIVIDE expression'''
    if p[2] == '+':
        p[0] = ring(p[1] + p[3])
        print("+ ", end='')
    elif p[2] == '-':
        p[0] = ring(p[1] - p[3])
        print("- ", end='')
    elif p[2] == '*':
        p[0] = ring(p[1] * p[3])
        print("* ", end='')
    elif p[2] == '^' and p[3] != '-':
        p[0] = ring(intpow(p[1], p[3]))
        print("^ ", end='')
    elif p[2] == '^' and p[3] == '-':
        p[0] = ring(intpow(modinv(p[1], 1234577), abs(p[4])))
        print("^ ", end='')
    elif p[2] == '/':
        p[0] = ring(p[1] * pow(p[3], EULER_RING - 1, RING_VALUE))
        print("/ ", end='')


def p_expression_uminus(p):
    'expression : MINUS NUMBER %prec NEGNUM'
    p[0] = -p[2]
    print(ring(p[0]), end=' ')


def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]


def p_expression_negation(p):
    'expression : MINUS  LPAREN expression RPAREN  %prec NEG'
    p[0] = -p[3]


def p_expression_bracket_number(p):
    'expression : LPAREN NUMBER RPAREN'
    p[0] = p[2]

    print(ring(p[0]), end=' ')


def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ring(p[1])

    print(ring(p[0]), end=' ')


def p_wyk_binop(t):
    '''wyk : wyk PLUS wyk
           | wyk MINUS wyk
           | wyk TIMES wyk
           | wyk DIVIDE wyk'''
    global RING_VALUE
    RING_VALUE = EULER_RING
    if t[2] == '+':
        t[0] = ring(t[1] + t[3])
    elif t[2] == '-':
        t[0] = ring(t[1] - t[3])
    elif t[2] == '*':
        t[0] = ring(t[1] * t[3])
    elif t[2] == '%':
        t[0] = ring(t[1] % t[3])


def p_wyk_negwyk(t):
    'wyk : MINUS NUMBER %prec NEGWYK'
    t[0] = (-t[2])

    print(ring(t[0]), end=' ')


def p_wyk_neg(t):
    'wyk : MINUS wyk %prec NEG'

    t[0] = (-t[2])


def p_wyk_group(t):
    'wyk : LPAREN wyk RPAREN'

    t[0] = (t[2])


def p_wyk_num(t):
    'wyk : NUMBER'

    t[0] = ring(t[1])
    print(ring(t[0]), end=' ')


def p_error(p):
    print(f"Syntax error at {p.value!r}")


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def intpow(x,  y):
    result = 1
    if y > 0:
        while y > 0:
            result = (result * x) % 1234577
            y -= 1

    elif y < 0:
        x = modinv(x, 1234577)
        y = abs(y)
        while y > 0:
            result = (result * x) % 1234577
            y -= 1

    return result


def mod(x):
    if x > 0:
        x = -x
    while x < 0:
        x = 1234577 + x
    return x


yacc.yacc()

while True:
    try:
        s = input('')
    except EOFError:
        break
    yacc.parse(s)
