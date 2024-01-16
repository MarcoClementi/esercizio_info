num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

num1 = int(num1)
num2 = int(num2)

if num1 % 2 == 0 and num2 % 2 == 0:
    print("Both numbers are even")
elif num1 % 2 != 0 and num2 % 2 != 0:
    print("Both numbers are odd")
else:
    print("One number is even and one number is odd")