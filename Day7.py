from pathlib import Path

def todo_list_app():
    todo_file = Path("todo_list.txt")

    # Load existing tasks
    if not todo_file.exists():
        todo_file.write_text("")  # Create file if not present

    tasks = todo_file.read_text().splitlines()

    print("📋 Welcome to the Simple To-Do List App!")
    print("Commands: [1] Add Task  [2] View Tasks  [3] Remove Task  [q] Quit\n")

    while True:
        choice = input("👉 Enter command (1/2/3/q): ").strip()

        if choice == '1':
            task = input("📝 Enter your new task: ").strip()
            if task:
                tasks.append(task)
                print(f"✅ Task added: {task}\n")
            else:
                print("⚠️ Task cannot be empty.\n")

        elif choice == '2':
            if not tasks:
                print("📭 No tasks found.\n")
            else:
                print("\n📌 Your Tasks:")
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t}")
                print()

        elif choice == '3':
            if not tasks:
                print("📭 No tasks to remove.\n")
                continue

            print("\n📌 Your Tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

            try:
                index = int(input("👉 Enter task number to remove: ")) - 1
                removed = tasks.pop(index)
                print(f"✅ Removed task: {removed}\n")
            except (IndexError, ValueError):
                print("⚠️ Invalid task number.\n")

        elif choice.lower() == 'q':
            print("👋 Exiting To-Do List App. See you soon!")
            break

        else:
            print("⚠️ Invalid command.\n")

    # Save updated tasks
    todo_file.write_text("\n".join(tasks))

if __name__ == "__main__":
    todo_list_app()
