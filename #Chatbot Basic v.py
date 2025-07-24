import math
import operator as op


def main():
    print(
        "Hello! I am a Chat Bot, If you would like to make a basic calculation write 'calculator'."
        " If you want to exit write 'exit' to end."
    )

    while True:
        user_input = input("You: ").lower()
        if user_input in ["hi", "hello", "hey", "howdy"]:
            print("Chat Bot: Hi there!")

        elif "How are you".lower() in user_input:
            print("Chat Bot: I am a chat Bot, I have no emotions. How are you?")

        elif "good" in user_input:
            print("Chat Bot: Great to hear that!")

        elif "bad" in user_input:
            print("Chat Bot: I'm sorry to hear that, I hope your day gets better.")

        elif user_input in ["what is your name", "whats your name"]:
            print("Chat Bot: I am a chat bot, so I do not have a name.")

        elif user_input in ["thanks", "thank you"]:
            print("Chat Bot: Of course! if you wish to exit write 'exit' to end.")

        elif user_input == "calculator":
            print("loading calculator")
            calculator_mode()  

        elif user_input == "exit":
            print("You have selected to exit.")
            break

        else:
            print("Chat Bot: Sorry I cant help you with that.")     


def calculator_mode():
    
    def addition(x, y):
        return x + y

    def subtraction(x, y):
        return x - y

    def multipication(x, y):
        return x * y

    def division(x, y):
        return x / y

    print("Choose your calculation")
    print("1, to add")
    print("2, to subtract")
    print("3, to multiply")
    print("4, to divide")
    action = input("Which operation?: ")
    if action == "1":
        x_value = int(input("x: "))
        y_value = int(input("y: "))
        answer = addition(x_value, y_value)
        print(answer)
    if action == "2":
        x_value = int(input("x: "))
        y_value = int(input("y: "))
        answer = subtraction(x_value, y_value)
        print(answer)
    if action == "3":
        x_value = int(input("x: "))
        y_value = int(input("y: "))
        answer = multipication(x_value, y_value)  
        print(answer)
    if action == "4":
        x_value = int(input("x: "))
        y_value = int(input("y: "))
        answer = division(x_value, y_value)
        print(answer)


if __name__ == "__main__":
    main()   