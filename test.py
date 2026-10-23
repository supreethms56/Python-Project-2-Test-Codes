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
            return
            
        print("📝 Your To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task.strip()}")
            
    except FileNotFoundError:
        print("📭 Your to-do list is empty!")

def main():
    # 1. Initialize the argument parser
    parser = argparse.ArgumentParser(description="A simple Command Line To-Do List App")

    # 2. Define the commands/arguments the user can type
    parser.add_argument("--add", type=str, help="Add a new task to the list")
    parser.add_argument("--list", action="store_true", help="Show all your tasks")

    # 3. Parse the arguments typed into the terminal
    args = parser.parse_args()

    # 4. Route the arguments to the correct action
    if args.add:
        add_task(args.add)
    elif args.list:
        list_tasks()
    else:
        # If the user types nothing, show them the help screen
        parser.print_help()

if __name__ == "__main__":
    main()
