# Simple Calculator Program
# Prompt the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prompt the user to input an operation choice
print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")
print("6. Floor division (//)")
print("7. Power (**)")
oper = int(input("Enter your choice (1/2/3/4/5/6/7): "))

# Perform the calculation based on the operation choice
match oper:
    case 1:
        result = num1 + num2
        print("num1 + num2 = result")
        print(f"{num1} + {num2} = {result}")
    case 2:
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    case 3:
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    case 4:
        if num2!= 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed!")
    case 5:
        result = num1  % num2
        print(f"{num1} % {num2} = {result}") 
    case 6:
        if num2 !=0:
            result = num1 // num2
            print(f"{num1} // {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed!")
    case 7:
        result = num1 ** num2
        print(f"{num1} ** {num2} = {result}")
        
    case _:
        print("Error: Invalid operation choice!")

        