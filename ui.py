""" User Interface (UI) module """


def column_width_counter(label_list, table):
    columns_width = []
    for column in range(len(label_list)):
        max = 0
        for record in range(len(table)):
            
            if len(table[record][column]) >= max:
                max = len(table[record][column])    
            
        columns_width.append(max)
    return columns_width


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    table.insert(0, title_list)

    # getting column width for a table
    columns_width = column_width_counter(title_list, table)

    edges_control = 1
    table_width = len(columns_width) - edges_control
    for item in columns_width:
        table_width += item

    break_line = '|'
    for num in columns_width:
        break_line += num*'-' + '|'

    print('/' + "-" * table_width + '\\')
    for position in table[:-1]:
        print("|", end="")
        for position_index, column in enumerate(position):
            print("{0:^{1}}".format(column, columns_width[position_index]), end ="|")
        print('')
        print(break_line)
    print("|", end="")
    for position_index, column in enumerate(table[-1]):    
        print("{0:^{1}}".format(column, columns_width[position_index]), end ="|")
    print('\n' + '\\' + "-" * table_width + '/')


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, number, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print(label)
    if type(result) == str or type(result) == int:
        print(result)
    elif type(result) == list:
        for item in result:
            print(item + " | ", end="")
    elif type(result) == dict:
        for key, value in result.items():
            print(str(key) + ": " + str(value))
    elif type(result) == tuple:
        print(result)
    else:
        print("I can't process this type of data")


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print(title)
    for index, option in enumerate(list_options):
        print(f'\t({index + 1}) {option}')
    print(f'\t(0) {exit_message}')

def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        ui.get_inputs()title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []
    print (title)
    for item in list_labels:
        user_input = input(f'{item}: ')
        inputs.append(user_input)

    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print("Unfortunately an error occured. This is the error message: {}".format(message))


def get_input_menu(menu_options):
    """
    Takes an integer as parameter = number of options in menu
    Returns an input integer if valid
    This function is for all options - all normal functionalities and option 
    "0" that exits to main Menu.
    """

    verifier = True
    while verifier:
        try:
            menu_choice = int(input('Choose an option from menu: '))
        except:
            print("Please choose a NUMBER.")
        else:
            if menu_choice in range(menu_options + 1):
                return menu_choice
            else:
                print("Your choice is not on the list.")
