import database

#This will show to user every time 
MENU_PROMPT = """
Please Choose one of these options 
1) Add a new bean.  
2) See all beans.
3) Find a bean by name. 
4) See which perparation method is best for a bean 
5) Exit. 

Your Selection: 
"""

#get database 
def menu():
    connection = database.connect() 
    database.create_tables(connection)
    
    while (user_input := input(MENU_PROMPT)) != "5":
        if user_input == "1":
            name = input("Enter bean name: ")
            method = input("Enter bean prep method: ")
            rating = int(input("Enter bean rating score out of 100: "))

            database.add_bean(connection, name, method, rating)
        elif user_input == "2":
            beans = database.get_all_beans(connection)

            for bean in beans: 
                print(f"{bean[1]} was prepared by {bean[2]} and was rated {bean[3]} / 100")
        elif user_input == "3":
            name = input("Enter bean name: ")
            beans = database.get_beans_by_name(connection, name)

            for bean in beans: 
                print(f"{bean[1]} was prepared by {bean[2]} and was rated {bean[3]} / 100")
        elif user_input == "4":
            name = input("Enter bean name to find: ")
            best_method = database.get_best_perparation(connection, name)

            print(f"The best preparation method for {name} is {best_method[2]}")
        else:
            print("Invalid Inpute, try again")

menu()



