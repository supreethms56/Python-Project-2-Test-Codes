import argparse

# Simple text file to save our tasks
TODO_FILE = "tasks.txt"

def add_task(task_text):
    """Saves a new task to the text file."""
    with open(TODO_FILE, "a") as file:
        file.write(task_text + "\n")
    print(f"✅ Added task: '{task_text}'")

def list_tasks():
    """Reads and prints all tasks from the text file."""
    try:
        with open(TODO_FILE, "r") as file:
            tasks = file.readlines()
            
        if not tasks:
            print("📭 Your to-do list is empty!")
            return [] # Return an empty list if no tasks exist
            
        print("📝 Your To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task.strip()}")
        return tasks # Return the tasks so other functions can use them
            
    except FileNotFoundError:
        print("📭 Your to-do list is empty!")
        return []

def delete_task(task_number):
    """Removes a specific task by its list number."""
    try:
        # 1. Read the existing tasks
        with open(TODO_FILE, "r") as file:
            tasks = file.readlines()

        # 2. Check if the list is empty
        if not tasks:
            print("📭 Nothing to delete. Your list is empty!")
            return

        # 3. Convert task number (e.g., 2) to Python index (e.g., 1)
        # Python starts counting at 0, but humans start counting at 1!
        target_index = task_number - 1

        # 4. Make sure the number isn't too small or too big
        if target_index < 0 or target_index >= len(tasks):
            print(f"❌ Error: Task #{task_number} does not exist!")
            return

        # 5. Remove the task from our temporary memory list
        removed_task = tasks.pop(target_index)

        # 6. Overwrite the file with the remaining tasks
        with open(TODO_FILE, "w") as file:
            file.writelines(tasks)

        print(f"🗑️ Deleted task: '{removed_task.strip()}'")

    except FileNotFoundError:
        print("📭 Nothing to delete. Your list is empty!")

def main():
    # Initialize the argument parser
    parser = argparse.ArgumentParser(description="A simple Command Line To-Do List App")

    # Define the commands/arguments
    parser.add_argument("--add", type=str, help="Add a new task to the list")
    parser.add_argument("--list", action="store_true", help="Show all your tasks")
    parser.add_argument("--delete", type=int, help="Delete a task by its list number")

    # Parse the arguments typed into the terminal
    args = parser.parse_args()

    # Route the arguments to the correct action
    if args.add:
        add_task(args.add)
    elif args.list:
        list_tasks()
    elif args.delete:
        delete_task(args.delete)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
