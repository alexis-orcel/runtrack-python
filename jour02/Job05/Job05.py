def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "%":
        return num1 % num2
    else:
        return "Invalid operator"
result = calcule(6, "+", 2)
print(result)

result = calcule(3, "-", 4)
print(result)

result = calcule(3, "*", 9)
print(result)

result = calcule(3, "/", 2)
print(result)

result = calcule(10, "%", 8)
print(result)
