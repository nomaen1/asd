while True:
    age = int(input("Введите ваш возраст: "))
    if age >= 18:
        print("Доступ разрешен")
        break
    else:
        print("Извините, пользование данным ресурсом только с 18 лет")