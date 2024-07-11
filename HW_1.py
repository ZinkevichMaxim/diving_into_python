BIG_LEAP_YEAR = 4
LARGE_NOT_BIG_YEAR = 100
SMALL_LEAP_YEAR = 4
MULTIPLE = 0
REFORM = 1582

year = int(input("Введите год: "))
if year < REFORM:
    result = "Год до ввода Григорианского календаря"
elif year % BIG_LEAP_YEAR:
    result = f"Год {year} високосный"
elif year % LARGE_NOT_BIG_YEAR:
    result = f"Год {year} не високосный"
elif year % SMALL_LEAP_YEAR:
    result = f"Год {year} високосный"
else:
    result = f"Год {year} не високосный"
print(result)
