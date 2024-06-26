def second_largest(numbers):
  if len(numbers) < 2:
    return None

  largest = second_largest = float('-inf')
  for num in numbers:
    if num > largest:
      second_largest = largest
      largest = num
    elif num > second_largest and num != largest:
      second_largest = num
  return second_largest
if __name__ == "__main__":
    numbers = [10, 5, 8, 3, 11]
    second_highest = second_largest(numbers)
    print(f"The second largest number is: {second_highest}")