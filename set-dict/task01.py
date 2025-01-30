set1={"Artel","Alif","Yandex", "Google", "Meta"}
set2={"Google", "Apple", "Amazon", "Meta"}
set3={"Alibaba", "Uzum", "Meta", "Google", "Amazon"}
elements = set1 & set2 & set3
print("Umumiy elementlar:", elements)

unique_to_set1 = set1 - set2 - set3
print("Faqat birinchi set uchun tegishli elementlar:",unique_to_set1)