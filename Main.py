from ToDoList import todoList

print("Welcome to the ToDoList App")

todoList = todoList()

while True:
    print("\nPlease select an option")
    print("""
    1. Add Task
    2. View Task
    3. Delete Task
    4. Update Task
    5. Save Task
    6. Load Task
    7. Search Task
    8. Check Overdue Task
    9. Exit""")

    option = int(input("Enter your option: "))

    if option == 1:
        print("Adding Task to the List...")
        taskname = input("\nEnter Task Name: ")
        date = input("\nEnter DeadLine in format YY-MM-DDDD: ")
        description = input("\nEnter Description of this Task: ")
        priority = input("\nEnter Priority of Task (Low, Medium, High): ")
        todoList.addTask(taskname, date, description, status = "Incomplete", priority = priority)
        todoList.viewTask()

    elif option == 2:
        print("Showing Task in the List...")
        todoList.viewTask()

    elif option == 3:
        print("Deleting a Task from the List...")
        taskname = input("\nEnter Task Name: ")
        todoList.deleteTask(taskname)

    elif option == 4:
        print("Updating a Task in the List...")
        todoList.viewTask()
        taskname = input("\nEnter the task name that you want to update: ")
        todoList.updateTask(taskname)

    elif option == 5:
        print("Saving Task to a CSV file...")
        todoList.saveTask()

    elif option == 6:
        print("Loading Task from task.csv file...")
        todoList.loadTask()

    elif option == 7:
        print("Searching Task in the List...")
        taskname = input("\nEnter Task Name:")
        todoList.searchTask(taskname)

    elif option == 8:
        print("Checking Overdue Task in the List...")
        todoList.overDueTask()

    elif option == 9:
        print("Thank you for using ToDoList App")
        break

    else:
        print("Invalid option, please try again")