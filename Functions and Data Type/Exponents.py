def power(base, exponent): 
  if exponent == 0:
    return 1
  else:
    return base * power(base, exponent - 1)

# Example usage
result = power(2, 4)
print(f"{2} to the power of {4} is: {result}")