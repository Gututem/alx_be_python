# control-flow/daily_reminder.py

def main():
    while True:
        task = input("Enter your task: ").strip()
        priority = input("Priority (high/medium/low): ").strip().lower()
        time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

        reminder = ""

        # Replacing match-case with if-elif for compatibility
        if priority == "high":
            reminder = f"'{task}' is a high priority task"
        elif priority == "medium":
            reminder = f"'{task}' is a medium priority task"
        elif priority == "low":
            reminder = f"'{task}' is a low priority task"
        else:
            print("Invalid priority. Please enter high, medium, or low.")
            continue

        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        elif time_bound == "no":
            reminder = f"Note: {reminder}. Consider completing it when you have free time."
        else:
            print("Invalid input for time-bound. Please enter yes or no.")
            continue

        print(f"\nReminder: {reminder}")
        break


if __name__ == "__main__":
    main()
