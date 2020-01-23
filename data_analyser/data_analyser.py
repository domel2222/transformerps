"""
This module creates reports for the marketing department.
This module can run independently from other modules.
Has no own data structure but uses other modules.
Avoid using the database (ie. .csv files) of other modules directly.
Use the functions of the modules instead.
"""

# todo: importing everything you need

# importing everything you need
import ui
import common
from sales import sales
from crm import crm
import data_manager


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    title = "Data Analyser"
    list_options = [
        'Last buyer name', 'Last buyer id',
        'Buyer name with the most money spent',
        'Buyer id with the most money spent',
        'Show most frequent buyers names', 'Show the most frequent buyers ids'
    ]
    exit_message = "Go back to main menu"
    ui.print_menu(title, list_options, exit_message)
    option = ui.get_input_menu(len(list_options))
    if option == 1:
        get_the_last_buyer_name()
        ui.print_result(get_the_last_buyer_name(),"The name of the last customer is:")
        start_module()
    elif option == 2:
        get_the_last_buyer_id()
    elif option == 3:
        ui.print_result(get_the_buyer_name_spent_most_and_the_money_spent(),
                        "The name of customer spent most money is: ")
        start_module()
    elif option == 4:
        ui.print_result(get_the_buyer_id_spent_most_and_the_money_spent(),
                        "The id of customer spent most money is: ")
        start_module()
    elif option == 5:
        get_the_most_frequent_buyers_names(num=1)
    elif option == 6:
        get_the_most_frequent_buyers_ids(num=1)
    elif option == 0:
        pass
    else:
        raise KeyError("There is no such option.")

    # your code


def get_the_last_buyer_name():
    """
    Returns the customer _name_ of the customer made sale last.

    Returns:
        str: Customer name of the last buyer
    """
    return crm.get_name_by_id(get_the_last_buyer_id())
    # your code


def get_the_last_buyer_id():
    """
    Returns the customer _id_ of the customer made sale last.

    Returns:
        str: Customer id of the last buyer
    """
    return sales.get_customer_id_by_sale_id(sales.get_item_id_sold_last())
    # your code


def get_the_buyer_name_spent_most_and_the_money_spent():
    """
    Returns the customer's _name_ who spent the most in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer name and the sum the customer spent eg.: ('Daniele Coach', 42)
    """
    table_crm = data_manager.get_table_from_file("crm/customers.csv")
    max_key = get_the_buyer_id_spent_most_and_the_money_spent()[0]
    for index, line in enumerate(table_crm):
        if max_key in line[0]:
            max_index = index
    max_money = get_the_buyer_id_spent_most_and_the_money_spent()[1]
    return (table_crm[max_index][1], max_money)


def get_the_buyer_id_spent_most_and_the_money_spent():
    """
    Returns the customer's _id_ who spent more in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer id and the sum the customer spent eg.: (aH34Jq#&, 42)
    """
    table_sales = data_manager.get_table_from_file("sales/sales.csv")
    cust_sales_dict = {}
    for line in table_sales:
        cust_sales_dict[line[6]] = 0
    for line in table_sales:
        if line[6] in cust_sales_dict.keys():
            cust_sales_dict[line[6]] += int(line[2])
    max_key = max(cust_sales_dict, key=cust_sales_dict.get)
    result = tuple((max_key, cust_sales_dict[max_key]))
    return result


def get_the_most_frequent_buyers_names(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer's name) who bought most frequently in an
    ordered list of tuples of customer names and the number of their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer names and num of sales
            The first one bought the most frequent. eg.: [('Genoveva Dingess', 8), ('Missy Stoney', 3)]
    """
    sales_file_name = "sales/sales.csv"
    crm_file_name = "crm/customers.csv"
    label = "the most frequent buyers name is: "
    sales_table = data_manager.get_table_from_file(sales_file_name)
    crm_table = data_manager.get_table_from_file(crm_file_name)
    dict_sales_count = {}
    for row in sales_table:
        if row[6] in dict_sales_count.keys():
            dict_sales_count[row[6]] += 1
        else:
            dict_sales_count[row[6]] = 1
    
    id_buyer = max(dict_sales_count, key=dict_sales_count.get)
    
    name_customer = []
    for row in crm_table:
        if row[0] == id_buyer:
            name_customer.append(row[1])
    
    ui.print_result(name_customer[num - 1],label)



def get_the_most_frequent_buyers_ids(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer ids of them) who bought more frequent in an
    ordered list of tuples of customer id and the number their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer ids and num of sales
            The first one bought the most frequent. eg.: [(aH34Jq#&, 8), (bH34Jq#&, 3)]
    """

    sales_file_name = "sales/sales.csv"
    label = "the most frequent buyers ids is: "

    sales_table = data_manager.get_table_from_file(sales_file_name)
    
    dict_sales_count = {}
    for row in sales_table:
        if row[6] in dict_sales_count.keys():
            dict_sales_count[row[6]] += 1
        else:
            dict_sales_count[row[6]] = 1
    
    id_buyer = max(dict_sales_count, key=dict_sales_count.get)
    print(type(id_buyer))
    ui.print_result(id_buyer,label)

