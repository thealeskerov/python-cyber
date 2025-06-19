# Simple console-based To-Do list application

tasks = []  # List to store tasks as dictionaries

def show_menu():
    print("\nTo-Do List Options:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Mark task as done")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        for i, task in enumerate(tasks):
            status = "✔" if task["done"] else "✘"
            print(f"{i+1}. [{status}] {task['task']}")

def add_task():
    new_task = input("Enter new task: ")
    tasks.append({"task": new_task, "done": False})
    print("Task added.")

def delete_task():
    view_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        tasks.pop(index)
        print("Task deleted.")
    except:
        print("Invalid number.")

def mark_done():
    view_tasks()
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        tasks[index]["done"] = True
        print("Task marked as done.")
    except:
        print("Invalid number.")

# Main program loop
while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        mark_done()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
