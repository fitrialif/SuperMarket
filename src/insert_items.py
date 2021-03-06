import sqlite3
from view_details import view_items

D_BASE_URL = "/home/chakri/SQLite/smarket_db.sqlite"


def insert_items():
    view_items()
    item_name_local = str(raw_input("Enter Item name : "))
    item_price_local = int(raw_input("Enter Item Price : "))
    conn_local = sqlite3.connect(D_BASE_URL)
    cur_bill = conn_local.cursor()
    cur_bill.execute('''INSERT INTO items(item_name, item_price) VALUES (?, ?)''', (item_name_local, item_price_local))
    f_choice = int(raw_input("Want to enter another item"))
    conn_local.commit()
    if f_choice:
        insert_items()
    conn_local.close()


def insert_items_gui(item_name_gui, item_price_gui):
    connection_gui = sqlite3.connect(D_BASE_URL)
    csr_gui = connection_gui.cursor()
    csr_gui.execute('''INSERT INTO items(item_name, item_price) VALUES (?, ?)''', (str(item_name_gui), int(item_price_gui)))
    print csr_gui.description
    connection_gui.commit()
    connection_gui.close()
