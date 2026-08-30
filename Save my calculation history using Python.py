History_file = "history.txt"
def show_history():
    file=open(History_file, "r")
    line=file.readlines()
    if len(line)==0:
        print("No history found")
    else:
     for char in line:
         print(char)
def clear_history():
    file=open(History_file, "w")
    file.close()
    print("History cleared successfully")
def save_history(user_input,result):
    file=open(History_file, "a")
    file.write(user_input + " = " + str(result) + "\n")
    file.close()
def calculate(user_input):
    parts=user_input.split()
    if len(parts)!=3:
        print("Invalid input")
    else:
        num1=float(parts[0])
        operator=parts[1]
        num2=float(parts[2])
        if operator=="+":
            result= num1 + num2
        elif operator=="-":
            result= num1 - num2
        elif operator=="*":
            result= num1 * num2
        elif operator=="/":
            if num2==0:
                print("Division by zero is not allowed")
                return
            result= num1/num2
        else:
            print("Invalid operator")
            return
        print("Result:", result)
        save_history(user_input, result)
    
print("1.Show history")
print("2.Clear history")
print("3.Calculate")
print("4.Exit")

def main():
    while True:
        choice=input("Enter your choice: ")
        if choice=="1":
            show_history()
        elif choice=="2":
            clear_history()
        elif choice=="3":
            user_input=input("Enter the expression (e.g., 5 + 3):")
            calculate(user_input)
        elif choice=="4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
main()
