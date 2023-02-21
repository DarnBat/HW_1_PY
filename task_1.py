num = int(input("Введите трехзначное число: "))
digit1 = num // 100  
digit2 = (num // 10) % 10 
digit3 = num % 10 
sum_digits = digit1 + digit2 + digit3
print("Сумма цифр числа", num, "равна", sum_digits)