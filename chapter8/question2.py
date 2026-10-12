# c=5*(f-32)/9
i = int(input("Enter the temperature in Fahrenheit: "))


def fahrenheit_to_celsius(f):
    c = 5 * (f - 32) / 9
    return print(f"The temperature in Celsius is: {c}")

fahrenheit_to_celsius(i)
