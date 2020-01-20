""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

FILE_NAME = "accounting/items.csv"
TITLE_LIST = ['ID:','Month:','Day:','Year:','Type:','Amount:']


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    title = "Accounting"
    list_options = ['Show table','Add new entry','Remove a record','Update specific record','Show year with the highest profit','Show average profit per item in a given year']
    exit_message = "Go back to main menu"
    ui.print_menu(title, list_options, exit_message)
    number_of_menu_options = 7
    user_input = ui.get_input_menu(number_of_menu_options-1)
    table = data_manager.get_table_from_file(FILE_NAME)

    if user_input == 1:
        show_table(table)
        start_module()
    elif user_input == 2:
        add(table)
        start_module()
    elif user_input == 3:
        show_table(table)
        list_labels = ['ID:']
        title = "Please provide the ID to be removed"
        id_ = ui.get_inputs(list_labels, title)
        remove(table, id_)
        start_module()
    elif user_input == 4:
        update(table, id_)
    elif user_input == 5:
        which_year_max(table)
    elif user_input == 6:
        avg_amount(table, year)
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
    
    ui.print_table(table, TITLE_LIST)

def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    title = "Please provide data for new entry:"
    new_record = ui.get_inputs(TITLE_LIST, title)
    table = table + [[";".join(new_record)]]
    data_manager.write_table_to_file(FILE_NAME, table)

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

    for row in table:
        if str(row[0]) == str(id_[0]):
            table.remove(row)
            label = "You have successfully removed index: "
            result = id_[0]
            ui.print_result(result, label)           
        else:
            pass
    data_manager.write_table_to_file(FILE_NAME, table)
    
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

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """

    # your code


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """

    # your code
