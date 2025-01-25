# To-Do List Application

# List to store tasks
tasks = []

# Function to display the menu
def show_menu():
    print("\nTo-Do List Application")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

# Function to view tasks
def view_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nTasks:")
        for i in range(len(task)):
            print(f"{i+1}. {task[i]}")

# Function to add a task
def add_task():1
    task = input("\nEnter the task: ")
    tasks.append(task)
    print("Task added successfully!")

# Function to delete a task
def delete_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("\nEnter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' deleted successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Main Program Loop
while True:
    show_menu()
    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Thank you. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
