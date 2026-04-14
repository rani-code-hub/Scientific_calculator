import math

def calculate(expression, is_degree=False):
    try:
        expression = expression.replace('^', '**')

        # --- Custom trig functions ---
        def sin(x):
            return math.sin(math.radians(x)) if is_degree else math.sin(x)

        def cos(x):
            return math.cos(math.radians(x)) if is_degree else math.cos(x)

        def tan(x):
            # handle tan(90) type cases
            if is_degree and (x % 180 == 90):
                return "Undefined"
            return math.tan(math.radians(x)) if is_degree else math.tan(x)

        allowed_names = {
            "sin": sin,
            "cos": cos,
            "tan": tan,
            "log": math.log10,
            "sqrt": math.sqrt,
            "pi": math.pi,
            "e": math.e
        }

        return eval(expression, {"__builtins__": None}, allowed_names)

    except:
        return "Error"