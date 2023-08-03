import pypyodbc

#CRUD for ingredients
class Ingredients:
    # connect cookiejar to project
    def __init__(self):
        try:
            self.con = pypyodbc.connect("DRIVER=SQLite Driver;"
                                        "SERVER=localhost;"
                                        "DATABASE=cookiejar.db;"
                                        "Trusted_connection=yes;")
            self.cur = self.con.cursor()
            print("\n*************** INGREDIENT *****\nCookie Jar open\n")
            simco = self.cur.fetchall()
            print("Simco Cookie Jar initialized\n", simco)
        except pypyodbc.Error as error:
            print("ERROR Message:", error)
            print("***** INGREDIENTS *****\n")

    # add new ingredient to table ingredient - Crud
    def insert_ingredient(self, ingredient, cost):
        try:
            # define query with placeholders
            sql_insert_ingredient = """INSERT INTO ingredient
                            (ingredient_name, cost) 
                            VALUES (?, ?);"""

            # specify 2 Python variables in sequential order to create insert_data tuple
            insert_ingredient = (ingredient, cost)
            self.cur.execute(sql_insert_ingredient, insert_ingredient)
            self.con.commit()
        finally:
            print("new ingredient added to table ingredient\n**********\n")

    # display all ingredients in table ingredient - cRud
    def get_all_ingredients(self):
        try:
            # define query
            sql_select_ingredient = """SELECT * FROM ingredient"""
            self.cur.execute(sql_select_ingredient)

            # extract results
            ingredientlist = self.cur.fetchall()

            # count results
            geting1 = 'There are '
            num = len(ingredientlist)
            geting2 = ' ingredients in your Cookie Jar:\n'
            print(f'{geting1}{num}{geting2}')

            # return list of rows from result
            # iterate each row
            for row in ingredientlist:
                print("ID: ", row[0])
                print("Ingredient: ", row[1])
                print("Cost: $", row[2])
                print("\n")
        finally:
            print("high quality ingredients\n**********\n")

    # update cost by ingredient_name - crUd
    def update_ingredient(self, ingredient_name, cost):
        try:
            # define query with placholders for cookie and price columns
            sql_update_ingcost = """UPDATE ingredient SET cost = ? WHERE ingredient_name = ?"""
            # specify 2 Python variables in sequential order to create update_data tuple
            update_data = (cost, ingredient_name)
            self.cur.execute(sql_update_ingcost, update_data)
            self.con.commit()
        finally:
            print("the cost has been updated\n**********\n")

    #delete an ingredient from cookiejar db by id_ingredient - cruD
    def delete_ingredient(self, id_ingredient):
        try:
            # use Python variable in the query to delete row
            sql_delete_ingredient = """DELETE FROM ingredient WHERE id_ingredient = ?"""
            self.cur.execute(sql_delete_ingredient, (id_ingredient,))
            self.con.commit()
        finally:
            print("ingredient deleted from Cookie Jar\n**********\n")

#close connection
    def end(self):
        if self.con:
            self.cur.close()
            self.con.close()
        print("\n***********************************\ningredient: Cookie Jar closed\n")
