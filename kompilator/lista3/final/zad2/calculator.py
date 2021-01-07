# Wojciech Wróblewski zad2 lista3 jftt

import ply.yacc as yacc
import ply.lex as lex


tokens = (
    'ADD', 'SUB', 'MULT', 'DIVIDE', 'MODULO', 'POWER',
    'LBRACKET', 'RBRACKET', 'END', 'ERR', 'NUMBER',
)


t_ADD = r'\+'
t_SUB = r'-'
t_MULT = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'
t_POWER = r'\^'
t_END = r'\n'
t_LBRACKET = r'\('
t_RBRACKET = r'\)'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


t_ignore = " \t"


def t_pass_endline(t):
    r'\\\n'
    pass


def t_ignore_comment(t):
    r'\#(\\\n|.)*'
    pass


def t_error(t):
    r'[a-zA-Z]*'

    if not err.state or not err.printed:
        err.state = True
        err.setPrinted(True)
        err.print_error()

    t.lexer.skip(1)


lexer = lex.lex()


precedence = (
    ('left', 'ADD', 'SUB'),
    ('left', 'MULT', 'DIVIDE', 'MODULO'),
    ('nonassoc', 'NEG_NUMBER', 'NEG_EXPONENT', 'NEG'),
    ('right', 'POWER'),
)


class Events:
    def __init__(self, n):
        self.out = ""
        self.error = False
        self.n = n
        self.current_input = ""

    def ring_modulo(self, value):
        return value % self.n

    def euler_modulo(self, value):
        return value % (self.n - 1)

    def display(self, string):
        self.out += (str(string)+" ")

    def set_error(self, value):
        self.error = value

    def inverse(self, a):
        # multiplicatiove inverse
        return pow(a, self.n - 2, self.n)

    def divide(self, a, b):
        return self.ring_modulo(a * self.inverse(b))

    def raise_to_the_power(self, a, b):
        return pow(a, self.ring_modulo(b), self.n)

    def get_result(self, err):

        result = yacc.yacc().parse(self.current_input)

        if err.state and not err.printed:
            err.setPrinted()
            err.print_error()

        if not err.state and event.out:
            print(self.out, "\nWynik:", result)

        self.out = ""

    def handle_newline(self):
        new_line = '\n'
        back_char = '\\'
        if len(self.current_input) == 0:
            return "pass"
        while self.current_input[-1] == back_char:
            self.current_input += new_line
            next = input()
            if len(next) == 0:
                return "break"
            self.current_input += next
        self.current_input += new_line
        return self.current_input


class Error:
    def __init__(self):
        self.message = "Błąd"
        self.state = False
        self.printed = False

    def clear_error_indicators(self):
        self.setError(False)
        self.setPrinted(False)

    def setError(self, value):
        self.state = value

    def setPrinted(self, value):
        self.printed = value

    def print_error(self):
        print(self.message)

    def print_exp_concat(self):
        print(self.message)
        print("exponents concatenation forbidden")


# define calculation ring
event = Events(1234577)
err = Error()


def p_end(t):
    '''expression : END
           | ERR'''
    pass


def p_exp_end(t):
    '''expression : expression END'''
    t[0] = t[1]


def p_expression_binop(p):
    '''expression : expression ADD expression
           | expression SUB expression
           | expression MULT expression
           | expression MODULO expression
           | expression DIVIDE expression
           | expression POWER exponent'''

    if p[2] == '+':
        p[0] = event.ring_modulo(p[1] + p[3])
        event.display(p[2])
    elif p[2] == '-':
        p[0] = event.ring_modulo(p[1] - p[3])
        event.display(p[2])
    elif p[2] == '*':
        p[0] = event.ring_modulo(p[1] * p[3])
        event.display(p[2])
    elif p[2] == '%':
        p[0] = event.ring_modulo(p[1] % p[3])
        event.display(p[2])
    elif p[2] == '/':
        p[0] = event.divide(p[1], p[3])
        event.display(p[2])
    elif p[2] == '^':
        p[0] = event.raise_to_the_power(p[1], p[3])
        event.display(p[2])


def p_wyk_binop(p):
    '''exponent : exponent ADD exponent
           | exponent SUB exponent
           | exponent MULT exponent
           | exponent MODULO exponent
           | exponent DIVIDE exponent
           | exponent POWER exponent'''

    if p[2] == '+':
        p[0] = event.ring_modulo(p[1] + p[3])
        event.display(p[2])
    elif p[2] == '-':
        p[0] = event.ring_modulo(p[1] - p[3])
        event.display(p[2])
    elif p[2] == '*':
        p[0] = event.ring_modulo(p[1] * p[3])
        event.display(p[2])
    elif p[2] == '%':
        p[0] = event.ring_modulo(p[1] % p[3])
        event.display(p[2])
    elif p[2] == '/':
        p[0] = event.divide(p[1], p[3])
        event.display(p[2])
    elif p[2] == '^':
        err.setError(True)
        err.setPrinted(True)
        err.print_exp_concat()


def p_expression_negnum(p):
    'expression : SUB NUMBER %prec NEG_NUMBER'

    p[0] = event.ring_modulo(-p[2])

    event.display(event.ring_modulo(-p[2]))


def p_expression_neg(p):
    'expression : SUB expression %prec NEG'

    p[0] = event.ring_modulo(-p[2])


def p_expression_brackets(p):
    'expression : LBRACKET expression RBRACKET'

    p[0] = p[2]


def p_expression_number(p):
    'expression : NUMBER'

    p[0] = event.ring_modulo(p[1])

    event.display(event.ring_modulo(p[1]))


def p_exponent_negexponent(p):
    'exponent : SUB NUMBER %prec NEG_EXPONENT'

    p[0] = event.euler_modulo(-p[2])

    event.display(event.euler_modulo(-p[2]))


def p_exponent_neg(p):
    'exponent : SUB exponent %prec NEG'

    p[0] = event.euler_modulo(-p[2])


def p_exponent_brackets(p):
    'exponent : LBRACKET exponent RBRACKET'

    p[0] = event.euler_modulo(p[2])


def p_exponent_number(p):
    'exponent : NUMBER'

    p[0] = event.euler_modulo(p[1])

    event.display(event.euler_modulo(p[1]))


def p_error(p):

    err.state = True
    if not err.printed:
        err.setPrinted(True)
        err.print_error()


yacc.yacc()
while True:
    err.clear_error_indicators()
    event.current_input = input()
    try:
        message = event.handle_newline()
        if message == "pass":
            continue
        elif message == "break":
            break

    except:
        err.print_error()
        break
    try:
        event.get_result(err)
    except:
        if err.state and not err.printed:
            err.setPrinted(True)
            err.setError(True)
            err.print_error()
