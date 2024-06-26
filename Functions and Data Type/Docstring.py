print("""
    Calculate the square of a given number.

    Parameters:
    n (int): The number whose square is to be calculated.

    Returns:
    int: The square of the input number `n`.
    """)
def calculate_square(n):
    return n ** 2

# Example usage:
number = int(input("Number: "))
square = calculate_square(number)
print(f"The square of {number} is: {square}")
