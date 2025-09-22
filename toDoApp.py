# toDoApp.py

tasks = []

def addtask(task):
    tasks.append(task)
    print("Task added!")

def showTasks():
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])

def removetask(tasknumber):
    if 1 <= tasknumber <= len(tasks):   # validate input
        tasks.pop(tasknumber - 1)       # adjust for 0-based index
        print("Task removed!")
    else:
        print("Invalid task number!")

def main():
    while True:
        print("\n--- To-Do App ---")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        
        ch = input("Enter choice: ").strip()
        
        if ch == "1":
            t = input("Enter task: ").strip()
            if t:
                addtask(t)
            else:
                print("Task cannot be empty!")
        elif ch == "2":
            showTasks()
        elif ch == "3":
            if len(tasks) == 0:
                print("No tasks to remove.")
            else:
                try:
                    n = int(input("Enter task no. to remove: "))
                    removetask(n)
                except ValueError:
                    print("Please enter a valid number!")
        elif ch == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Wrong choice!")

main()
