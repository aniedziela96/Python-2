from stack import Stack

# Alternatywne nazwy:
# 1. notacja zwykła, notacja infiksowa, infix notation
# 2. notacja polska (NP), notacja prefiksowa, Polish notation (PN), prefix notation
# 3. odwrotna notacja polska (ONP), notacja postfiksowa, Reverse Polish notation (RPN), postfix notation


def infix_to_postfix(infix_expr):
    prec = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}

    op_stack = Stack() # Stos operatorow
    postfix = [] # Wyjscie

    for token in list(infix_expr):
        if token == " ":
            continue
        elif token.isalnum():
            postfix.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            while op_stack.peek() != '(':
                postfix.append(op_stack.pop())

            op_stack.pop() # Zrzucenie '(' ze stosu
        else:
            while not op_stack.is_empty() and prec[op_stack.peek()] >= prec[token]:
                postfix.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():
        postfix.append(op_stack.pop())

    return " ".join(postfix)


def postfix_eval(postfix_expr):
    operand_stack = Stack()

    for token in postfix_expr.split():
        if token in '+-*/':
            b = operand_stack.pop()
            a = operand_stack.pop()
            result = do_math(token, a, b)
            operand_stack.push(result)  # operand_stack.push(do_math(token, a, b))
        else:
            operand_stack.push(int(token))

    return operand_stack.pop()


def do_math(op, a, b):
    if op == "*":
        return a * b
    elif op == "/":
        return a // b  # dla uproszczenia "/" będzie dzieleniem całkowitym
    elif op == "+":
        return a + b
    else:
        return a - b


if __name__ == "__main__":
    print(postfix_eval('29 5 - 3 2 * /'))

    print(infix_to_postfix("A * B + C * D"))
    print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
    print(postfix_eval(infix_to_postfix("( 5 - 6 ) * 4 - ( 5 - 2 * 2 )")))

    print(postfix_eval(infix_to_postfix("(1+2) * 5")))
