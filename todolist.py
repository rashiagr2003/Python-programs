# Simple Daily Task Manager

# Initialize our three lists
daily_tasks = []
completed_tasks = []
incomplete_tasks = []

# Main program starts here
print("Welcome to Simple Daily Task Manager!")

while True:
    # Display menu options
    print("\n--- TASK MANAGER ---")
    print("1. Add a new task")
    print("2. Mark task as completed")
    print("3. Mark task as incomplete")
    print("4. Show all tasks")
    print("5. End day review")
    print("6. Exit")
    
    # Get user choice
    choice = input("Choose an option (1-6): ")
    
    # Option 1: Add a task to daily tasks
    if choice == '1':
        task = input("Enter task: ")
        daily_tasks.append(task)
        print(f"Added: {task}")
    
    # Option 2: Move a task from daily to completed
    elif choice == '2':
        if not daily_tasks:
            print("No tasks to complete.")
        else:
            # Show current daily tasks
            print("\nYour daily tasks:")
            for i, task in enumerate(daily_tasks, 1):
                print(f"{i}. {task}")
            
            # Get task number
            num = input("Enter task number to mark as completed: ")
            try:
                num = int(num)
                if 1 <= num <= len(daily_tasks):
                    # Move task from daily to completed
                    completed_task = daily_tasks.pop(num-1)
                    completed_tasks.append(completed_task)
                    print(f"Completed: {completed_task}")
                else:
                    print("Invalid task number.")
            except:
                print("Please enter a number.")
    
    # Option 3: Move a task from daily to incomplete
    elif choice == '3':
        if not daily_tasks:
            print("No tasks to mark as incomplete.")
        else:
            # Show current daily tasks
            print("\nYour daily tasks:")
            for i, task in enumerate(daily_tasks, 1):
                print(f"{i}. {task}")
            
            # Get task number
            num = input("Enter task number to mark as incomplete: ")
            try:
                num = int(num)
                if 1 <= num <= len(daily_tasks):
                    # Move task from daily to incomplete
                    incomplete_task = daily_tasks.pop(num-1)
                    incomplete_tasks.append(incomplete_task)
                    print(f"Marked as incomplete: {incomplete_task}")
                else:
                    print("Invalid task number.")
            except:
                print("Please enter a number.")
    
    # Option 4: Show all tasks in all lists
    elif choice == '4':
        print("\n----- TASKS -----")
        print("Daily Tasks:")
        if daily_tasks:
            for i, task in enumerate(daily_tasks, 1):
                print(f"{i}. {task}")
        else:
            print("  None")
        
        print("\nCompleted Tasks:")
        if completed_tasks:
            for i, task in enumerate(completed_tasks, 1):
                print(f"{i}. {task}")
        else:
            print("  None")
        
        print("\nIncomplete Tasks:")
        if incomplete_tasks:
            for i, task in enumerate(incomplete_tasks, 1):
                print(f"{i}. {task}")
        else:
            print("  None")
    
    # Option 5: End day review - move all remaining daily tasks to incomplete
    elif choice == '5':
        if not daily_tasks:
            print("No tasks left for end-of-day review.")
        else:
            print("Moving all remaining tasks to incomplete list:")
            for task in daily_tasks:
                print(f"- {task}")
                incomplete_tasks.append(task)
            daily_tasks.clear()  # Empty the daily tasks list
            print("End-of-day review complete.")
    
    # Option 6: Exit the program
    elif choice == '6':
        print("Thank you for using Task Manager. Goodbye!")
        break
    
    # Handle invalid choices
    else:
        print("Invalid choice. Please try again.")