subjects = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

sorted_subjects = sorted(subjects, key=lambda bal: bal[1])

print(sorted_subjects)