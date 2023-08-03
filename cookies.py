import pypyodbc

#CRUD for cookies
class Cookies:
    #connect cookiejar to project
    def __init__(self):
        try:
            self.con = pypyodbc.connect("DRIVER=SQLite Driver;"
                                        "SERVER=localhost;"
                                        "DATABASE=cookiejar.db;"
                                        "Trusted_connection=yes;")
            self.cur = self.con.cursor()
            print("\n*************** COOKIE *****\nCookie Jar open\n")
            simco = self.cur.fetchall()
            print("Simco Cookie Jar initialized\n", simco)
        except pypyodbc.Error as error:
            print("ERROR Message:", error)
            print("***** COOKIES *****\n")

    #add new cookie to table cookie - Crud
    def insert_cookie(self, cookie_name, instructions, price):
        try:
            # define query with placeholders
            sql_insert_cookie = """INSERT INTO cookie
                            (cookie_name, instructions, price) 
                            VALUES (?, ?, ?);"""

            # specify 3 Python variables in sequential order to create insert_data tuple
            insert_cookie = (cookie_name, instructions, price)
            self.cur.execute(sql_insert_cookie, insert_cookie)
            self.con.commit()
        finally:
            print("new cookie added to table cookie\n**********\n")

    #display all cookies in table cookie - cRud
    def get_all_cookies(self):
        try:
            #define query
            sql_select_cookie = """SELECT id_cookie, cookie_name, price FROM cookie"""
            self.cur.execute(sql_select_cookie)

            # extract results
            cookielist = self.cur.fetchall()

            # count results
            getck1 = 'You have '
            num = len(cookielist)
            getck2 = ' cookie recipes in your Cookie Jar:\n'
            print(f'{getck1}{num}{getck2}')

            #return list of rows from result
            #iterate each row
            for row in cookielist:
                print("ID: ", row[0])
                print("Cookie: ", row[1])
                print("Price: $", row[2])
                print("\n")
        finally:
            print("cookies cookies cookies - yummm\n**********\n")

    #update price by cookie_name - crUd
    def update_cookie(self, cookie_name, price):
        try:
            #define query with placholders for cookie and price columns
            sql_update_ckprice = """UPDATE cookie SET price = ? WHERE cookie_name = ?"""
            #specify 2 Python variables in sequential order to create update_data tuple
            update_cookie_price = (price, cookie_name)
            self.cur.execute(sql_update_ckprice, update_cookie_price)
            self.con.commit()
        finally:
            print("the price has been updated\n**********\n")

    #delete a recipe from cookiejar db by id_cookie - cruD
    def delete_cookie(self, id_cookie):
        try:
            #use Python variable in the query to delete row
            sql_delete_cookie = """DELETE FROM cookie WHERE id_cookie = ?"""
            self.cur.execute(sql_delete_cookie, (id_cookie,))
            self.con.commit()
        finally:
            print("cookie deleted from Cookie Jar\n**********\n")

# other functions
    # add recipe to table cookie_ingredient
    def insert_recipe(self, id_cookie, id_ingredient, measure):
        try:
            # define query with placeholders
            sql_insert_recipe = """INSERT INTO cookie_ingredient
                            (id_cookie, id_ingredient, measure) 
                            VALUES (?, ?, ?);"""

            # specify 3 Python variables in sequential order to create insert_data tuple
            insert_list = (id_cookie, id_ingredient, measure)
            self.cur.execute(sql_insert_recipe, insert_list)
            self.con.commit()
        finally:
            print("new recipes added to table cookie_ingredient\n**********\n")

    # display all recipes in table cookie_ingredient
    def get_all_recipes(self):
        try:
            # define query
            sql_select_recipes = """SELECT * FROM cookie_ingredient"""
            self.cur.execute(sql_select_recipes)
            recipelist = self.cur.fetchall()
            getrec1 = 'There are '
            num = len(recipelist)
            getrec2 = ' recipes in your Cookie Jar:\n'
            print(f'{getrec1}{num}{getrec2}')

            for item in recipelist:
                print(item)
        finally:
            print("listed all recipes\n**********\n")

    # order cookies by price - low to high
    def order_cookies_by_price(self):
        try:
            # define query
            sql_order_cookies_by_price = """SELECT * FROM cookie ORDER BY price"""
            self.cur.execute(sql_order_cookies_by_price)
            ordercookielist = self.cur.fetchall()

            # count results
            orderck1 = 'Sorting '
            num = len(ordercookielist)
            orderck2 = ' cookies by price:\n'
            print(f'{orderck1}{num}{orderck2}')

            # return list of rows from result
            # iterate each row
            for item in ordercookielist:
                print(item)
        finally:
            print("cookies sorted by price\n**********\n")

    #display all ingredients for a selected cookie
    def get_ingredients_for_cookie(self):
        try:
            sql_get_cookie_ingredients = """SELECT cookie.cookie_name, cookie_ingredient.measure, 
                                        ingredient.ingredient_name, ingredient.cost
                                        FROM cookie 
                                        INNER JOIN cookie_ingredient ON cookie.id_cookie = cookie_ingredient.id_cookie
                                        INNER JOIN ingredient ON ingredient.id_ingredient = 
                                        cookie_ingredient.id_ingredient
                                        GROUP BY cookie.cookie_name, ingredient.ingredient_name"""
            self.cur.execute(sql_get_cookie_ingredients)
            ckinglist = self.cur.fetchall()

            for item in ckinglist:
                print(item)
        finally:
            print("listed all ingredients for each cookie\n**********\n")

    #get the cost of all inredients for a selected cookie
    def get_cost_ingredients_for_cookie(self):
        try:
            sql_get_cost_ingredients_for_cookie = """SELECT cookie.cookie_name,
                                        SUM(ingredient.cost)
                                        FROM cookie 
                                        INNER JOIN cookie_ingredient ON cookie.id_cookie = cookie_ingredient.id_cookie
                                        INNER JOIN ingredient ON ingredient.id_ingredient = 
                                        cookie_ingredient.id_ingredient
                                        GROUP BY cookie.cookie_name"""
            self.cur.execute(sql_get_cost_ingredients_for_cookie)
            totalcost = self.cur.fetchall()

            for row in totalcost:
                print("Cookie: ", row[0])
                print("Total Cost: $", row[1])
                print("\n")
        finally:
            print("sum cost of all ingredients for each cookie\n**********\n")

    #close connection
    def end(self):
        if self.con:
            self.cur.close()
            self.con.close()
        print("\n***********************************\ncookie: Cookie Jar closed\n")
