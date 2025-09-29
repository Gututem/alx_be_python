# daily_reminder.py

def main():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    if priority == "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    elif priority == "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    elif priority == "low":
        reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    else:
        reminder = f"Invalid priority for task: '{task}'"

    if time_bound == "yes" and priority in ["high", "medium"]:
        reminder += " that requires immediate attention today!"

    print(reminder)


if __name__ == "__main__":
    main()
