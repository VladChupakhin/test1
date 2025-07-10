try:
    num1 = int(input("1-ое число: "))
    num2 = int(input("2-ое число: "))
    num3 = int(input("3-ое число: "))
    
    maximum = max(num1, num2, num3)
    minimum = min(num1, num2, num3)
    average = (num1 + num2 + num3) - (minimum + maximum)
    
    print(f"Мин. знач.: {minimum}")
    print(f"Ср. знач.: {average}")
    print(f"Макс. знач.: {maximum}")

except ValueError:
    print("Ошибка: пожалуйста, вводите только целые числа")