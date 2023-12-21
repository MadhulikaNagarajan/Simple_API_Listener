import sqlite3
# import functools


# user_data = 'Admin', 'Admin@123'


# def __init__(self, connection):
#     self.connection = connection


def create_user_table():
    connection = sqlite3.connect('userdata.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS User_Data(Sno INTEGER PRIMARY KEY,Username text,Password text)')
    connection.commit()
    connection.close()

def get_user_data():
    connection = sqlite3.connect('userdata.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM User_Data')
    return cursor.fetchall()
    # connection.close()


def insert_user_data(Username):
    connection = sqlite3.connect('userdata.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO User_Data(Username, Password)VALUES(?,?)', Username)
    connection.commit()
    connection.close()


def update_user_data(entered_username, entered_password):
    connection = sqlite3.connect('userdata.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM User_Data Where Username =?', (entered_username,))
    if cursor.fetchall() == []:
        return 'user not found'
    else:
        cursor.execute('UPDATE User_Data SET Username =?, Password =? Where Username = ?',
                       (entered_username, entered_password, entered_username,))
        connection.commit()
        connection.close()
        return "User data updated successfully"


def delete_user_data(user_data):
    connection = sqlite3.connect('userdata.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM User_Data Where Username =?', (user_data,))
    # result =
    if cursor.fetchall() == []:
        return 'user not found'
    else:
        cursor.execute('DELETE FROM User_Data Where Username = ?', (user_data,))
        connection.commit()
        connection.close()
        return "User data deleted successfully"


# @functools.lru_cache(maxsize=2)
def authorise_user_data(user_data):
    connection = sqlite3.connect('userdata.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM User_Data Where Username = ?', (user_data,))
    return cursor.fetchall()



# get_user_data()
