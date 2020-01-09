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
    user_input = ui.get_input_menu(number_of_menu_options-1) # the function asks for number of menu options - 1
    if user_input == 1:
        show_table(data_manager.get_table_from_file("hr/persons.csv"))
    elif user_input == 2:
        list_labels = ["Code:","Name and Surname:","Birth date:"]
        title = "Please provide data for new entry"
        new_entry = ui.get_inputs(list_labels, title)
        add(new_entry)
    elif user_input == 3:
        remove(table, id_)
    elif user_input == 4:
        update(table, id_)
    elif user_input == 0:
        pass
         # how do i get back to main()?


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
    file_in_list_form = data_manager.get_table_from_file(file_name)
    table_after_change = file_in_list_form + [[",".join(new_entry)]]
    data_manager.write_table_to_file(file_name, table_after_change)
    start_module()
    #return table #what for?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<change


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """
    
    

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

    # your code

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
