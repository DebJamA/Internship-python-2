import cookies as c
import ingredients as i

cookie = c.Cookies()
ingredient = i.Ingredients()

##########CRUD for cookies
#create fifth cookie
cookie.insert_cookie('sixth cookie', 'step1, step2, step3', 7)

#read table cookie
cookie.get_all_cookies()

#update price of first cookie from 15 to 5
cookie.update_cookie('first cookie', 5)

#delete id_cookie 4
cookie.delete_cookie(4)

##########CRUD for ingredients
#create fifth ingredient
ingredient.insert_ingredient('sixth ingredient', 5.29)

#read table ingredient
ingredient.get_all_ingredients()

#update cost of first ingredient from 13.49 to 3.49
ingredient.update_ingredient('first ingredient', 3.49)

#delete id_ingredient 4
ingredient.delete_ingredient(4)

##########other functions
#add recipe to table cookie_ingredient
cookie.insert_recipe(2, 6, '14 oz')

#read table cookie_ingredient
cookie.get_all_recipes()

#sort table cookie by price low to high
cookie.order_cookies_by_price()

#display all ingredients for each cookie
cookie.get_ingredients_for_cookie()

#get the cost of all inredients for each cookie
cookie.get_cost_ingredients_for_cookie()
