import random

def menu():
    '''

    Returns nothing
    -------
    Prins the statements below

    '''
    print("COMMAND MENU")
    print("walk- Walk down the path")
    print("show- Show all items")
    print("drop- Drop an item")
    print("exit- Exit program")
    
def choice():
    '''

    Returns choice.lower()
    -------
    TYPE: string
        DESCRIPTION: Asks the user what they'd liek to do. it then returns the command in lowercase'

    '''
    choice = input("\nCommand: ")
    return choice.lower()
    

def walk(file1, file2):
    '''

    Parameters: file1 and fil2e
    
    ----------
    file1 : Text file
        DESCRIPTION: "wizard_all_items.txt"
    file2 : Text file
        DESCRIPTION: "wizard_inventory.txt"

    Returns nothing
    -------
    SEE COMMENTS BELOW

    '''
    
    #an empty lsit is created to hold the items youare not carrying
    not_in_inventory = []
    
    #the wizard_all_items file is opned and put into a list called "all_items"
    with open("{}.txt".format(file1), "r") as path_items:
        all_items = path_items.readlines()
    #wizard_inventory fiel is opned and whatever is in there is added to a "wizard_items" list
    with open("{}.txt".format(file2), "r") as inventory_items:
        wizard_items = inventory_items.readlines()
        
        #iterating thorugh all the items in all_items list
        for item in all_items:
            #if an item isn't in the wizard_items list, it is added to the not_in_inventory list
            if item not in wizard_items:
                not_in_inventory.append(item)
        #a random item is chosen from the not_in_inventory lsit and assigned "random_item" variable
        random_item = random.choice(not_in_inventory)
        #pritns this statement and asks if they want to pikc it up
        print("While walking, you come across {}".format(random_item))
        grab = input("Grab it? (y/n): ")
        #if grab is "y" AND you have less then 4 items in the list, then the item is added to "wizard_items"
        if grab.lower() == "y" and len(wizard_items) < 4:
            wizard_items.append(random_item)
            #"wizard inventory file is opned and the "wizard_items" list is added to it
            with open("{}.txt".format(file2), "w") as inventory_items:
                inventory_items.writelines(wizard_items)
                #prints that you picked up the item
            print("You picked up {}".format(random_item))
            #if you say "n", it pritns that you didn;t pick up the item
        elif grab.lower() == "n":
            print("You did not pick up {}".format(random_item))
            #if yo are carrying 4+ items, this statement is printed
        elif len(wizard_items) >=4: 
            print("You cannot carry anything else. drop something first.")
            
            
def show(file2):
    '''

    Parameters: file2
    ----------
    file2 : Text file
        DESCRIPTION: "wizard_inventory.txt"

    Returns nothing
    -------
    the file is opned and each item is printed along with an index number. 
    number is increased by 1 each loop

    '''
    
    index = 1
    with open("{}.txt".format(file2)) as current_inventory:
        for item in current_inventory:
            print("{}. {}".format(index, item))
            index +=1
      
def drop(file2):
    '''

    Parameters: file2
    ----------
    file2 : text file
        DESCRIPTION: "wizard_inventory.txt"

    Returns nothing
    -------
    an index number is requested and then subtracted by 1
    the file is opned and it's contents is added to a list, "items''
    as logn as the item is in the correct range, the item will be popped
    and a statement pritns, staying that the item was dropped
    the file is opned again and the list is added back into it
    if the index is not vali,d a message prints and the number is requested again.
    if there aren't any items in the list, a message prints stating this'

    '''
    number = int(input("Number: "))
    number -= 1
    with open("{}.txt".format(file2)) as current_inventory:
        items = current_inventory.readlines()
        if number in range(0, len(items)):
            print("{} was dropped".format(items[number])) 
            items.pop(number)
            with open("{}.txt".format(file2), "w") as current_inventory:
                current_inventory.writelines(items)
        else:
            print("Not a valid option. Try again")
            number = int(input("Number: "))
        if len(items) == 0:
            print("You are not carrying any items.")

print("The Wizard Inventory program\n")        
menu()

#go controls the while loop. while go is "y", it the loop will continue
go = "y"

while go == "y":
    user_choice = choice()
    if user_choice == "walk":
        walk("wizard_all_items", "wizard_inventory")
    elif user_choice == "show":
        show("wizard_inventory")
    elif user_choice == "drop":
        drop("wizard_inventory")
    
    #if the user enter exit, the loop breaks
    elif user_choice == "exit":
        break
    
    #if soemthing invalid is entered, this is printed
    else: 
        print("Not a valid choice. try again.")

#Bye pritns at the end
print("\nBye!")
    