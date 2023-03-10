temp = int(input("Какая температура на улице? "))
if temp < int(-30):
    print("Там так холодно, лучше дома сиди!")
elif temp > int(-30) and temp < 0:
    print("Холодновато. Оденься потеплее!")
elif temp >= 0 and temp < 15:
    print("Прохладно. Куртку накинь!")
elif temp >= 15 and temp < 30:
    print("Тепло. Иди погуляй в парке!")
elif temp >= 30 and temp < 50:
    print("Ого, как жарко!")
elif temp >= 50:
    print("Там такая жара, лучше сиди дома!")
else:
    print("Ошибка!")