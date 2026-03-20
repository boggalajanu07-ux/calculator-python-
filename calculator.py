while True:
    a = int(input("enter the first number:"))
    b = int(input("enter the second number:"))
    op=input("enter the operation (+,-,*,/):")
    if op=="+":
        print(a+b)
    elif op=="-":
        print(a-b)
    elif op=="*":
        print(a*b)
    elif op=="/":
        print(a/b)
    elif op=="/":
         if b==0:
             print("cannot divided by zero")
         else:
             print(a/b)
    else:
          print("invalid operation")
    choice=input("do you want to continue? (y/n)")
    if choice=="n":
        break
