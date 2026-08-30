tasks = ["apple","orange","guava"]
while True :
    print(  "="*40)
    print("To Do List App")
    print("="*40)
    print("1.add task:")
    print("2.remove and update task:")
    print("3.view task:")
    print("4. Exit:")
    choice=(input("\nyour choice(1-4):"))
    print("you enter choice:",choice)
    if choice=="1" :
        task= input("entre task: ")
        tasks.append(task)
        print(tasks) 
    elif choice=="2":
        task= input("enter task to remove:")
        if task in tasks :
            tasks.remove(task)
            print(tasks)
        elif task in tasks :
            tasks.update(task)
            print(tasks)
        else:
            print("task is not present in the list")
    elif choice== "3":
        print("you only see the list:", tasks)
        break
    else:
        print("exit from the list")
        break







  

        





