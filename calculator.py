import math

def calculate(expression):
    try:
        # Replace symbols for user-friendly input
        expression = expression.replace('^', '**')

        # Allowed functions
        allowed_names = {
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "log": math.log10,
            "sqrt": math.sqrt,
            "pi": math.pi,
            "e": math.e
        }

        return eval(expression, {"__builtins__": None}, allowed_names)

    except:
        return "Error"