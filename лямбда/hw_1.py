def hello(x):
    print(x * x - 10)
hello(10)
#######################

hello = lambda x: x * x - 10
print(hello(10))

#######################

print((lambda x: x * x - 10)(10))