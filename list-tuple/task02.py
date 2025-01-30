def add_one_to_list(numbers):
    number = int(''.join(map(str, numbers)))
    number += 1
    return [int(digit) for digit in str(number)]

numbers = [1, 2, 9]
result = add_one_to_list(numbers)
print(result)  