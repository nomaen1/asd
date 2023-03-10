import random
def rand(count):
    language = ["Python", "Java", "Kotlin", "JavaScript", "C#","RUBY"]
    lang = []
    for i in language:
        lang.append(i)
    for n in range(count):
        res = ""
        for l in range(count):
            res += random.choice(lang)
        with open('hw_1.txt', 'w') as g:
            g.write(res)
rand(1)        