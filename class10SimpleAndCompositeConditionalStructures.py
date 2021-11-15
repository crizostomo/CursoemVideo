time = int(input("How old is your car? "))
#if time <=3:
#    print("new car")
#else:
#    print("old car")
print("new car" if time<=3 else "old car")
print("---End---")

name = str(input("What is your name? "))
if name == "Diogo":
    print("Great name!")
else:
    print("Your name is ok")
print("Good morning {}".format(name))