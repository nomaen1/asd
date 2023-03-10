# Tuple - Кортежи
# it_company = ("GeekTech", "GeekStudio", "MadDevs")
# print(it_company)
# tup = (10, 2.0, True, "Geek")
# print(tup)
# print(it_company.count("GeekTech"))
# print(it_company.index("MadDevs"))

# lst_company = list(it_company)
# print(lst_company)
# lst_company.append("Hapsida")
# print(lst_company)

# it_company = tuple(lst_company)
# print(it_company)

# tup = (10, 33.3, "hello", False, (1, 2, 3, 4), [1, 2, 3])
# print(tup)

# tup = ("Hello",)
# print(type(tup))

# for i in range(10, 20, 2):
#     print(i)

# numbers = [10, 2, 3, 4, 5, 73, 100, 101, 203, 1001, 4403]
# for num in numbers: #итерация   
#     if num % 2 == 0:
#         print(num, "Четный")
#     else:
#         print(num, "Нечетный")

# names = ["Kurmanbek", "Nurbolot", "Atai", "Janysh"]
# for name in names:
#     print("Здраствуйте", name)

# cars = ("BMW", "Mercedes", "Tesla", "Honda")
# for car in cars:
#     print(car)


# geek = "GeekTech"
# for g in geek:
#     print(g)

# num = 23
# for n in num:
#     print(n)

# numbers = [100, 101, 102, 103, 200, 204, "Hello", 1.0, True]
# for n in numbers:
#     if n == 200:
#         print("OK")
#         break
#     print(n)

# nums = []
# for i in range(1, 101):
#     nums.append(i)
# print(nums)

# num1 = 100
# num2 = 20
# while num2 > num1:
#     num1 += 1
#     print(num1)

# n = 0
# while True:
#     n += 1
#     print(n)
#     if n == 10000:
#         print("STOP")
#         break

# import random
# import time
# random_number = random.randint(1000, 9999)
# i = 0
# while True:
#     i += 1
#     if i == random_number:
#         print("Hacked", random_number, "is password")
#         break
#     print("Hacking", i)

# while True:
#     time.sleep(1)
#     print (time.ctime())