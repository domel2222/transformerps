""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
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

    in_menu =  True

    while in_menu:
        ui.print_menu("Sales", ["Show Table", "Add", "Remove", "Update", "Get Lowest Price Item Id", "Get Items Sold Between"], "Back to Main Menu")
        number_of_menu_options = 6
        user_input = ui.get_input_menu(number_of_menu_options-1) #asks user to select numbered option from the menu
        if user_input == 1:
            show_table(data_manager.get_table_from_file("sales/sales.csv"))
        elif user_input == 2:
            title_list = ["Id", "Title", "Price", "Month", "Day", "Year"]
            callout = "Please provide data for new entry"
            added_to_table = ui.get_inputs(title_list, callout)
            add(added_to_table)
        elif user_input == 3:
            remove(table, id)
        elif user_input == 4:
            update(table, id)
        elif user_input == 5:
            get_lowest_price_item_id(table, id)
        elif user_input == 6:
            get_items_sold_between(table, id)
        elif user_input == 0:
            in_menu = False #jest w menu i prosi o input, jeśli nie dostanie 0 pętla się powtarza a jak się przerwie, user wychodzi itd. 
    # main.main() #exit to the main menu


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    title_list = ["Id", "Title", "Price", "Month", "Day", "Year"]
    ui.print_table(table, title_list) #z UI tabelka


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    file_name = "sales/sales.csv"
    file_in_list_form = data_manager.get_table_from_file(file_name)
    added_to_table = file_in_list_form + [[",".join(table)]] #nowy wpis
    data_manager.write_table_to_file(file_name, added_to_table)

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

    # your code

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

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    # your code


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """

    # your code
