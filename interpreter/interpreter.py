def main():
    expression = input("Expression: ")
    result = evaluate_expression(expression)
    print(f"{result:.1f}")

def evaluate_expression(expression):
    # Split the expression into its components
    x, operator, z = expression.split()

    # Convert the operands to integers
    x = int(x)
    z = int(z)

    # Perform the appropriate arithmetic operation
    if operator == "+":
        return x + z
    elif operator == "-":
        return x - z
    elif operator == "*":
        return x * z
    elif operator == "/":
        return x / z
    else:
        raise ValueError("Unknown operator")

main()
