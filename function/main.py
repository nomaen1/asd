# # Functions
# def hello_geektech():
#     print("Hello World")
#     print("GeekTech")
# hello_geektech()

# def add():
#     print(111 + 111)
# add()
# len()


# def add(num1, num2):
#     print(num1 + num2)
# add(10, 30)
# add(10, 10)
# add(5, 2)
# add(2, 2, 3)

# def mult(num1:int, num2:int) -> int:
#     print(num1 * num2)
# mult(10, 10)
# mult(20.0, 10.0)

# def div(num1 : int = 1, num2 : int = 1) -> float:
#     print(num1 / num2)
# div(40, 20)
# div()
# div(20)
# div(num2=40, num1=10)

# def avg(lst: list) ->float:
#     print(sum(lst) / len(lst))
# numbers = [1, 10, 20, 30, 40, 50 ,60, 70, 80, 90, 100]
# nums = [1, 100, 200, 300, 500, 1000, 5000, 10000]
# avg(numbers)
# # avg(nums)

# def add(num1:int, num2:int) -> int:
#     print("Ответ:", num1 + num2)
    
# def sub(num1:int, num2:int) -> int:
#     print("Ответ:", num1 - num2)
    
# def mult(num1:int, num2:int) -> int:
#     print("Ответ:", num1 * num2)
    
# def div(num1:int, num2:int) -> float:
#     print("Ответ:", num1 / num2)

# def main(num1:int, num2:int, operator:str) -> int:
#     if operator == "+":
#         add(num1, num2)
#     elif operator == "-":
#         sub(num1, num2)
#     elif operator == "*":
#         mult(num1, num2)
#     elif operator == "/":
#         div(num1, num2)
#     else:
#         print("ERROR")
# main(20, 30, "+")
# main(10, 5, "-")
# main(20, 5, "*")
# main(40, 8, "/")

# def welcome(name: str) -> str:
#     return f"Здраствуйте {name}"
# print(welcome("Janysh"))

# def info_about_me(name, surname, age,  address, language, date_of_birth):
#     print(f"""Всем привет! Меня зовут {name}, а фамилия {surname}. Мне {age} лет,
#     Я живу в {address} и я изучаю язык {language}. Мое день рождение {date_of_birth}""")
# info_about_me("Жаныш", "Тыныбеков", 18, "C.Ибраимова", "Python", "20 ноября")

#Исключения
# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print("Деление на ноль невозможно")

# try:
#     print(10 +"10")
# except TypeError:
#     print("TypeError: неподдерживаемые типа операндов для + : 'int' и 'str'")

# try:
#     print("Hello World")
#     print(10 / 0)
#     print(10 + "5")
#     print(10 + 10)
# except:
#     print("Error")

# raise ZeroDivisionError("Hello World")

# try:
#     print(True + "False")
# except:
#     print("Error")
# finally:
#     print("В итоге я сработаю")

print('hello')