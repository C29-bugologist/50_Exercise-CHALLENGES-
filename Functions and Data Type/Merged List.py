def merge_lists(list1, list2):
    merged_list = []
    for item1 in list1:
        merged_list.append(item1)
    for item2 in list2:
        merged_list.append(item2)
    return merged_list

# Example usage:
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

merged = merge_lists(list1, list2)
print("Merged list:", merged)
