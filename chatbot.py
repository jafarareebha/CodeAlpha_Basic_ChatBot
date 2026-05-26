def Chatbot():
    UserInput = input("You:").lower()
    while UserInput!="bye":
        if UserInput=="hello" or UserInput=="hi":
            print("Hi")
        elif UserInput=="how are you":
            print("I'm fine! Thanks")
        elif UserInput=="bye":
            print("Goodbye!")
            exit()
        else:
            print("Sorry, I don't understand.")
        UserInput = input("You:").lower()
    print("Goodbye!")
Chatbot()