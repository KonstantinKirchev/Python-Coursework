n = int(input().strip())

if 1 <= n <= 10:
    for x in range(n):
        num = input()
        if 2 <= len(num) <=15:
            if (num[0] == "7" or num[0] == "8" or num[0] == "9") and len(num) == 10:
                try : 
                    integer = int(num)
                    print("YES")
                except ValueError  :
                    print("NO")
            else :
                print("NO")
