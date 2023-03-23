def main(x, y):
    """Integer type variables 'x' and 'y' are given. Return the value of the expression in README.md file.
    https://github.com/codeschool43/Build_in_function_homework#build_func07

    Args:
        x (int): integer
        y (int): integer
        
    Returns:
        int: the value of the expression
    """
    x = ((x**2) + (6*x**3) + 3*x*y)
    return x
print(main(5, 2))