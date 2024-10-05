def add(a,b):
    ans = a + b
    print("add=", ans)

def sub(a,b) :
    ans = a - b
    print("ans=",ans)

def mul(a,b) :
    ans = a * b
    print("ans=",ans)

def div(a,b) :
    ans = a / b
    print("ans=",ans)
while True:
    ch = int(input("\n\nENTER CHOICE: \n1.Addition\t        2.Subtraction\n3.Multiplication\t4.Division\n5 EXIT"))
    if ch==1:
        fn= int(input("Enter First Number:"))
        sn= int(input("Enter Second Number:"))
        add(fn,sn)
    elif ch==2:
        fn= int(input("Enter First Number:"))
        sn= int(input("Enter Second Number:"))
        sub(fn,sn)
        
    elif ch==3:
        fn= int(input("Enter First Number:"))
        sn= int(input("Enter Second Number:"))
        mul(fn,sn)

    elif ch==4:
        fn= int(input("Enter First Number:"))
        sn= int(input("Enter Second Number:"))
        div(fn,sn)

    elif ch==5:
        print("Exiting...")
        break

    else:
        print("INVALID CHOICE")
        
