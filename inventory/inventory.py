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

file_name = "inventory/inventory.csv"


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    in_menu = True

    while in_menu:
        ui.print_menu("Inventory", [
            "Show Table", "Add", "Remove", "Update", "Get Available Items",
            "Get Average Durability By Manufacturers"
        ], "Back to Main Menu")
        number_of_menu_options = 7
        user_input = ui.get_input_menu(
            number_of_menu_options -
            1)  #asks user to select numbered option from the menu
        table = data_manager.get_table_from_file(file_name)
        if user_input == 1:
            show_table(data_manager.get_table_from_file(file_name))
        elif user_input == 2:
            file_in_list_form = data_manager.get_table_from_file(file_name)
            add(file_in_list_form)
        elif user_input == 3:
            file_in_list_form = data_manager.get_table_from_file(file_name)
            list_labels = ["Id:"]
            title = "Please provide Id of entry to be removed"
            id_to_be_removed = ui.get_inputs(list_labels, title)
            remove(file_in_list_form, id_to_be_removed)
        elif user_input == 4:
            id_ = ui.get_inputs(['Choose ID which do you want update:  '],
                                "Please provide your personal information")
            update(table, id_)
        elif user_input == 5:
            year = ui.get_inputs(["Year: :"], "Enter a year")
            get_available_items(table, year)
        elif user_input == 6:
            get_average_durability_by_manufacturers(table)
            
        elif user_input == 0:
            in_menu = False  #jest w menu i prosi o input, jeśli nie dostanie 0 pętla się powtarza a jak się przerwie, user wychodzi itd.

    main.main()  #exit to the main menu


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    ui.print_table(
        table, ["Id", "Name", "Manufacturer", "Purchase Year", "Durability"
                ])  #z UI tabelka


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    CURRENT_YEAR = 2020
    message = ("Please check your input")
    title_list = [
        "Name: ", "Manufacturer: ", "Purchase Year: ", "Durability: "
    ]
    title = "Please provide data for new entry"
    id_ = common.generate_random(table)
    new_record = ui.get_inputs(title_list, title)
    new_record.insert(0, id_)
    if isinstance(new_record[1],
                  str) and int(new_record[3]) < CURRENT_YEAR + 1:
        table += [[";".join(new_record)]]
        label = "You have just added new client: "
        ui.print_result(new_record, label)
        data_manager.write_table_to_file(file_name, table)
    else:
        ui.print_error_message(message)
        add(table)
    start_module()

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

    count = 0
    for entry in table:
        entry = str(entry[0])
        entry_in_list_form = entry.split(",")
        if entry_in_list_form[0] == id[0]:
            new_table = table[:count] + table[count + 1:]
            data_manager.write_table_to_file(file_name, new_table)
        count += 1
    start_module()

    return table


def update(table, id_):
    index_table = 0
    for row in table:
        if table[index_table][0] == str(id_[0]):
            ui.print_result(row, f"This is  which you choose ")
            datauser = ui.get_inputs(
                ["Name: ", "Manufacter: ", "Purchase Year: ", "Durability: "],
                "Please insert new information")
            table[index_table][1:] = datauser
            ui.print_result(table[index_table],
                            f"This is your record after changes")
        index_table += 1

    data_manager.write_table_to_file(file_name, table)

    start_module()

    return table


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
    temp_table = []
    current_year = 2020
    row_counter = 0
    for row in table:
        if int(table[row_counter][3]) + int(table[row_counter][4]) >= current_year:
            temp_table.append(row)
        row_counter += 1
    ui.print_table(temp_table, ["Id", "Name", "Manufacturer", "Purchase Year", "Durability"])
    



def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    manufacturers_time_on_list = {}
    manufacturers_sum_of_durability = {}
    manufacturers_avg_of_durability = {}
    row_counter = 0
    for row in table:
        if row[2] in manufacturers_time_on_list.keys():
            manufacturers_time_on_list[row[2]] += 1
            manufacturers_sum_of_durability[row[2]] += int(row[4])
        else:
            manufacturers_time_on_list[row[2]] = 1
            manufacturers_sum_of_durability[row[2]] = int(row[4])
        row_counter += 1
    manufacturers_avg_of_durability = {key:float(manufacturers_sum_of_durability[key])/float(manufacturers_time_on_list[key]) for key in manufacturers_time_on_list}
    ui.print_result(manufacturers_avg_of_durability, "the average durability times for each manufacturer")

    
          
    return manufacturers_avg_of_durability