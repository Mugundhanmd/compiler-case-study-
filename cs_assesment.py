
import re

# ---------------- LEXER ----------------
def lexer(code):
    tokens = re.findall(r'[a-zA-Z]+|\d+|[=+*()-]', code)
    return tokens

# ---------------- PARSER ----------------
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def parse_expression(tokens):
    if len(tokens) == 3:
        root = Node(tokens[1])
        root.left = Node(tokens[0])
        root.right = Node(tokens[2])
        return root
    return None

# ---------------- SEMANTIC ----------------
def semantic_check(var, value):
    if not var.isalpha():
        return False
    return True

# ---------------- MAIN ----------------
code = input("Enter expression: ")

tokens = lexer(code)
print("Tokens:", tokens)

# Remove assignment part
var = tokens[0]
expr_tokens = tokens[2:]

if semantic_check(var, expr_tokens):
    ast = parse_expression(expr_tokens)

    print("AST Root:", ast.value)
    print("Left:", ast.left.value)
    print("Right:", ast.right.value)
else:
    print("Semantic Error")