def chatbot():
    while True:
        text=input("Введите что-то:")
        if text.find("?")>=0:
            print("Конечно!")
        elif text.find("!")>=0:
            print("Успокойся")
        elif text == "":
            print("Как классно, когда ты молчишь. Продолжай в том же духе!")
        else:
            print("Ну и что")
chatbot()