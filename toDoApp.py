# toDoApp.py
"""Simple ToDo CLI app — UI improved version"""

# ==============================
# 📘 Documentation
# - addtask(task): adds a new task
# - showTasks(): shows all tasks
# - removetask(tasknumber): removes a task using its number
# - main(): runs the menu loop
# ==============================

# list to store all tasks
tasks = []


def addtask(task):
    # function to add a new task to the list
    tasks.append(task)
    print("✅ Task added!")


def showTasks():
    # function to display all tasks
    if len(tasks) == 0:  # if no tasks yet
        print("⚠️  No tasks yet.")
    else:
        print("\n📋 Your Tasks:")
        # loop through tasks and print with numbers
        for i in range(len(tasks)):
            print(f"   {i+1}. {tasks[i]}")


def removetask(tasknumber):
    # function to remove a task by its number
    try:
        removed = tasks.pop(tasknumber - 1)  # adjust index (1-based)
        print(f"❌ Task removed: {removed}")
    except IndexError:  # if number is invalid
        print("⚠️  Invalid task number.")


def main():
    # main function to run the ToDo menu
    print("=" * 40)
    print("   📌 Welcome to the ToDo App 📌   ")
    print("=" * 40)

    while True:  # loop until user exits
        print("\nPlease choose an option:")
        print("[1] ➕ Add Task")
        print("[2] 📂 Show Tasks")
        print("[3] ❌ Remove Task")
        print("[4] 🚪 Exit")
        print("-" * 40)

        # ask for user choice
        ch = input("Enter choice (1-4): ").strip()

        if ch == "1":
            # add new task
            t = input("Enter a new task: ")
            addtask(t)
        elif ch == "2":
            # show all tasks
            showTasks()
        elif ch == "3":
            # check if there are tasks to remove
            if not tasks:
                print("⚠️  No tasks to remove.")
                continue
            n = input("Enter task number to remove: ")
            # make sure input is a number
            if not n.isdigit():
                print("⚠️  Please enter a valid number.")
                continue
            removetask(int(n))
        elif ch == "4":
            # exit the program
            print("\n👋 Goodbye! Thanks for using ToDo App.")
            print("=" * 40)
            break
        else:
            # if input is invalid
            print("⚠️  Invalid choice, try again.")


if __name__ == "__main__":
    # run the program
    try:
        main()
    except KeyboardInterrupt:  # handle Ctrl+C
        print("\n\n👋 Goodbye! (Exited with Ctrl+C)")
        print("=" * 40)
