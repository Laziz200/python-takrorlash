def sum_of_tuples(lst):
    return [sum(t) for t in lst]

input1 = [(1, 2), (2, 3), (3, 4)]
output1 = sum_of_tuples(input1)
print(output1) 

input2 = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
output2 = sum_of_tuples(input2)
print(output2)  