"""
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

*Пример:*

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
- 
"""
k = int(input("Введите k"))
a = []
for i in range(0,k*2+1):
    a.append(0)
a[k-1] = a[k+1] = 1
a[k] = 0
for i in range(k+2, k*2+1):
    a[i] = a[i-1] + a[i-2]
for i in range(k-2,-1,-1):
    a[i] = a[i+2] - a[i+1]
print(a)