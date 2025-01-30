def extract_numbers(strings):
    result = []
    for s in strings:
        num_str = ''.join(filter(str.isdigit, s))
        if num_str:
            result.append(int(num_str))
    return result

input_strings = ["2w3e", "er4", "56%"]
output_numbers = extract_numbers(input_strings)
print(output_numbers) 