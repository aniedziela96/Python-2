from stack import Stack
from Lista3Zadanie3 import postfix_eval


#zmieniona funkcja aby działała dla wyrażeń z i bez białych znaków
def infix_to_postfix(infix_expr):
    prec = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}

    op_stack = Stack() # Stos operatorow
    postfix = [] # Wyjscie

    #zamian split robię listę charów, a białe znaki pomijam
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

if __name__ == "__main__":

    expr = input()

    while expr != "quit":
        
        print(postfix_eval(infix_to_postfix(expr)))

        expr = input()

