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


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    title = "Human Resources Manager"
    list_options = ["Show Table", "Add new item", "Update item", "Remove item."]
    exit_message = "Back to main menu"
    ui.print_menu(title, list_options, exit_message)
    number_of_menu_options = 5
    file_name = "hr/persons.csv"
    user_input = ui.get_input_menu(number_of_menu_options-1) # the function asks for number of menu options - 1
    if user_input == 1:
        show_table(data_manager.get_table_from_file("hr/persons.csv"))
    elif user_input == 2:
        file_in_list_form = data_manager.get_table_from_file(file_name)
        add(file_in_list_form)
    elif user_input == 3:
        file_in_list_form = data_manager.get_table_from_file(file_name)
        list_labels = ["Id:"]
        title = "Please provide Id from entry you want to change"
        id_from_entry_to_be_changed = ui.get_inputs(list_labels, title)
        update(file_in_list_form, id_from_entry_to_be_changed)
    elif user_input == 4:
        file_in_list_form = data_manager.get_table_from_file(file_name)
        list_labels = ["Id:"]
        title = "Please provide Id of entry to be removed"
        id_to_be_removed = ui.get_inputs(list_labels, title)
        remove(file_in_list_form, id_to_be_removed)
    elif user_input == 0:
        pass


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
    file_name = "hr/persons.csv"
    list_labels = ["Code:","Name and Surname:","Birth date:"]
    title = "Please provide data for new entry"
    new_entry = ui.get_inputs(list_labels, title)
    table_after_change = table + [[",".join(new_entry)]]
    data_manager.write_table_to_file(file_name, table_after_change)
    start_module()
    #return table #what for?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<change


def remove(table, id):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """
    file_name = "hr/persons.csv"
    count = 0
    for entry in table:
        entry = str(entry[0])
        entry_in_list_form = entry.split(",")
        print(entry_in_list_form[0]) #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<test
        if entry_in_list_form[0] == id[0]:
            print("yes")#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<test
            new_table = table[:count] + table[count+1:]
            data_manager.write_table_to_file(file_name, new_table)
        count += 1
    start_module()

    #return table<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<again, why?


def update(table, id):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    file_name = "hr/persons.csv"
    count = 0
    for entry in table:
        entry = str(entry[0])
        entry_in_list_form = entry.split(",")
        if entry_in_list_form[0] == id[0]:
            print("yes")#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<test
            #chosen_parameter = "" <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<error handling
            #while chosen_parameter != "Name" or chosen_parameter != "Date":
            list_labels = ":"
            title = "which parameter do you want to change? (Name/Date)"
            chosen_parameter_list = ui.get_inputs(list_labels, title)
            chosen_parameter = chosen_parameter_list[0]
            print(chosen_parameter)#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            if chosen_parameter == "Name":
                list_labels = ":"
                title = "New Name and Surname"
                new_name = ui.get_inputs(list_labels, title)[0]
                modified_entry = entry_in_list_form[0] + "," + new_name + "," + entry_in_list_form[2]
                print(modified_entry)
                new_table = table[:count] + [[modified_entry]] + table[count+1:]
                print(new_table)
                data_manager.write_table_to_file(file_name, new_table)
            if chosen_parameter == "Date":
                list_labels = ":"
                title = "New Date of Birth"
                new_date_of_birth = ui.get_inputs(list_labels, title)[0]
                modified_entry = entry_in_list_form[0] + "," + entry_in_list_form[2] + "," + new_date_of_birth
                new_table = table[:count] + [[modified_entry]] + table[count+1:]
                print(new_table)            
                data_manager.write_table_to_file(file_name, new_table)
        count += 1
    start_module()

    #return table<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<again, why?


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

    # your code


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    # your code
