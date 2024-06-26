def squares_of_first_n(n):
    squares = [i**2 for i in range(1, n+1)]
    return squares

# Example usage:
n = 5
result = squares_of_first_n(n)
print(f"Squares of the first {n} natural numbers:", result)
