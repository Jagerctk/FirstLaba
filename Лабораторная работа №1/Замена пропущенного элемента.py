numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
v = numbers[0:4]
b = numbers[5:20]
num1 = v + b
summ = sum(num1)/len(numbers)
numbers[4] = summ
print("Измененный список:", numbers)

