""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common
import main

def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    table = data_manager.get_table_from_file("hr/persons.csv")
    title = "Human Resources Manager"
    list_options = ["Show Table", "Add new item", "Remove item", "Update item", "Oldest person"]
    exit_message = "Back to main menu"
    ui.print_menu(title, list_options, exit_message)
    # number_of_menu_options = 7
    file_name = "hr/persons.csv"
    user_input = ui.get_input_menu(len(list_options)) # the function asks for number of menu options - 1
    if user_input == 1:
        show_table(table)
    elif user_input == 2:
        add(table)
    elif user_input == 3:
        id_ = ui.get_inputs(['Choose ID which do you want remove: '], "Please provide your personal information")
        remove(table, id_)
        
    elif user_input == 4:
        id_ = ui.get_inputs(['Choose ID which do want update: '], "Please provide your personal information")
        update(table, id_)
        
    elif user_input == 5:
        table = data_manager.get_table_from_file(file_name)
        (get_oldest_person(table))

    elif user_input == 0:
        main.main()


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    
    ui.print_table(table, ["Code","Name and Surname","Birth date"])
    start_module()

def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    id_  = common.generate_random(table)

    list_labels = ["Name and Surname:","Birth date:"]
    title = "Please provide data for new entry"
    new_entry = ui.get_inputs(list_labels, title)
    table.append([id_, new_entry[0], new_entry[1]])
    ui.print_result(table[len(table)-1], f'You add n record')
    data_manager.write_table_to_file("hr/persons.csv", table)
    start_module()
    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """
    file_name = "hr/persons.csv"
    id_ = ("".join(map(str, id_)))

    for row in table:
        if row[0] == id_:
            ui.print_result(row, f"This is  employee who  you going to remove ")
            table.remove(row)
            ui.print_result(row, f"You removed this record")
        
    data_manager.write_table_to_file(file_name, table)
    start_module()
    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """
    id_ = ("".join(map(str, id_)))
    index_table = 0
    for row in table:
        if row[0] == id_:
            ui.print_result(row, f"This is  employee which you choose ")
            datauser = ui.get_inputs(['input your name: ', 'Choose your hire year:  '], "Please insert new information")
            table[index_table][1:] = datauser
            ui.print_result(table[index_table],f"This is your record after changes")
        index_table += 1
    data_manager.write_table_to_file("hr/persons.csv", table)
    start_module()
    
    return table 


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """
    
    oldest_person = []

    for record in table:
        if not oldest_person:
            oldest_person.append(record)
        elif record[2] == oldest_person[0][2]:    # 2 describe year of birth form HR table
            oldest_person.append(record)
        elif record[2] < oldest_person[0][2]:
            oldest_person.clear()
            oldest_person.append(record)
    
    name_list = [name[1] for name in oldest_person] # 1 describe name person of the list
    ui.print_result(name_list,f"Olders person of the company")
    start_module()
        


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    # your code
