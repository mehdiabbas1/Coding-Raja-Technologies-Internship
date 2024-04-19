tasks=[]

def addTask():
  task = input("Please enter a task: ")
  priority=input("priority(HIGH, MEDIUM, LOW otherwise None): ").upper()
 ## duetime = input("Enter the due time : ")
  duedate=(input(f"Date(DD MM YYYY): ").split())
  ##duedate=(f"{duedate} duedate:{dat")
  ##print(f"Due Date is added to the task at {date}/{month}/{year}","\n")
  #tasks.append(task)
  #tasks.append(priority)
  #tasks.append(task[x-1])
  tasks.append(f"{task}:{priority}:{duedate}")
  print(f"Task '{task}' added to the list.")

def view(tasks):
  if tasks!=[]:
    for i in range(len(tasks)):
      print(f"{i+1}. {tasks[i]}")
  else:
    print("EMPTY!!!")


#def listTasks():
  
  #if not tasks:
    #print("There are no tasks currently.")
  #else:
    #print("Current Tasks:")
    #for index, task in enumerate(tasks):
     # print(f"Task #{index}. {task} ")


def completeTask():
  if tasks!=[]:
            which_task=int(input("which task is completed: "))
            if which_task<=len(tasks) and which_task>0:
                if "=completed" not in tasks[which_task-1]: 
                  tasks[which_task-1]=f"{tasks[which_task-1]}=completed"
                else:
                    print("Already mark as completed...\n")
            else:
                print("No task is there!!")
  else:
     print("Empty list..")


def deleteTask():
  if tasks!=[]:
    which_task=int(input("which task to be delete: "))
    del tasks[which_task-1]
  else:
    print("task list is empty!!\n")


def filehandle(file_path):
    mode=input("Only for reading type:'r' or add something type:'a': ").lower()
    if file_path=="" or mode=="":
        print("No file name or mode!")
    elif file_path!="" and (mode=="a" or mode=="r"):
        print(f"File name: {file_path}, mode='{mode}'")
        file=open(f"{file_path}",f"{mode}")
        if mode=="r":
            print(file.read())
            file.close()

        elif mode=="a":
            write_words=input("Write tasks to add it to the existing file: ")
            file.write(f"\n{write_words}")
            file.close()
            print("Successfully added.")

        else:
            print("Not a right mode!!")



    elif file_path!="" and (mode!="a" or mode!="r"):
        print("wrong mode..")
        
  



if __name__ == "__main__":
  file_path="file.txt"
  ### Create a loop to run the apP
  print("Welcome to the to do list app :)")
  while True:
    print("\n")
    print("Please select one of the following options")
    print("------------------------------------------")
    print("1. Add a new task")
    print("2. Delete a task")
    print("3. View tasks")
    print("4. Completed Task")
    print("5. TASK FILE")

    choice = input("Enter your choice: ")

    if (choice == "1"):
      addTask()
    elif (choice == "2"):
      deleteTask()
    elif (choice == "3"):
      view(tasks)
    elif (choice == "4"):
      completeTask()
    elif (choice == "5"):
      filehandle(file_path)
    else:
      print("Invalid input. Please try again.")
    continue

  print("Goodbye 👋👋")