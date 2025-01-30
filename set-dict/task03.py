set1={100, 20, 45, 80, 70, 50}
set2={30, 55, 70, 60, 32, 100}
set1 = {x for x in set1 if x >= 60}
set2 = {x for x in set2 if x >= 60}

common_elements = set1 & set2
if common_elements:
    average = sum(common_elements) / len(common_elements)
else:
    average = 0

print(average)