def search_list(lst, target):
    for element in lst:
        if element == target:
            print(f"Element {target} found in the list.")
            break
    else:
        print(f"Element {target} not found in the list.")

def print_numbers(range_start, range_end):
    for num in range(range_start, range_end + 1):
        if num % 3 == 0:
            continue
        print(num, end=' ')
        
my_list = [1, 2, 3, 4, 5]
search_list(my_list, 3)
search_list(my_list, 6)
print("\n")
print_numbers(1, 20)
