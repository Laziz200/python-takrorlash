def digit(numbers):
    result = []
    for number in numbers:
        first_digit = int(str(number)[0])
        if first_digit % 2 == 0:
            result.append(number)
    return result

input_numbers = [123, 456, 789, 852, 12, 42, 61, 369]
output_numbers = digit(input_numbers)
print(output_numbers)