# Simple calculator test

print("Choose the operation:")
first = float(input())
operator = input()
second = float(input())
if operator == '+':
    result = first + second
elif operator == '-':
    result = first - second
elif operator == '*' or operator == 'x':
    result = first * second
elif operator == '/' or operator == ':':
    result = first / second
else:
    result = "undefined"
print(str(first) + " " + operator + " " + str(second) + " = " + str(result))
