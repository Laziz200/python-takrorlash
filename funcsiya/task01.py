def list_to_dict(input_list):
    result = {}
    for item in input_list:
        result[item[0]] = {"name": item[1], "grade": item[2]}
    return result

input_list = [
    [1, "Jean Castro", "V"],
    [2, "Lula Powell", "V"],
    [3, "Brian Howell", "VI"],
    [4, "Lynne Foster", "VI"],
    [5, "Zachary Simon", "VII"],
]

output_dict = list_to_dict(input_list)
print(output_dict)