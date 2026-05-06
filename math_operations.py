import ast
import operator

def add_numbers(a: float, b: float) -> float:
    return a + b

def calculate_string(math_expression: str) -> float:
    allowed_ops = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
    }

    def _eval(node):
        if isinstance(node, ast.Constant):
            return node.n
        elif isinstance(node, ast.BinOp):
            return allowed_ops[type(node.op)](_eval(node.left), _eval(node.right))
        raise ValueError(f"Unsupported expression: {node}")

    tree = ast.parse(math_expression, mode='eval')
    return _eval(tree.body)
