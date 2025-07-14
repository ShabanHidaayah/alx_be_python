# Get user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Generate the reminder message
if time_bound == "yes":
    print(f"\nReminder: '{task}' is a {priority} priority task that requires immediate attention today!")
else:
    if priority == "low":
        print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.")
    else:
        print(f"\nReminder: '{task}' is a {priority} priority task.")

# Required success message
print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
print("\n🚀 Click here to tweet! 🚀")