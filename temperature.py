def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


# Main program
if __name__ == "__main__":
    celsius = 25
    print("Fahrenheit:", celsius_to_fahrenheit(celsius))
