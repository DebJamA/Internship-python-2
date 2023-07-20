import sqlite3

try:
    #create new db and open db connection
    sqliteConnection = sqlite3.connect('cookiejar.db')
    sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS cookies (
                id_cookies INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                name TEXT NOT NULL,
                quantity TEXT NOT NULL,
                price INTEGER);'''

    cursor = sqliteConnection.cursor()
    cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit()
finally:
    print("SQLite table cookies already exists")

class Cookies:
    #connect cookiejar to project
    def __init__(self):
        try:
            self.con = sqlite3.connect('cookiejar.db')
            self.cur = self.con.cursor()
            print("Connected to SQLite")
            simco = self.cur.fetchall()
            print("Simco Cookie Jar initialized", simco)
        except sqlite3.Error as error:
            print("SQLite ERROR Message:", error)

    # display all recipes in the table - cRud
    def get_all(self):
        try:
            #define query
            sql_select_query = """SELECT * from cookies"""
            self.cur.execute(sql_select_query)
            #extract results
            recipes = self.cur.fetchall()
            #return list of rows from result
            print("Total rows are:  ", len(recipes))
            #iterate each row
            print("Printing each row")
            for row in recipes:
                print("ID: ", row[0])
                print("Name: ", row[1])
                print("Quantity: ", row[2])
                print("Price: ", row[3])
                print("\n")
        finally:
            print("end cookie recipes - yummm")

    # add a recipe to cookies table - Crud
    def insert_cookies(self, name, quantity, price):
        try:
            # define query with placeholders
            sql_insert_query = """INSERT INTO cookies
                            (name, quantity, price) 
                            VALUES (?, ?, ?);"""

            # specify 3 Python variables in sequential order to create insert_data tuple
            insert_data = (name, quantity, price)
            self.cur.execute(sql_insert_query, insert_data)
            self.con.commit()
        finally:
            print("recipe has been added to table cookies")

    # update price by name - crUd
    def update_cookies(self, name, price):
        try:
            #define query with placholders for name and price columns
            sql_update_query = """Update cookies set price = ? where name = ?"""
            #specify 2 Python variables in sequential order to create update_data tuple
            update_data = (price, name)
            self.cur.execute(sql_update_query, update_data)
            self.con.commit()
        finally:
            print("the price has been updated")

    #delete a recipe from cookiejar db by id_cookies - cruD
    def delete_cookies(self, id_cookies):
        try:
            #use Python variable in the query to delete row
            sql_delete_query = """DELETE from cookies where id_cookies = ?"""
            self.cur.execute(sql_delete_query, (id_cookies,))
            self.con.commit()
        finally:
            print("recipe deleted from db cookiejar")

    #close connection
    def end(self):
        if self.con:
            self.cur.close()
            self.con.close()
            print("table cookies is closed")
