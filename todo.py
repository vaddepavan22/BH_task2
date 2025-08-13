# to_do_list_file.py
# Console To-Do List with add/remove/view and file storage

FILENAME = "tasks.txt"
tasks = []  # still using a list in memory

# ===== File Handling =====
def load_tasks():
    """Load tasks from file into the list."""
    try:
        with open(FILENAME, "r") as f:
            for line in f:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass  # no file yet, start empty

def save_tasks():
    """Save all tasks from the list into the file."""
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

# ===== Core Features =====
def add_task():
    title = input("Enter task: ").strip()
    if not title:
        print("Task cannot be empty.")
        return
    tasks.append(title)
    save_tasks()
    print("Task added.")

def remove_task():
    if not tasks:
        print("No tasks to remove.")
        return
    view_tasks()
    try:
        idx = int(input("Enter task number to remove: ")) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            save_tasks()
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def view_tasks():
    if not tasks:
        print("\nNo tasks yet.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

# ===== Menu =====
def main():
    load_tasks()
    while True:
        print("\n=== TO-DO LIST ===")
        print("1) Add Task")
        print("2) Remove Task")
        print("3) View Tasks")
        print("0) Exit")

        choice = input("Choose: ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            view_tasks()
        elif choice == "0":
            print("Thanks for using the To-Do List!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
