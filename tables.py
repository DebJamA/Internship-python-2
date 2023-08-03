import pypyodbc

con = pypyodbc.connect("DRIVER=SQLite Driver;SERVER=localhost;DATABASE=cookiejar.db;Trusted_connection=yes;")
cur = con.cursor()
print("\n***********************************\nConnection open\n")

# create all necessary tables
cur.execute("""CREATE TABLE IF NOT EXISTS cookie (
            id_cookie INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            cookie_name TEXT NOT NULL,
            instructions TEXT NOT NULL,
            price INTEGER NOT NULL)""")

cur.execute("""CREATE TABLE IF NOT EXISTS ingredient
            (id_ingredient INTEGER PRIMARY KEY NOT NULL,
            ingredient_name TEXT NOT NULL, 
            cost REAL NOT NULL)""")

cur.execute("""CREATE TABLE IF NOT EXISTS cookie_ingredient
            (id_cookie INTEGER,
            id_ingredient INTEGER,
            measure TEXT NOT NULL,
            FOREIGN KEY (id_cookie) REFERENCES cookie (id_cookie),
            FOREIGN KEY (id_ingredient) REFERENCES ingredient (id_ingredient))""")

con.commit()

sql = """SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"""
cur.execute(sql)

tables = cur.fetchall()
tb1 = 'Successfully created '
num = len(tables)
tb2 = ' tables:'
print(f'{tb1}{num}{tb2}')

for item in tables:
    print(item)

print("\nsqlite_sequence table was automatically created\nand initialized because normal table 'cookie'\ncontains "
      "AUTOINCREMENT column\n")

cur.close()
con.close()
print("Connection closed\n***********************************\n")
