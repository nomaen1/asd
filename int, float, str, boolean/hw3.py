# 3)Какие переменные можно складывать(без изменения их типа данных) и что при этом
# получится?
a = 589
b = 932.901
c = 'Hello world'
d = '892.01'

print(c + " " + d)
print(a + b)
# a и b (int + float) - верно
# c и d (str + str) - верно
# a + c и d (int + str) - неверно
# b + c и d (float + str) - неверно