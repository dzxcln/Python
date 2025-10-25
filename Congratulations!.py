name = input("Enter your name: ")
achievement = input("Enter your achievement: ")

message = "Congratulations, " + name.title() + "! " + \
          "You have successfully completed " + achievement.upper() + "!"

decor = "*" * len(message)

print("\n" + decor)
print(message)
print(decor)

print("\nFun facts about your message:")
print("Message length:", len(message))

