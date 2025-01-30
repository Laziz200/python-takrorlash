list1 = [1, 2, 3, 5, 7, 8, 9, 10]
list2 = [1, 2, 4, 8, 9]

common_elements = list(filter(lambda x: x in list2, list1))
print(common_elements)