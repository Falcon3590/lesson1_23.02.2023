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

# class1 = int(input("Укажите сколько учащихся в классе 1: "))
# class2 = int(input("Укажите сколько учащихся в классе 2: "))
# class3 = int(input("Укажите сколько учащихся в классе 3: "))
# print("Наименьшее число парт, которое нужно приобрести для 3х классов", round((class1 + class2 + class3) / 2), 'шт.') # округлил целочисленно в большую сторону 

# 5. Вагоны в электричке пронумерованы натуральными числами, начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с «хвоста»;
# это зависит от того, в какую сторону едет электричка). В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда и обнаружил, что его
# вагон имеет номер j. Он хочет определить, сколько всего вагонов в электричке. Напишите программу, которая будет это делать или сообщать, что без
# дополнительной информации это сделать невозможно.

# i = int(input("Укажите в какой вагон сел Витя: "))
# j = int(input("Укажите в каком вагоне он оказался: "))

# if i == j:
#     print("Нужна доп инфа")
# else:
#     print(f"Кол-во вагонов {i+j-1}")

# 7. Дано натуральное число. Требуется определить, является ли год с данным номером високосным. Если год является високосным, то выведите YES,
# иначе выведите NO. Напомним, что в соответствии с григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100,
# а также если он кратен 400.

# year = int(input("Введите год: "))
# if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
#     print("YAS")
# else:
#   print("NO")
#
# print(year % 4)
# print(year % 100)
# print(year % 400)
