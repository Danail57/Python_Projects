N1 = int(input('Enter the first number: '))
N2 = int(input('Enter the second number: '))
operator = input('Enter your operator: + - / *: ')

if operator == "+":
    result = N1 + N2
    print(f"{N1} + {N2} = {result} - {'even' if result % 2 == 0 else 'odd'}")

elif operator == '-':
    result = N1 - N2
    print(f"{N1} - {N2} = {result} - {'even' if result % 2 == 0 else 'odd'}")

elif operator == '*':
    result = N1 * N2
    print(f"{N1} * {N2} = {result} - {'even' if result % 2 == 0 else 'odd'}")

elif operator == '/':
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        result = N1 / N2
        print(f"{N1} / {N2} = {result:.2f}")

elif operator == '%':
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        result = N1 % N2
        print(f"{N1} % {N2} = {result}")
else:
    print(f"Invalid operator: '{operator}'. Please enter one of +, -, *, /: ")

