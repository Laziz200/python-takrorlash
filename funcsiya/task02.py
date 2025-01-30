def sort_odd_even(lst):
    odd = sorted([x for x in lst if x % 2 != 0])
    even = sorted([x for x in lst if x % 2 == 0], reverse=True)
    
    result = []
    odd_index = 0
    even_index = 0
    
    for x in lst:
        if x % 2 != 0:
            result.append(odd[odd_index])
            odd_index += 1
        else:
            result.append(even[even_index])
            even_index += 1
    
    return result

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
output_list = sort_odd_even(input_list)
print(output_list)