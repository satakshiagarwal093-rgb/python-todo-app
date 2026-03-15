tasks = []
try:
    with open("tasks.txt", "r") as file:
        tasks = file.read().splitlines()
except FileNotFoundError:
    pass
while True:
    print("\nTo do List")
    print("1. View Tasks")
    print("2. Add Tasks")
    print("3. Delete Task")
    print("4. Exit")
    choice = input("Enter Choice: ")
    if choice == "1":
        if len(tasks) == 0:
            print("No Tasks Available")
        else:
            for task in tasks:
                print(task)
    elif choice == "2":
        task = input("Enter task: ")
        tasks.append(task)
        with open("tasks.txt", "a") as file:
                file.write(task + "\n")
        print("Task Added")
    elif choice == "3":
        task = input ("Enter the delete task: ")
        if task in tasks:
            tasks.remove(task)
            print("Task Deleted")
        else:
            print("Task not found")
    elif choice == "4":
        print("GoodBye!!")
        break
