print("Hello and Welcome to the Chatbox")
name = input("Enter Name: ")
age = input("Enter age: ")
print("your name is "+ name + " and you are "+ age + " years old")
print("want to to math? lets do it!")
difficulty = input("do you want easy or hard? ")
if (difficulty == "easy"):
    answer = input("what is one plus one: ") 
    if (answer == "2"):
        print("yes")
    else:
        print("aw man you lost on easy")
    print("-------")
else:
    answer2 = input("what is 6 times 4: ")
    if (answer2 == "24"):
        print("wow you are good at math!")
    else:
        print("nope")
    print("-------")
    print("Good by " +name+ " and have a good day!!")
