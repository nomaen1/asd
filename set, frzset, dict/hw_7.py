# while True:
#     password = []
#     command_1 = input("Введите пароль: ")
#     command_2 = input("Повторите пароль: ")
#     if len(command_1) < 8:
#         print("Слишком короткий!")
#     elif "123" in command_1:
#         print("Слишком легкий пароль")
#     elif command_1 == command_2:
#         print("Пароль создан")
#     password.append(command_1)
#     else:
#         print("Пароли не совпадают")
#         print(password)

password = input("Password: ")
confirm_password = input("Confirm password: ")
passwords = set()
if password != confirm_password:
    print("Различются")
elif len(password) < 8:
    print("Короткий пароль!")
elif "123" in password:
    print("Простой пароль!")
else:
    print("ОК")
    print("Пароль создан")
    passwords.add(password)