a = float(input("Enter first number: "))    # 1
b = float(input("Enter second number: "))   # 2

print("Addition:", a + b)                   # 3
print("Subtraction:", a - b)                # 4
print("Multiplication:", a * b)             # 5

if b != 0:                                  # 6
    print("Division:", a / b)               # 7
else:                                       # 8
    print("Cannot divide by zero.")         # 9
#new change
print("Done!")                              # 10
print("Exponentiation:", a ** b)         # 11
print("Modulo:", a % b)                  # 12
import math                              # 13
print("Square root of first number:", math.sqrt(a))  # 14
print("Absolute difference:", abs(a - b))            # 15
