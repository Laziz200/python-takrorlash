def count_even_odd(numbers):
    result = {"toq": 0, "juft": 0}
    for number in numbers:
        if number % 2 == 0:
            result["juft"] += 1
        else:
            result["toq"] += 1
    return result

numbers = [1, 2, 3, 5, 7, 8, 9, 10]
print(count_even_odd(numbers))