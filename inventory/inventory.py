""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
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
    in_menu =  True

    while in_menu:
        ui.print_menu("Inventory", ["Show Table", "Add", "Remove", "Update", "Get Available Items", "Get Average Durability By Manufacturers"], "Back to Main Menu")
        number_of_menu_options = 6
        user_input = ui.get_input_menu(number_of_menu_options-1) #asks user to select numbered option from the menu
        file_name = "inventory/inventory.csv"
        table = data_manager.get_table_from_file("inventory/inventory.csv")
        if user_input == 1:
            show_table(data_manager.get_table_from_file("inventory/inventory.csv"))
        elif user_input == 2:
            title_list = ["Id: ", "Name: ", "Manufacturer: ", "Purchase Year: ", "Durability: "]
            callout = "Please provide data for new entry"
            added_to_table = ui.get_inputs(title_list, callout)
            add(added_to_table)
        elif user_input == 3:
            file_in_list_form = data_manager.get_table_from_file(file_name)
            list_labels = ["Id:"]
            title = "Please provide Id of entry to be removed"
            id_to_be_removed = ui.get_inputs(list_labels, title)
            remove(file_in_list_form, id_to_be_removed)
        elif user_input == 4:
            id_ = ui.get_inputs(['Choose ID which do you want update:  '], "Please provide your personal information")
            update(table,id_)
        elif user_input == 5:
            get_available_items(table, id)
        elif user_input == 6:
            get_average_durability_by_manufacturers(table, id)
        elif user_input == 0:
            in_menu = False #jest w menu i prosi o input, jeśli nie dostanie 0 pętla się powtarza a jak się przerwie, user wychodzi itd. 
    
    main.main() #exit to the main menu



def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    ui.print_table(table, ["Id", "Name", "Manufacturer", "Purchase Year", "Durability"]) #z UI tabelka

def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    file_name = "inventory/inventory.csv"
    file_in_list_form = data_manager.get_table_from_file(file_name)
    added_to_table = file_in_list_form + [[";".join(table)]] #nowy wpis
    data_manager.write_table_to_file(file_name, added_to_table)

    return table


def remove(table, id):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    file_name = "inventory/inventory.csv"
    count = 0
    for entry in table:
        entry = str(entry[0])
        entry_in_list_form = entry.split(",")
        if entry_in_list_form[0] == id[0]:
            new_table = table[:count] + table[count+1:]
            data_manager.write_table_to_file(file_name, new_table)
        count += 1
    start_module()

    return table


def update(table, id_):
    index_table = 0
    for row in table:
        print(row)
        print(table[index_table][0])
        print(id_)
        if table[index_table][0] == str(id_[0]):
            ui.print_result(row, f"This is  employee which you choose ")
            datauser = ui.get_inputs(["Name: ", "Manufacter: " , "Purchase Year: ", "Durability: "], "Please insert new information")
            table[index_table][1:] = datauser
            ui.print_result(table[index_table],f"This is your record after changes")
        index_table += 1


    data_manager.write_table_to_file("inventory/inventory.csv", table)
    
    
    start_module()

    return tables


# special functions:
# ------------------

def get_available_items(table, year):
    """
    Question: Which items have not exceeded their durability yet (in a given year)?

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """

    # your code


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    # your code
