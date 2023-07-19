import sqlite3

try:
    # pass database name to establish connection to SQLite
    sqliteConnection = sqlite3.connect('cookiejar.db')
    # create a cursor object to execute SQLite command/queries from Python
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    sqlite_select_Query = "select sqlite_version();"
    # execute will run SQL query and return result
    cursor.execute(sqlite_select_Query)
    # fetchall will read query result
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)
    # close cursor
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:
        # close connection
        sqliteConnection.close()
        print("The SQLite connection is closed")
