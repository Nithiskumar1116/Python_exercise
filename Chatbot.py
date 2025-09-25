while True:
    user = input("You: ").lower()
    if user in ["bye", "salut", "tata"]:
        print("Good Bye!!")
        break
    elif user in ["hy", "hello", "hai", "hi"]:
        print("Hello!!")
    elif user in ["bonjour"]:
        print("Bonjour!! Comment ça va??")
    elif user in ["how are you", "are you doing well"]:
        print("I am Fine!! and you?")
    elif user in ["comment ca va"]:
        print("Ça va bien!! et toi??")
    elif user in ["Thank you","Thanks"]:
        print("Thank you")
    elif user in ["Merci"]:
        print("Merci Beaucoup")
    else:
        print("Not Trained")