import json
import csv

# File paths
tasks_json_file = 'lesson-9/homework/tasks.json'
tasks_csv_file = 'lesson-9/homework/tasks.csv'

# Load tasks from tasks.json
def load_tasks():
    with open(tasks_json_file, 'r') as file:
        tasks = json.load(file)
    return tasks

# Save tasks back to tasks.json
def save_tasks(tasks):
    with open(tasks_json_file, 'w') as file:
        json.dump(tasks, file, indent=4)

# Display tasks
def display_tasks(tasks):
    print("\nTasks:")
    print("ID\tTask Name\t\tCompleted\tPriority")
    for task in tasks:
        print(f"{task['id']}\t{task['task']}\t\t{task['completed']}\t{task['priority']}")

# Calculate task completion stats
def calculate_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    pending_tasks = total_tasks - completed_tasks
    average_priority = sum(task['priority'] for task in tasks) / total_tasks if total_tasks > 0 else 0

    print("\nTask Statistics:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {average_priority:.2f}")

# Convert JSON data to CSV
def convert_to_csv(tasks):
    with open(tasks_csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task['id'], task['task'], task['completed'], task['priority']])
    print(f"\nTasks have been exported to {tasks_csv_file}.")


def main():
    # Load tasks
    tasks = load_tasks()

    # Display tasks
    display_tasks(tasks)

    # Calculate and display statistics
    calculate_stats(tasks)

    # Modify a task (example: mark task with ID 1 as completed)
    for task in tasks:
        if task['id'] == 1:
            task['completed'] = True
            break

    # Save changes back to JSON
    save_tasks(tasks)
    print("\nChanges have been saved to tasks.json.")

    # Convert tasks to CSV
    convert_to_csv(tasks)

if __name__ == "__main__":
    main()
