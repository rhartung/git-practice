import operator

def do_math(num1, num2, operation):
    """Performs an operation on 2 numbers.
    
    Params: num1 and num2 should be integers.  Operation is a string.
    Acceptable operations include Add, Subtract, Multiply, Divide.

    Returns integer that is result of operation."""

    valid_ops = {"add": operator.add, "subtract": operator.sub,
                 "multiply": operator.mul, "divide": operator.div}

    if type(num1) != int or type(num2) != int or type(operation) != str:
        return "num1 and num2 must be integers.  operation must be a string."

    operation = operation.lower()
    
    if operation not in valid_ops:
        return "Acceptable operations include Add, Subtract, Multiply, Divide."

    return valid_ops[operation](num1, num2)

print do_math(5, 4, "MulTiPly")
print do_math(10, 7, "add")
print do_math(80, 10, "DIVIDE")
print do_math(4, 6, "subtract")
print do_math(9, 7, "foo")
print do_math("bleeb", "bork", 700)
