is_year_leap=int(input("Введите год (Например, 2025): "))

remainder = is_year_leap % 4

if remainder == 0:
    print("год", is_year_leap, ": True")

else:
    print("год", is_year_leap, ": False")