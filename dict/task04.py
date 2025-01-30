days = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31,
}
sorted_months_days = dict(sorted(days.items(), key=lambda item: item[1]))

for month, days in sorted_months_days.items():
    print(f"{month}: {days} kun")