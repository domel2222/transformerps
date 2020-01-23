""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
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
    table = data_manager.get_table_from_file("store/games.csv")
    while in_menu:
        ui.print_menu("Store", ["Show Table", "Add", "Remove", "Update", "Get Counts By Manufacturers", "Get Average By Manufacturer"], "Back to Main Menu")
        number_of_menu_options = 6
        file_name = "store/games.csv" 
        user_input = ui.get_input_menu(number_of_menu_options-1) #asks user to select numbered option from the menu
        if user_input == 1:
            show_table(data_manager.get_table_from_file("store/games.csv"))
        elif user_input == 2:
            table = data_manager.get_table_from_file("store/games.csv")
            add(table)
        elif user_input == 3:
            file_in_list_form = data_manager.get_table_from_file(file_name)
            title = "Please provide Id of entry to be removed"
            list_labels = ":"
            id_to_be_removed = ui.get_inputs(list_labels, title)
            remove(file_in_list_form, id_to_be_removed)
        elif user_input == 4:
            id_ = ui.get_inputs(['Choose ID which do want update: '], "Please provide your personal information")
            update(table, id_)
        elif user_input == 5:
            get_counts_by_manufacturers(table)
        elif user_input == 6:
            get_average_by_manufacturer(table, id)
        elif user_input == 0:
            in_menu = False #dopóki jest w menu i prosi o input, dopóty nie dostanie 0 pętla się powtarza a jak się przerwie, user wychodzi itd. 


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    title_list = ["Id", "Title", "Manufacturer", "Price", "In Stock"]
    ui.print_table(table, title_list) #z UI tabelka


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    id_  = common.generate_random(table)

    list_labels = ["Title", "Manufacturer", "Price", "In Stock"]
    title = "Please provide data for new entry"
    new_entry = ui.get_inputs(list_labels, title)
    new_record = ([id_, new_entry[0], new_entry[1], new_entry[2], new_entry[3]])
    table.append(new_record)
    label = "This is your record after changes"
    ui.print_result(new_record, label)
    data_manager.write_table_to_file("store/games.csv", table)
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
    file_name = "store/games.csv"
    count = 0
    for entry in table:
        temp_row = entry
        entry = str(entry[0])
        entry_in_list_form = entry.split(",")
        if entry_in_list_form[0] == id[0]:
            new_table = table[:count] + table[count+1:]
            ui.print_result(temp_row, f"You removed this record")
            data_manager.write_table_to_file(file_name, new_table)
        count += 1
    start_module()

    #return table<<<<<<<<<<<<<<<<<<<<<<<<<why?


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """
    id_ = ("".join(map(str, id_)))
    index_table = 0
    for row in table:
        if row[0] == id_:
            ui.print_result(row, f"This is position what do you want change ")
            datauser = ui.get_inputs(['input Title: ', 'Choose new manufacturer :  ', "Enter new price", "Change amout of stock in storage"], "Please insert new information")
            table[index_table][1:] = datauser
            ui.print_result(table[index_table],f"This is your record after changes")
        index_table += 1
    data_manager.write_table_to_file("store/games.csv", table)
    start_module()
    
    return table 
    

# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    count_manufactor = {}
    for row in table:
        if row[2] in count_manufactor:
            count_manufactor[row[2]] += int(row[4]) # 2 manufactor 4 amount 
        else:
            count_manufactor[row[2]] = int(row[4])

    ui.print_result(count_manufactor,f"Manufactor counts")
    start_module()


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """

    # your code
