def is_leap(year) -> bool:
    leap = False
    
    if 1900 <= year <= 10**5:
        if year % 4 == 0:
            leap = True
            if year % 100 == 0:
                leap = False
                if year % 400 == 0:
                    leap = True
        return leap
    
    return leap

year = int(input().strip())
print(is_leap(year))