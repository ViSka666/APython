mount= input("Введите месяц: ")

def mount_to_season(mount):
    if mount in [12, 1, 2]:
        return "Зима"
   
    elif mount in [3, 4, 5]:
        return "Весна"
    
    elif mount in [6, 7, 8]:
        return "Лето"   

    elif mount in [9, 10, 11]:
        return "Осень"

    else:
        return "Неверный номер месяца"  
    
season= mount_to_season(int(mount))
print(season) 