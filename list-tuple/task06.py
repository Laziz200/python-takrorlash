def is_even_first_digit(number):
    first_digit = int(str(number)[0])
    return first_digit % 2 == 0

numbers = [123, 456, 789, 852, 12, 42, 61, 369]

even_first_digit_numbers = []
for num in numbers:
    if is_even_first_digit(num):
        even_first_digit_numbers.append(num)

print(even_first_digit_numbers)
