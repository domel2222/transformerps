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
    if user_input == 1:
        show_table(data_manager.get_table_from_file("accounting/items.csv"))
    elif user_input == 2:
        add(table)
    elif user_input == 3:
        # show_table(data_manager.get_table_from_file("accounting/items.csv"))
        table = data_manager.get_table_from_file("accounting/items.csv")
        print(table)
        list_labels = ['ID:']
        title = "Please provide the ID to be removed"
        id_ = ui.get_inputs(list_labels, title)
        remove(table, id_)
        print(id_) #test
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

    file_name = "accounting/items.csv"
    table = data_manager.get_table_from_file(file_name)
    title_list = ['id','month','day','year','type','amount']
    ui.print_table(table, title_list)
    start_module()

def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code

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
    file_name = "accounting/items.csv"

    for row in table:
        if str(row[0]) == str(id_[0]):
            table.remove(row)
        else:
            pass

    data_manager.write_table_to_file(file_name, table)
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
