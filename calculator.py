while True:
    a = float(input("enter the first number:"))
    b = float(input("enter the second number:"))
    print("choose operation:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    choice = input("enter your choice(1/2/3/4):")
    if choice == "1":
        print(a+b)
    elif choice == "2":
        print(a-b)
    elif choice == "3":
        print(a*b)
    elif choice == "4":
         if b!=0:
             print("a/b")
         else:
             print("cannot divisible by zero")
    else:
          print("invalid operation")
    again =input("do you want to continue? (y/n)")
    if again =="n":
        break
