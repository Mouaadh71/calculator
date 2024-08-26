while True :

    def add(a,b):
        return a+b
    def subtruct(a,b):
        return a-b
    def multeplay(a,b):
        return a*b
    def divaid(a,b):
        return a/b
    def calculator():
        print("1 add\n2 subtruct \n3 multeplay \n4 divaid")
        while True :
            Operation = input("choose the Operation : ")
            if Operation == "add"or"divaid"or"multeplay"or"subtruct":
                break
            else :
                print("invalid Operation")
        while True :
            first_num = int(input("choose the first number : "))
            second_num = int(input("choose the second number : "))
            if second_num == 0 and Operation == "divaid":
                print("you can't divaid by 0")
            else :
                break 

        if Operation =="add" :
            ruselt = add(first_num,second_num)
        elif Operation == "subtruct" :
            ruselt = subtruct(first_num,second_num)
        elif Operation == "multeplay" :
            ruselt = multeplay(first_num,second_num)
        elif Operation == "divaid" :
            ruselt = divaid(first_num,second_num)
        print(ruselt)

    calculator()
