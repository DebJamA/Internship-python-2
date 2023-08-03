# Create 'Ingredients' Class and DB Table (py-2-3)  
  
---  
  
## Make sure the system is set up properly  
  
1. Make sure you are in the pipenv **(Internship-python-2) %** directory  
  
2. Create and switch to new branch ***Internship-py-2-3***  
  
3. If `pypyodbc` is not working - [setting up odbc drivers](https://solutions.posit.co/connections/db/best-practices/drivers/#setting-up-database-connections-1) for SQLite with a helpful [video](https://www.youtube.com/watch?v=id0GX4sXnyI)  
  
___  
  
## Data modeling: SQL schema  
  
1. Design relational db management system for `cookiejar.db` using [DBDiagram.io](https://dbdiagram.io/home)  
  
![cookiejar.db schema diagram](https://raw.githubusercontent.com/DebJamA/Internship-python-2/Internship-py-2-3/rdms_cookiejar.png)  
  
2. Create `tables.py` to create all tables  
- include `FOREGN KEY` where necessary  
- run `python3 tables.py`  
  
```  
Output:  

***********************************
Connection open

Successfully created 4 tables:
('cookie',)
('cookie_ingredient',)
('ingredient',)
('sqlite_sequence',)

sqlite_sequence table was automatically created
and initialized because normal table 'cookie'
contains AUTOINCREMENT column

Connection closed
***********************************

```  
  
___  
  
## Database query  
  
1. Re-populate table **cookie** with data and pre-populate table **ingredient** and table **cookie_ingredient** using DB Browser for SQLite  
  
2. Check data in sqlite shell  
```
sqlite> .mode column
sqlite> SELECT * FROM cookie;
id_cookie  cookie_name    instructions          price
---------  -------------  --------------------  -----
1          first cookie   step1, step2,  step3  15   
2          second cookie  step1, step2,  step3  9    
3          third cookie   step1, step2,  step3  8    
4          delete cookie  step1, step2,  step3  99   
5          fifth cookie  step1, step2,  step3  3    

sqlite> SELECT * FROM ingredient;
id_ingredient  ingredient_name    cost 
-------------  -----------------  -----
1              first ingredient   13.49
2              second ingredient  6.99 
3              third ingredient   2.48 
4              delete ingredient  99.99
5              fifth ingredient   1.67 

sqlite> SELECT * FROM cookie_ingredient;
id_cookie  id_ingredient  measure  
---------  -------------  ---------
1          1              1 1/2 cup
1          2              1/2 tsp  
1          3              1 stick  
1          5              1 tbsp   
2          1              2 cup    
2          5              1/2 tbsp 
3          1              2 1/4 cup
3          3              2 sticks 
3          5              2 tbsp   
5          1              2 1/2 cup
5          2              1/4 tsp
```
  
3. Create `ingredients.py`  
  
- Create `class Ingredients` and define functions for CRUD operations for table  
 **ingredient**:  
	- `INSERT` **ingredient** - ingredient_name and cost  
	- `SELECT` all **ingredient** to view list of each ngredient_name and cost  
	- `UPDATE` a selected **ingredient** cost  
	- `DELETE` a selected **ingredient** from the db  
  
4. Update `cookies.py` to include additional functions:  
	- Sort all **cookie** by **price**  
	- Get all **ingredient** for a selected **cookie**  
	- Get total **cost** of all **ingredient** for a selected **cookie**  
  
5. Update `main.py` to run the app  
  
6. Update `README.md`  
  
___  
  
## Run the app  
  
1. `(Internship-python-2)% python3 main.py`  
	-- Make sure everything is working  
```
You have 6 cookie recipes in your Cookie Jar:

ID:  1
Cookie:  first cookie
Price: $ 15

ID:  2
Cookie:  second cookie
Price: $ 9

ID:  3
Cookie:  third cookie
Price: $ 8

ID:  4
Cookie:  delete cookie
Price: $ 99

ID:  5
Cookie:  fifth cookie
Price: $ 3

ID:  6
Cookie:  sixth cookie
Price: $ 7

**********
There are 6 ingredients in your Cookie Jar:

ID:  1
Ingredient:  first ingredient
Cost: $ 13.49

ID:  2
Ingredient:  second ingredient
Cost: $ 6.99

ID:  3
Ingredient:  third ingredient
Cost: $ 2.48

ID:  4
Ingredient:  delete ingredient
Cost: $ 99.99

ID:  5
Ingredient:  fifth ingredient
Cost: $ 1.67

ID:  6
Ingredient:  sixth ingredient
Cost: $ 5.29

**********
There are 12 recipes in your Cookie Jar:

(1, 1, '1 1/2 cup')
(1, 2, '1/2 tsp')
(1, 3, '1 stick')
(1, 5, '1 tbsp')
(2, 1, '2 cup')
(2, 5, '1/2 tbsp')
(3, 1, '2 1/4 cup')
(3, 3, '2 sticks')
(3, 5, '2 tbsp')
(5, 1, '2 1/2 cup')
(5, 2, '1/4 tsp')
(2, 6, '14 oz')

**********
Sorting 5 cookies by price:

(5, 'fifth cookie', 'step1, step2,  step3', 3)
(1, 'first cookie', 'step1, step2,  step3', 5)
(6, 'sixth cookie', 'step1, step2, step3', 7)
(3, 'third cookie', 'step1, step2,  step3', 8)
(2, 'second cookie', 'step1, step2,  step3', 9)

***** Get all ingredients for each cookie *****
('fifth cookie', '2 1/2 cup', 'first ingredient', 3.49)
('fifth cookie', '1/4 tsp', 'second ingredient', 6.99)
('first cookie', '1 tbsp', 'fifth ingredient', 1.67)
('first cookie', '1 1/2 cup', 'first ingredient', 3.49)
('first cookie', '1/2 tsp', 'second ingredient', 6.99)
('first cookie', '1 stick', 'third ingredient', 2.48)
('second cookie', '1/2 tbsp', 'fifth ingredient', 1.67)
('second cookie', '2 cup', 'first ingredient', 3.49)
('second cookie', '14 oz', 'sixth ingredient', 5.29)
('third cookie', '2 tbsp', 'fifth ingredient', 1.67)
('third cookie', '2 1/4 cup', 'first ingredient', 3.49)
('third cookie', '2 sticks', 'third ingredient', 2.48)

***** Total cost of ingredients for each cookie *****
Cookie:  fifth cookie
Total Cost: $ 10.48

Cookie:  first cookie
Total Cost: $ 14.63

Cookie:  second cookie
Total Cost: $ 10.45

Cookie:  third cookie
Total Cost: $ 7.64
```
  
2. Push to GitHub:  
 
	a. `(Internship-python-2)% git add .`  
  
	b. `(Internship-python-2)% git commit -m "created relational db schema"`   
  
	c. `(Internship-python-2)% git push cookie Internship-py-2-3`  
  
---  
