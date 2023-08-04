# To-Do List

tasks = []

def show_menu():
    print("Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

def view_tasks():
    print("Tasks:")
    for index, task_info in enumerate(tasks, 1):
        status = "Completed" if task_info["completed"] else "Not Completed"
        print(f"{index}. {task_info['task']} - {status}")

def mark_completed():
    view_tasks()
    task_index = int(input("Enter the number of the task you want to mark as completed: ")) - 1

    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number!")

def delete_task():
    view_tasks()
    task_index = int(input("Enter the number of the task you want to delete: ")) - 1

    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        print("Task deleted successfully!")
    else:
        print("Invalid task number!")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
