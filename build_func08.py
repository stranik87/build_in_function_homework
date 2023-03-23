def main(x, y):
    """Integer type variables 'x' and 'y' are given. Return the value of the expression in README.md file.
    https://github.com/codeschool43/Build_in_function_homework#build_func08

    Args:
        x (int): integer
        y (int): integer
        
    Returns:
        int: the value of the expression
    """
    x = 5*x**2*y**3 +  x*y**2
    return x
print(main(7, 1))