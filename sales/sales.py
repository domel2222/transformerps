""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
    * customer_id (string): id from the crm
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common
# main module
import main

title_list = ["Id", "Title", "Price", "Month", "Day", "Year", "customer_id"]
file_name = "sales/sales.csv"


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
        ui.print_menu("Sales", [
            "Show Table", "Add", "Remove", "Update",
            "Get Lowest Price Item Id", "Show all customers" , 
            " ", 
            " ",
            "sales_per_customer"
        ], "Back to Main Menu")
        user_input = ui.get_input_menu(len(title_list))  #asks user to select numbered option from the menu
        table = data_manager.get_table_from_file(file_name)
        if user_input == 1:
            show_table(data_manager.get_table_from_file(file_name))
        elif user_input == 2:
            add(table)
        elif user_input == 3:
            file_in_list_form = data_manager.get_table_from_file(file_name)
            list_labels = ["Id"]
            title = "Please provide Id from entry you want to change"
            id_from_entry_to_be_changed = ui.get_inputs(list_labels, title)
            remove(file_in_list_form, id_from_entry_to_be_changed)
        elif user_input == 4:
            id_ = ui.get_inputs(['Choose ID which do you want update:  '],
                                "Please provide your personal information")
            update(table, id_)
        elif user_input == 5:
            get_lowest_price_item_id(table)
        elif user_input == 6:
            ui.print_result(get_all_customer_ids(), "See all customers below")
            ui.print_result(" ", " ")
        # elif user_input == 7:
        #     get_items_sold_between(table)








        elif user_input == 9:
            table = data_manager.get_table_from_file(file_name)
            get_num_of_sales_per_customer_ids_from_table(table)
        elif user_input == 0:
            main.main()
S

def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    title_list = [
        "Id", "Title", "Price", "Month", "Day", "Year", "customer_id"
    ]
    ui.print_table(table, title_list)  #z UI tabelka


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    id_ = common.generate_random(table)

    list_labels = [
        "Title: ", "Price: ", "Month: ", "Day: ", "Year: ", "customer_id: "
    ]
    title = "Please provide data for new entry"
    new_entry = ui.get_inputs(list_labels, title)
    table.append([
        id_, new_entry[0], new_entry[1], new_entry[2], new_entry[3],
        new_entry[4], new_entry[5]
    ])
    data_manager.write_table_to_file(file_name, table)
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
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    index_table = 0
    for row in table:
        if table[index_table][0] == str(id_[0]):
            ui.print_result(row, f"This is sales which you choose ")
            datauser = ui.get_inputs([
                "Title: ", "Price: ", "Month: ", "Day: ", "Year: ", "crm_id: "
            ], "Please insert new information")
            table[index_table][1:] = datauser
            ui.print_result(table[index_table],
                            f"This is your record after changes")
        index_table += 1
    data_manager.write_table_to_file(file_name, table)
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


def get_items_sold_between(table, month_from, day_from, year_from, month_to,
                           day_to, year_to):
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


# functions supports data abalyser
# --------------------------------


def get_title_by_id(id):
    """
    Reads the table with the help of the data_manager module.
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the item

    Returns:
        str: the title of the item
    """

    # your code


def get_title_by_id_from_table(table, id):
    """
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the sales table
        id (str): the id of the item

    Returns:
        str: the title of the item
    """

    # your code


def get_item_id_sold_last():
    """
    Reads the table with the help of the data_manager module.
    Returns the _id_ of the item that was sold most recently.

    Returns:
        str: the _id_ of the item that was sold most recently.
    """

    # your code


def get_item_id_sold_last_from_table(table):
    """
    Returns the _id_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _id_ of the item that was sold most recently.
    """

    # your code


def get_item_title_sold_last_from_table(table):
    """
    Returns the _title_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _title_ of the item that was sold most recently.
    """

    # your code


def get_the_sum_of_prices(item_ids):
    """
    Reads the table of sales with the help of the data_manager module.
    Returns the sum of the prices of the items in the item_ids.

    Args:
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """

    # your code


def get_the_sum_of_prices_from_table(table, item_ids):
    """
    Returns the sum of the prices of the items in the item_ids.

    Args:
        table (list of lists): the sales table
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """

    # your code


def get_customer_id_by_sale_id(sale_id):
    """
    Reads the sales table with the help of the data_manager module.
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
         sale_id (str): sale id to search for
    Returns:
         str: customer_id that belongs to the given sale id
    """

    # your code


def get_customer_id_by_sale_id_from_table(table, sale_id):
    """
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
        table: table to remove a record from
        sale_id (str): sale id to search for
    Returns:
        str: customer_id that belongs to the given sale id
    """

    # your code


def get_all_customer_ids():
    """
    Reads the sales table with the help of the data_manager module.

    Returns:
         set of str: set of customer_ids that are present in the table
    """

    sales_tab = data_manager.get_table_from_file(file_name)
    customers_ids = {}
    for line in sales_tab:
        customers_ids[line[6]] = 0
    result = list(customers_ids.keys())
    return result


def get_all_customer_ids_from_table(table):
    """
    Returns a set of customer_ids that are present in the table.

    Args:
        table (list of list): the sales table
    Returns:
         set of str: set of customer_ids that are present in the table
    """

    # your code


def get_all_sales_ids_for_customer_ids():
    """
    Reads the customer-sales association table with the help of the data_manager module.
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)

    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
            all the sales id belong to the given customer_id
    """

    # your code


def get_all_sales_ids_for_customer_ids_from_table(table):
    """
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
    Args:
        table (list of list): the sales table
    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
         all the sales id belong to the given customer_id
    """

    # your code


def get_num_of_sales_per_customer_ids():
    """
     Reads the customer-sales association table with the help of the data_manager module.
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    # your code


def get_num_of_sales_per_customer_ids_from_table(table):
    """
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Args:
        table (list of list): the sales table
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    ID_Clent = 6
    dict_sales = {}

    for record in table:
        if record[ID_Clent] in dict_sales:
            dict_sales[record[ID_Clent]] += 1
        else:
            dict_sales[record[ID_Clent]] = 1

    
    ui.print_result(dict_sales, "Customer id and num of sales")
    start_module()


