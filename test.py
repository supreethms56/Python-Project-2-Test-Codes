import argparse
import csv
import os

def load_csv(file_path):
    """Helper function to safely read rows from a CSV file."""
    if not os.path.exists(file_path):
        print(f"❌ Error: The file '{file_path}' does not exist.")
        return None
    
    try:
        with open(file_path, mode="r", newline="", encoding="utf-8") as file:
            # reader converts each CSV line into a Python list of columns
            reader = csv.reader(file)
            return list(reader)
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return None

def list_csv(file_path):
    """Reads a CSV file and prints it out like a formatted table."""
    rows = load_csv(file_path)
    if rows is None:
        return

    if not rows:
        print("📭 The CSV file is completely empty!")
        return

    print(f"\n📝 Contents of '{file_path}':")
    print("-" * 40)
    for index, row in enumerate(rows, start=1):
        # joining columns with a pipe symbol | for readability
        row_text = " | ".join(row)
        print(f"{index}. {row_text}")
    print("-" * 40)

def edit_csv(file_path, row_number, new_content, output_path):
    """Edits a specific row in the CSV and saves the result as a new file."""
    rows = load_csv(file_path)
    if rows is None:
        return

    # Check if the list is empty
    if not rows:
        print("📭 Nothing to edit. The file is empty!")
        return

    # Convert human numbers (1, 2...) to Python index (0, 1...)
    target_index = row_number - 1

    # Validate that row number exists
    if target_index < 0 or target_index >= len(rows):
        print(f"❌ Error: Row #{row_number} does not exist in this file!")
        return

    # Split the comma-separated string provided by the user into a list
    # e.g., "Buy milk,Urgent" becomes ["Buy milk", "Urgent"]
    new_row_data = [item.strip() for item in new_content.split(",")]

    # Update the row in memory
    old_row = rows[target_index]
    rows[target_index] = new_row_data

    # Save the updated data out into the fresh file path
    try:
        with open(output_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print(f"🗑️ Replaced row #{row_number}: '{' | '.join(old_row)}'")
        print(f"💾 Updated row with: '{' | '.join(new_row_data)}'")
        print(f"✨ Successfully saved changes as a new file: '{output_path}'")
    except Exception as e:
        print(f"❌ Error saving new CSV file: {e}")

def main():
    parser = argparse.ArgumentParser(description="Advanced CSV Viewer and Editor CLI")

    # Arguments required to specify files
    parser.add_argument("--file", type=str, help="The target CSV file you want to look at or edit")
    parser.add_argument("--output", type=str, help="The destination path when saving your edits as a new file")

    # Action flags
    parser.add_argument("--list", action="store_true", help="Show all rows inside the specified CSV file")
    parser.add_argument("--edit-row", type=int, help="The row number (1-based index) you want to update")
    parser.add_argument("--new-content", type=str, help="The new comma-separated data to put inside that row")

    args = parser.parse_args()

    # Route the commands depending on what combinations the user typed
    if args.list:
        if not args.file:
            print("❌ Error: You must supply a target file path using --file <filename.csv>")
        else:
            list_csv(args.file)

    elif args.edit_row:
        # Editing requires the original file, row target, new text, and an output path
        if not args.file or not args.new_content or not args.output:
            print("❌ Error: Editing requires --file, --new-content, AND --output specified together.")
        else:
            edit_csv(args.file, args.edit_row, args.new_content, args.output)
            
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
