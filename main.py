# 1. За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# **Input:**
# n = 700
# m = 750
# **Output:**

# import math 
# n = float(input("Укажите сколько км машина проезжает за день: "))
# m = float(input("Укажите длину маршрута в км: "))
# print(math.ceil(m / n), "дня потребуется на такой маршрут")


# 2
# 3. В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. За каждой партой может сидеть два учащихся.
#  Известно количество учащихся в каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.
# **Input:**
# 20
# 21
# 22
# **Output:**
# 32

class1 = int(input("Укажите сколько учащихся в классе 1: "))
class2 = int(input("Укажите сколько учащихся в классе 2: "))
class3 = int(input("Укажите сколько учащихся в классе 3: "))
print("Наименьшее число парт, которое нужно приобрести для 3х классов", round((class1 + class2 + class3) / 2), 'шт.') # округлил целочисленно в большую сторону 