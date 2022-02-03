#Creating a simple calculator

#Display options to users
print("1 Addition")
print("2 Subtaction")
print("3 Multiplication")
print("4 Division")



def calculator (num1, num2, operation):
    if choice == "1":
        print(num1, "+", num2, "=", (num1 + num2))
 
    elif choice == "2":
        print(num1, "-", num2, "=", (num1 - num2))
 
    elif choice == "3":
        print(num1, "*", num2, "=", (num1 * num2))
     
    elif choice == "4":
        print(num1, "/", num2, "=", (num1 / num2))
     
    else:
        print("invalid choice")




#Users enters choice
choice=input("enter choice: ")

#Enter 2 numbers in which the operation will be performed
first_number = float(input("enter number 1: "))
second_number = float(input("enter number 2: "))



calculator(num1 = first_number,
           num2 = second_number,
           operation = choice)


calculator(num1 = 12,
           num2 = 3,
           operation = 4)

