from random import randint
import time

"""
Задача 3 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
 (Теорема Де Моргана) . Но теперь количество предикатов не три, а генерируется случайным образом от 5 до 25, 
 сами значения предикатов случайные, проверяем это утверждение 100 раз, с помощью модуля time выводим на экран , 
 сколько времени отработала программа. 
В конце вывести результат проверки истинности этого утверждения.
"""
def Check_equality(array):
    res1 = array[0]
    res2 = not array[0]
    for i in range(1,len(array)-1):
        res1 = res1 or array[i]
        res2 = res2 and not array[i]
    res1 = not res1
    if res1 == res2: 
        return(True)
    else:
        return(False)


def Generate():
    N = randint(5,26)
    array = []
    for i in range(0,N-1):
       temp = randint(0,1)
       if temp == 0:
           array.append(False)
       else:
           array.append(True)
    return array


start = time.time()


for i in range(1,100):
    res = True
    if Check_equality(Generate()) == False:
        res = False
        break

stop = time.time()
print(stop - start)
print(res)