FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def get_valid_temperature(prompt):
    while True:
        user_input = input(prompt).strip()
        try:
            temp = float(user_input)
            return temp
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

def get_temperature_unit(prompt):
    while True:
        unit = input(prompt).strip().upper()
        if unit in ["C", "F"]:
            return unit
        print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")

def main():
    temperature = get_valid_temperature("Enter the temperature to convert: ")
    unit = get_temperature_unit("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    if unit == "C":
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted}°F")
    else:
        converted = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted}°C")

if __name__ == "__main__":
    main()
