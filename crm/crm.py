""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
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

    title = "CRM"
    list_options = ['Show table','Add new entry','Remove a record','Update specific record','Show id of the customer with the longest name','Show customers who are subscribed to the newsletter']
    exit_message = "Go back to main menu"
    ui.print_menu(title, list_options, exit_message)
    number_of_menu_options = 7
    file_name = "crm/customers.csv"
    user_input = ui.get_input_menu(number_of_menu_options-1)
    if user_input == 1:
        show_table(data_manager.get_table_from_file("crm/customers.csv"))
    elif user_input == 2:
        file_in_list_form = data_manager.get_table_from_file(file_name)
        add(file_in_list_form)
    elif user_input == 3:
        file_in_list_form = data_manager.get_table_from_file(file_name)
        list_labels = ["Id"]
        title = "Please provide Id from entry you want to change"
        id_from_entry_to_be_changed = ui.get_inputs(list_labels, title)
        remove(file_in_list_form, id_from_entry_to_be_changed)
    elif user_input == 4:
        update(table, id_)
    elif user_input == 5:
        get_longest_name_id(table)
    elif user_input == 6:
        get_subscribed_emails(table)
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
    title_list = ['id','name','email','subscribed']
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
    file_name = "crm/customers.csv"
    list_labels = ['Id:','Name:','Email:','Subscribed:']
    title = "Please provide data for new entry"
    new_entry = ui.get_inputs(list_labels, title)
    table_after_change = table + [[",".join(new_entry)]]
    data_manager.write_table_to_file(file_name, table_after_change)
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

    file_name = "crm/customers.csv"
    count = 0
    for entry in table:
        entry = str(entry[0])
        entry_in_list_form = entry.split(";")
        if entry_in_list_form[0] == id[0]:
            new_table = table[:count] + table[count+1:]
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

    # your code

    return table


# special functions:
# ------------------

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """

    table = data_manager.get_table_from_file("crm/customers.csv")
    longest_name = table[0][1]
    result = table[0][0]
    for line in table:
        if len(line[1]) >= len(longest_name) and line[1][0] >= longest_name[0]:
            longest_name = line[1]
            result = line[0]
    return result


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """

    # your code
