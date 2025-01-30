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
a=input("oy nomini kiritiing: ")
for key in days:
    if key.lower() == a.lower():
        print(f"{key} oyida {days[key]} kundan iborat")
        break