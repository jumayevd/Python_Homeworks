import os
import json
import csv
from abc import ABC, abstractmethod

class Task:
    """
    Represents a task in the to-do application.

    Attributes:
        task_id (str): A unique identifier for the task.
        title (str): The title of the task.
        description (str): A brief description of the task.
        due_date (str or None): The due date of the task, optional.
        status (str): The current status of the task (Pending, In Progress, Completed).
    """

    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        """
        Initializes a new task with the given details.

        Parameters:
            task_id (str): The unique identifier for the task.
            title (str): The title of the task.
            description (str): A brief description of the task.
            due_date (str, optional): The due date of the task. Defaults to None.
            status (str, optional): The status of the task. Defaults to "Pending".
        """
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        """
        Returns a string representation of the task.

        Returns:
            str: A formatted string describing the task.
        """
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"

class StorageHandler(ABC):
    """
    An abstract base class for storage handlers that handle saving and loading tasks from storage.

    Methods:
        save(tasks): Saves the tasks to storage.
        load(): Loads tasks from storage and returns them as a list of Task objects.
    """

    @abstractmethod
    def save(self, tasks):
        pass

    @abstractmethod
    def load(self):
        pass

class JSONStorageHandler(StorageHandler):
    """
    Handles saving and loading tasks in JSON format.

    Attributes:
        file_name (str): The name of the JSON file where tasks are saved/loaded.
    """

    def __init__(self, file_name):
        """
        Initializes the handler with the specified JSON file name.

        Parameters:
            file_name (str): The name of the JSON file.
        """
        self.file_name = file_name

    def save(self, tasks):
        """
        Saves the list of tasks to a JSON file.

        Parameters:
            tasks (list of Task): The list of tasks to save.
        """
        with open(self.file_name, "w") as file:
            json.dump([task.__dict__ for task in tasks], file, indent=4)

    def load(self):
        """
        Loads tasks from a JSON file.

        Returns:
            list of Task: A list of Task objects loaded from the JSON file.
        """
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                return [Task(**data) for data in json.load(file)]
        return []

class CSVStorageHandler(StorageHandler):
    """
    Handles saving and loading tasks in CSV format.

    Attributes:
        file_name (str): The name of the CSV file where tasks are saved/loaded.
    """

    def __init__(self, file_name):
        """
        Initializes the handler with the specified CSV file name.

        Parameters:
            file_name (str): The name of the CSV file.
        """
        self.file_name = file_name

    def save(self, tasks):
        """
        Saves the list of tasks to a CSV file.

        Parameters:
            tasks (list of Task): The list of tasks to save.
        """
        with open(self.file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Task ID", "Title", "Description", "Due Date", "Status"])
            for task in tasks:
                writer.writerow([task.task_id, task.title, task.description, task.due_date, task.status])

    def load(self):
        """
        Loads tasks from a CSV file.

        Returns:
            list of Task: A list of Task objects loaded from the CSV file.
        """
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                reader = csv.DictReader(file)
                return [Task(row["Task ID"], row["Title"], row["Description"], row["Due Date"], row["Status"]) for row in reader]
        return []

class ToDoApp:
    """
    The main to-do application that manages tasks and interacts with the user.

    Attributes:
        storage_handler (StorageHandler): The storage handler used to load and save tasks.
        tasks (list of Task): A list of tasks currently managed by the application.
    """

    def __init__(self, storage_handler):
        """
        Initializes the application with the specified storage handler.

        Parameters:
            storage_handler (StorageHandler): The storage handler for saving/loading tasks.
        """
        self.storage_handler = storage_handler
        self.tasks = self.storage_handler.load()

    def add_task(self):
        """
        Prompts the user to enter details for a new task and adds it to the task list.
        """
        task_id = input("Enter Task ID: ")
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        due_date = input("Enter Due Date (YYYY-MM-DD, optional): ") or None
        status = input("Enter Status (Pending/In Progress/Completed): ") or "Pending"
        self.tasks.append(Task(task_id, title, description, due_date, status))
        print("Task added successfully!")

    def view_tasks(self):
        """
        Displays all tasks in the task list.
        """
        if not self.tasks:
            print("No tasks available.")
            return
        print("Tasks:")
        for task in self.tasks:
            print(task)

    def update_task(self):
        """
        Prompts the user to update the details of an existing task by entering its ID.
        """
        task_id = input("Enter Task ID to update: ")
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = input(f"Enter new Title ({task.title}): ") or task.title
                task.description = input(f"Enter new Description ({task.description}): ") or task.description
                task.due_date = input(f"Enter new Due Date ({task.due_date}): ") or task.due_date
                task.status = input(f"Enter new Status ({task.status}): ") or task.status
                print("Task updated successfully!")
                return
        print("Task not found.")

    def delete_task(self):
        """
        Prompts the user to delete an existing task by entering its ID.
        """
        task_id = input("Enter Task ID to delete: ")
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print("Task deleted successfully!")
                return
        print("Task not found.")

    def filter_tasks(self):
        """
        Filters tasks based on their status and displays the filtered list.
        """
        status = input("Enter Status to filter by (Pending/In Progress/Completed): ")
        filtered_tasks = [task for task in self.tasks if task.status == status]
        if filtered_tasks:
            print("Filtered Tasks:")
            for task in filtered_tasks:
                print(task)
        else:
            print("No tasks found with the given status.")

    def save_tasks(self):
        """
        Saves the current list of tasks to storage.
        """
        self.storage_handler.save(self.tasks)
        print("Tasks saved successfully!")

    def load_tasks(self):
        """
        Loads tasks from storage and updates the task list.
        """
        self.tasks = self.storage_handler.load()
        print("Tasks loaded successfully!")

    def menu(self):
        """
        Displays the main menu and allows the user to choose actions like adding, viewing, updating, deleting tasks.
        """
        while True:
            print("\nWelcome to the To-Do Application!")
            print("1. Add a new task")
            print("2. View all tasks")
            print("3. Update a task")
            print("4. Delete a task")
            print("5. Filter tasks by status")
            print("6. Save tasks")
            print("7. Load tasks")
            print("8. Exit")

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 8.")
                continue

            if choice == 1:
                self.add_task()
            elif choice == 2:
                self.view_tasks()
            elif choice == 3:
                self.update_task()
            elif choice == 4:
                self.delete_task()
            elif choice == 5:
                self.filter_tasks()
            elif choice == 6:
                self.save_tasks()
            elif choice == 7:
                self.load_tasks()
            elif choice == 8:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 8.")

# Entry point to run the program
if __name__ == "__main__":
    print("Choose storage format: 1 for JSON, 2 for CSV")
    format_choice = input("Enter your choice: ")
    if format_choice == "1":
        handler = JSONStorageHandler("tasks.json")
    elif format_choice == "2":
        handler = CSVStorageHandler("tasks.csv")
    else:
        print("Invalid choice. Defaulting to JSON.")
        handler = JSONStorageHandler("tasks.json")

    app = ToDoApp(handler)
    app.menu()
