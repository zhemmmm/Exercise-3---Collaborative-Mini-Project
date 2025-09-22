# toDoApp.py
"""Simple ToDo CLI app — UI improved version"""

tasks = []

def addtask(task):
    tasks.append(task)
    print("✅ Task added!")

def showTasks():
    if len(tasks) == 0:
        print("⚠️  No tasks yet.")
    else:
        print("\n📋 Your Tasks:")
        for i in range(len(tasks)):
            print(f"   {i+1}. {tasks[i]}")

def removetask(tasknumber):
    try:
        removed = tasks.pop(tasknumber - 1)  # fixed to 1-based index
        print(f"❌ Task removed: {removed}")
    except IndexError:
        print("⚠️  Invalid task number.")

def main():
    print("=" * 40)
    print("   📌 Welcome to the ToDo App 📌   ")
    print("=" * 40)

    while True:
        print("\nPlease choose an option:")
        print("[1] ➕ Add Task")
        print("[2] 📂 Show Tasks")
        print("[3] ❌ Remove Task")
        print("[4] 🚪 Exit")
        print("-" * 40)

        ch = input("Enter choice (1-4): ").strip()

        if ch == "1":
            t = input("Enter a new task: ")
            addtask(t)
        elif ch == "2":
            showTasks()
        elif ch == "3":
            if not tasks:
                print("⚠️  No tasks to remove.")
                continue
            n = input("Enter task number to remove: ")
            if not n.isdigit():
                print("⚠️  Please enter a valid number.")
                continue
            removetask(int(n))
        elif ch == "4":
            print("\n👋 Goodbye! Thanks for using ToDo App.")
            print("=" * 40)
            break
        else:
            print("⚠️  Invalid choice, try again.")

if __name__ == "__main__":
    main()
