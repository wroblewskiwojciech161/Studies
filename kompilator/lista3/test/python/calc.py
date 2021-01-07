# Wojciech Wróblewski zad2 lista 3
# jftt

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
    ('nonassoc', 'NEGNUM', 'NEG_EXPONENT', 'NEG'),
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

    def print_div_err(self):
        print(self.message)
        print("dividing by zero !!!")

    def print_mod_err(self):
        print(self.message)
        print("modulo 0 operation - undefined")


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


def p_expression_binop(t):
    '''expression : expression ADD expression
           | expression SUB expression
           | expression MULT expression
           | expression DIVIDE expression
           | expression MODULO expression
           | expression POWER exponent'''

    if t[2] == '+':
        t[0] = event.ring_modulo(t[1] + t[3])
        event.display(t[2])
    elif t[2] == '-':
        t[0] = event.ring_modulo(t[1] - t[3])
        event.display(t[2])
    elif t[2] == '*':
        t[0] = event.ring_modulo(t[1] * t[3])
        event.display(t[2])
    elif t[2] == '%':
        if t[3] == 0:
            err.setError(True)
            err.setPrinted(True)
            err.print_mod_err()
        else:
            t[0] = event.ring_modulo(t[1] % t[3])
            event.display(t[2])
    elif t[2] == '/':
        if t[3] == 0:
            err.setError(True)
            err.setPrinted(True)
            err.print_div_err()
        else:
            t[0] = event.divide(t[1], t[3])
            event.display(t[2])
    elif t[2] == '^':
        t[0] = event.raise_to_the_power(t[1], t[3])
        event.display(t[2])


def p_wyk_binop(t):
    '''exponent : exponent ADD exponent
           | exponent SUB exponent
           | exponent MULT exponent
           | exponent DIVIDE exponent
           | exponent MODULO exponent
           | exponent POWER exponent'''

    if t[2] == '+':
        t[0] = event.ring_modulo(t[1] + t[3])
        event.display(t[2])
    elif t[2] == '-':
        t[0] = event.ring_modulo(t[1] - t[3])
        event.display(t[2])
    elif t[2] == '*':
        t[0] = event.ring_modulo(t[1] * t[3])
        event.display(t[2])
    elif t[2] == '%':
        if t[3] == 0:
            err.setError(True)
            err.setPrinted(True)
            err.print_mod_err()
        else:
            t[0] = event.ring_modulo(t[1] % t[3])
            event.display(t[2])
    elif t[2] == '/':
        if t[3] == 0:
            err.setError(True)
            err.setPrinted(True)
            err.print_div_err()
        else:
            t[0] = event.divide(t[1], t[3])
            event.display(t[2])
    elif t[2] == '^':
        err.setError(True)
        err.setPrinted(True)
        err.print_exp_concat()


def p_expression_negnum(t):
    'expression : SUB NUMBER %prec NEGNUM'

    t[0] = event.ring_modulo(-t[2])

    event.display(event.ring_modulo(-t[2]))


def p_expression_neg(t):
    'expression : SUB expression %prec NEG'

    t[0] = event.ring_modulo(-t[2])


def p_expression_brackets(t):
    'expression : LBRACKET expression RBRACKET'

    t[0] = t[2]


def p_expression_number(t):
    'expression : NUMBER'

    t[0] = event.ring_modulo(t[1])

    event.display(event.ring_modulo(t[1]))


def p_exponent_negexponent(t):
    'exponent : SUB NUMBER %prec NEG_EXPONENT'

    t[0] = event.euler_modulo(-t[2])

    event.display(event.euler_modulo(-t[2]))


def p_exponent_neg(t):
    'exponent : SUB exponent %prec NEG'

    t[0] = event.euler_modulo(-t[2])


def p_exponent_brackets(t):
    'exponent : LBRACKET exponent RBRACKET'

    t[0] = event.euler_modulo(t[2])


def p_exponent_number(t):
    'exponent : NUMBER'

    t[0] = event.euler_modulo(t[1])

    event.display(event.euler_modulo(t[1]))


def p_error(t):

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
