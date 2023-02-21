num = int(input("Введите шестизначное число: "))
digit1 = num // 100000
digit2 = (num // 10000) % 10
digit3 = (num // 1000) % 10
digit4 = (num // 100) % 10
digit5 = (num // 10) % 10
digit6 = num % 10
sum1 = (digit1 + digit2 + digit3)
sum2 = (digit4 + digit5 + digit6)
if sum1 == sum2 : print("yes")
else : print("no")