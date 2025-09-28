from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time in YYYY-MM-DD HH:MM:SS format."""
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(current_date, days_to_add):
    """Calculate and display the date after adding specified days."""
    future_date = current_date + timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def get_valid_integer(prompt):
    """Keep asking the user until a valid integer is entered."""
    while True:
        user_input = input(prompt).strip()
        try:
            value = int(user_input)
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    current_date = display_current_datetime()
    
    days_input = get_valid_integer("Enter the number of days to add to the current date: ")
    calculate_future_date(current_date, days_input)

if __name__ == "__main__":
    main()
