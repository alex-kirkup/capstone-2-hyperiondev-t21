#=====importing libraries===========

from datetime import date

#====Login Section====

#get users from user.txt
users = []
with open("user.txt","r") as f:
    for line in f.readlines():
        line = line.strip().split(', ')
        users.append(
            {
                'username' : line[0],
                'password' : line[1],
            }
        )

#loop until user logged in successfully
user_found = False
while not user_found:
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    for user in users:
        if user['username'] == username and user['password'] == password:
            user_found = True
            print()
            print(f"You are now logged in as {username}")
            print()

    if not user_found:
        print()
        print("You have not entered a valid username and/or password")
        print()

#create user menu options
if username == "admin":
    user_input_str = '''Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - View my tasks
        s - Statistics
        e - Exit
        : '''
else:
    user_input_str = '''Select one of the following Options below:
        a - Adding a task
        va - View all tasks
        vm - view my task
        e - Exit
        : '''

while True:
    #present the menu to the user and 
    #capturing user selection as lower case
    menu = input(user_input_str).lower()

    if menu == 'r' and username == 'admin':
        #register a new user (admin user only)

        new_username = input("Please enter new username: ")
        new_password = input("Please enter password: ")
        new_password_check = input("Please confirm password: ")

        if new_password == new_password_check:
            with open("user.txt","a") as f:
                f.write('\n' + new_username + ', ' + new_password)

            print()
            print(f"You have registered {new_username} as a new user")
            print()

        else:
            print()
            print(f"The passwords did not match - user {new_username} was not created")
            print()

    elif menu == 'a':
        #add a task
            
        username = input("Please enter the username to whom the task is assigned: ")
        title = input("Please enter a title for the task: ")
        desc = input("Please enter a description for the task: ")
        due_date = input("Please enter the due date: ")
        current_date = date.today()
    
        with open("tasks.txt","a") as f:
            f.write(
                '\n' + 
                username + ', ' + 
                title + ', ' + 
                desc + ', ' + 
                current_date.strftime('%d %b %Y') + ', ' + 
                due_date + ', ' + 
                'No'
            )

        print()
        print(f"You have successfully entered a new task")
        print()

    elif menu == 'va':
        #view all tasks

        with open("tasks.txt","r") as f:
            for line in f.readlines():
                line = line.strip().split(', ')

                print("-----------------------------------------------")
                print(f"Task:             {line[1]}")
                print(f"Assigned to:      {line[0]}")
                print(f"Date assigned:    {line[3]}")
                print(f"Due date:         {line[4]}")
                print(f"Task complete?    {line[5]}")
                print(f"Task description:")
                print(f"  {line[2]}")
                print("-----------------------------------------------")
                print()


    elif menu == 'vm':
        #view own tasks
            
        with open("tasks.txt","r") as f:
            for line in f.readlines():
                line = line.strip().split(', ')

                if line[0] == username:
                    print("-----------------------------------------------")
                    print(f"Task:             {line[1]}")
                    print(f"Assigned to:      {line[0]}")
                    print(f"Date assigned:    {line[3]}")
                    print(f"Due date:         {line[4]}")
                    print(f"Task complete?    {line[5]}")
                    print(f"Task description:")
                    print(f"  {line[2]}")
                    print("-----------------------------------------------")
                    print()

    elif menu == 's':
        #display stats about tasks

        count_tasks = 0
        with open("tasks.txt","r") as f:
            for line in f.readlines():
                count_tasks += 1

        count_users = 0
        with open("user.txt","r") as f:
            for line in f.readlines():
                count_users += 1

        print(f"Task and user statistics")
        print(f"------------------------")
        print(f"Number of tasks: {count_tasks}")
        print(f"Number of users: {count_users}")
        print(f"------------------------")
        print()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")