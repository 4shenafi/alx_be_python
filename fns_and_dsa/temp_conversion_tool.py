FAHRENHEIT_TO_CELSIUS_FACTOR = float(5 / 9)
CELSIUS_TO_FAHRENHEIT_FACTOR = float(9 / 5)

def convert_to_celsius(fahrenheit):
    fahrenheit = float(fahrenheit)
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f'{fahrenheit}°F is {celsius}°C')

def convert_to_fahrenheit(celsius):
    celsius = float(celsius)
    fahrenheit = (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32
    print(f'{celsius}°C is {fahrenheit}°F')

def main():
    try:
        temp = float(input("Enter the temperature to convert: "))
        choice = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if choice == 'C':
            convert_to_fahrenheit(temp)
        elif choice == 'F':
            convert_to_celsius(temp)
        else:
            print("Invalid Choice!")
    except ValueError:
        print("Invalid input! Please enter a numeric temperature.")

if __name__ == "__main__":
    main()
