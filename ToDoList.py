from tabulate import tabulate
from datetime import datetime

class todoList:

    def __init__(self):
        self.name = []
        self.date = []
        self.description = []
        self.status = []
        self.priority = []

    def addTask(self, taskname, date, description, status = "Incomplete", priority = "Low"):
        for nameList  in self.name:
            if nameList == taskname:
                print("This task has already existed")
                return

        self.name.append(taskname)
        self.date.append(date)
        self.description.append(description)
        self.status.append(status)
        self.priority.append(priority)

    def deleteTask(self, taskname):
        self.viewTask()

        for nameList in self.name:
            if nameList == taskname:
                index = self.name.index(taskname)
                self.name.pop(index)
                self.date.pop(index)
                self.description.pop(index)
                self.status.pop(index)
                self.priority.pop(index)
                print("Task has been deleted successfully")
                return
        else:
            print("This task cannot be found")

    def viewTask(self):
        if not self.name:
            print("No task has been added yet.")
            return

        table_data = []
        for i in range(len(self.name)):
            table_data.append([i+1, self.name[i], self.date[i], self.description[i], self.status[i], self.priority[i]])

        headers = ["No", "Task Name", "Task Date", "Task Description", "Task Status", "Task Priority"]
        print(tabulate(table_data, headers = headers, tablefmt="grid"))
        # for i in range(len(self.name)):
        #     if self.priority[i] == "High":
        #         print("Task Name: ", self.name[i])
        #         print("Task Date: ", self.date[i])
        #         print("Task Description: ", self.description[i])
        #         print("Task Status: ", self.status[i])
        #         print("Task Priority: ", self.priority[i])
        # print("\n")
        #
        # for i in range(len(self.name)):
        #     if self.priority[i] == "Medium":
        #         print("Task Name: ", self.name[i])
        #         print("Task Date: ", self.date[i])
        #         print("Task Description: ", self.description[i])
        #         print("Task Status: ", self.status[i])
        #         print("Task Priority: ", self.priority[i])
        # print("\n")
        #
        # for i in range(len(self.name)):
        #     if self.priority[i] == "Low":
        #         print("Task Name: ", self.name[i])
        #         print("Task Date: ", self.date[i])
        #         print("Task Description: ", self.description[i])
        #         print("Task Status: ", self.status[i])
        #         print("Task Priority: ", self.priority[i])
        # print("\n")

    def updateTask(self, taskname):
        index = self.name.index(taskname)
        self.status[index] = "Completed"

    def saveTask(self):
        with open("task.csv","w") as f:
            for i in range(len(self.name)):
                f.write(self.name[i] + "," + self.date[i] + "," + self.description[i] + "," + self.status[i] + "," + self.priority[i] + "\n")

        print("Task has been saved successfully to task.csv")

    def loadTask(self):
        with open("task.csv", "r") as f:
            for line in f:
                list = line.split(",")
                self.addTask(list[0], list[1], list[2], list[3], list[4].strip())
            self.viewTask()

    def searchTask(self, taskname):
        if taskname in self.name:
            index = self.name.index(taskname)
            print(f"""
            Task Name: {taskname}
            Task Date: {self.date[index]}
            Task Description: {self.description[index]}
            Task Status: {self.status[index]}
            Task Priority: {self.priority[index]}""")
        else:
            print("This task cannot be found in the list")

    def overDueTask(self):
        found = False
        for i in range(len(self.name)):
            taskDate = datetime.strptime(self.date[i], "%Y-%m-%d")
            if taskDate < datetime.today() and self.status[i] != "Completed":
                print(f"""
                Overdue Task Name: {self.name[i]}
                Please Complete This Task As Soon As Possible""")
                found = True

        if found == False:
            print("No overdue task found in the list")

