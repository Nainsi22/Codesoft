def display_menu():
    print("\nTo-Do List Menu:")
    print("1.Add Task")
    print("2:View Task")
    print("3.Delete Task")
    print("4. Exit")

def add_task(tasks):
    task = input("enter the task:")
    tasks.append(task)
    print("rask Added Successfully!")


def view_tasks(tasks):
    if tasks:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("\nYour to-do list is empty")
def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the task number to delete:"))
            if 1<= task_num <= len(tasks):
                removed_task= tasks.pop(task_num-1)
                print(f"Task '{removed_task}' deleted success")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number")
def main():
    tasks = []
    while True:
        display_menu()
        choice = input("enter your choice:")
        if choice =="1":
            add_task(tasks)
        elif choice==  "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! please try again.")
if __name__ == "__main__":
    main()


