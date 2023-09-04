def to_do():

    todo = []

    while True:
        menu = input("To add a task type 'add', to remove a task type 'remove', to view all tasks type 'view', and to exit type 'exit'")
        
        if menu == 'view':
            print("To do list:")
            for index, task in enumerate(todo, start=1):
                 print(f"{index}. {task}")

        elif menu == 'add':
            add = input('What task would you like to add? ')
            todo.append(add)
            print('Task submitted')
            print("To do list:")
            for index, task in enumerate(todo, start=1):
                 print(f"{index}. {task}")
        
        elif menu == 'remove':
            remove = input('Which task would you like to remove? ')
            if remove not in todo:
                print('Error: Invalid choice')
            else:
                todo.remove(remove)
                print("Task removed")
                print("To do list:")
            for index, task in enumerate(todo, start=1):
                 print(f"{index}. {task}")
    
        elif menu == 'exit':
            print("Finally...I mean bye...")
            break
        
        else: print("Wrong input - Please type 'add, remove, view or exit'")

to_do()
