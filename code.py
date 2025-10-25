HISTORY_FILE="history.txt"

def show_history():
    file=open(HISTORY_FILE,"r")
    lines=file.readlines()
    if len(lines)==0:
        print("No history file!")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file=open(HISTORY_FILE,"w")
    file.close()
    print("HISTORY CLEARED")

def save_to_history(equation,result):
    file=open(HISTORY_FILE,"a")
    file.write(equation+ "=" + str(result)+ "\n")
    file.close()

def calculate(user_input):
    parts=user_input
    if len(parts)!=3:
        print("Invalid input.Use format:number operator(eg. 8+8)")
        return

    num1=float(parts[0])
    op=parts[1]
    num2=float(parts[2])

    if op=="+":
        result=num1+num2
    elif op=="-":
        result=num1-num2
    elif op=="*":
        result=num1*num2
    elif op=="/":
        if num2==0:
            print("cannot divide by zero")
        result=num1/num2
    else:
        print("Invalid operator.USE ONLY + - * /.")
        return

    if int(result)==result:
        result=int(result)
    print("Result:",result)
    save_to_history(user_input, result)

def main():
    print("---SMPLE CALCULATOR(type history,clear or exit)")
    while True:
        user_input=input("enter calculation(+ - * /) or command(history,clear,exit)")
        if user_input=="exit":
            print("Good Bye")
            break
        elif user_input=="history":
            show_history()
        elif user_input=="clear":
            clear_history()
        else:
            calculate(user_input)

if __name__ == "__main__":
    main()



