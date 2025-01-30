def extract_digits(s):
    return ''.join(filter(str.isdigit, s))

input_str = "w34r1"
output_str = extract_digits(input_str)
print(output_str) 