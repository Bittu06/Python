def goodbye(name, ending="Thank you"):
    print(f"Goodbye, {name}")
    print(ending)

user_name1 = input("Enter your name:")
ending = input("Enter your message:")
user_name2 = input("Enter your name:")
goodbye(user_name1, ending)    # This will print the message
goodbye(user_name2) # This will print the default message

