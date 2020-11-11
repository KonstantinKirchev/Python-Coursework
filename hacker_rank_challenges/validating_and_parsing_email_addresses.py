import email.utils
import re 
  
regex = "^[a-zA-Z][a-zA-Z0-9-._]+[@][a-zA-Z]+[.][a-zA-Z]{1,3}$"

def check(email):  
    if(re.search(regex,email)):  
        return True           
    return False

n = int(input())

if 0 < n < 100:
    for x in range(n):
        emailInput = input()
        temp = email.utils.parseaddr(emailInput)
        if(check(temp[1])):
            result = email.utils.formataddr(temp)
            print(result)