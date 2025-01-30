months = {
    'yan': ('Yanvar', 31),
    'fev': ('Fevral', 28),
    'mar': ('Mart', 31),
    'apr': ('Aprel', 30),
    'may': ('May', 31),
    'iyn': ('Iyun', 30),
    'iyl': ('Iyul', 31),
    'avg': ('Avgust', 31),
    'sen': ('Sentabr', 30),
    'okt': ('Oktabr', 31),
    'noy': ('Noyabr', 30),
    'dek': ('Dekabr', 31)
}

user_input = input("Oy nomini kiriting (dastlabki uchta harf): ").strip().lower()

if user_input in months:
    month_name, days = months[user_input]
    print(f"{month_name} {days} kundan iborat")
else:
    print("Noto'g'ri oy nomi kiritildi")