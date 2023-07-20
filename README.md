# Create 'cookies' Class and DB Table (py-2-2)  
  
---  
  
## Make sure the system is set up properly  
  
1. Make sure you are in the pipenv **(Internship-python-2) %** directory  
  
2. Create and switch to new branch ***Internship-py-2-2***  
  
	`(Internship-python-2)% git branch`  
	```
	Output:  
	* Internship-py-2-1  
	```  
  
	`(Internship-python-2)% git checkout -b Internship-py-2-2`  
	```
	Output:  
	‘Switched to branch ‘Internship-py-2-2’  
	```  
  
	`(Internship-python-2)% git branch`  
	```
	Output:  
	Internship-py-2-1  
	* Internship-py-2-2  
	```  
  
___  
  
## Create 'cookies' table  
  
1. Create `cookies.py`  
  
	a. Create table **cookies** and specify data types  
  
	b. Run `(Internship-python-2)% python3 cookies.py` to create table **cookies**  
  
	c. Update `cookies.py` to comment out all `CREATE TABLE` code  
  
	d. Pre-populate table **cookies** with data using DB Browser for SQLite  
	- Download [sqlitebrowser for macOS](https://github.com/sqlitebrowser/sqlitebrowser) from GitHub  
It is a SQLite-compatible, open source tool to manage databases with the spreadsheet-like UI,  similar to MySQLWorkbench  
  
	> Download and install: brew install --cask db-browser-for-sqlite  
	> Open: Finder --> Applications --> DB Browser for SQLite  
	> Open Database --> . . . /cookiejar.db --> Browse Data --> Insert a new record in the current table  
	> Enter data  
	> Write data to the database file
  
2. Create `class Cookeis:`  
  
- Include initializer (`def __init__`) to implement the logic for connecting the database to the project  
  
	- Include functions:   
	-- `insert_cookies` to create  
	-- `get_all` to read  
	-- `update_cookies` to update  
	-- `delete_cookies` to delete  
	-- `end` to close connection  
  
3. Update `main.py`  
`import cookies as c` to run the Cookies class functions  
  
___  
  
## Run the app  
  
1. Check the style of `main.py`:  
`(Internship-python-2)% pycodestyle main.py`  
  
2. Run the app:  
`(Internship-python-2)% python3 main.py`  
  
```
Output:  
SQLite table cookies already exists
Connected to SQLite
Simco Cookie Jar initialized []
Total rows are:   9
Printing each row
ID:  1
Name:  peanut butter blossom
Quantity:  3 dozen
Price:  9

ID:  2
Name:  oatmeal raisin
Quantity:  2 dozen
Price:  12

ID:  3
Name:  coffee cashew biscotti
Quantity:  4 dozen
Price:  16

ID:  4
Name:  ginger molasses
Quantity:  2 dozen
Price:  14

ID:  5
Name:  lemon crinkle
Quantity:  3 dozen
Price:  10

ID:  6
Name:  coconut macaroons
Quantity:  1 dozen
Price:  6

ID:  7
Name:  sugar cookies
Quantity:  3 dozen
Price:  7

ID:  8
Name:  linzer thumbprints
Quantity:  4 dozen
Price:  15

ID:  9
Name:  maple walnut shortbread bars
Quantity:  3 dozen
Price:  17

end cookie recipes - yummm
recipe has been added to table cookies
the price has been updated
recipe deleted from db cookiejar
```  
  
4. Check the data  
`(Internship-python-2)% python3 main.py`  
  
```
Output:  
SQLite table cookies already exists
Connected to SQLite
Simco Cookie Jar initialized []
Total rows are:   9
Printing each row
ID:  1
Name:  peanut butter blossom
Quantity:  3 dozen
Price:  9

ID:  2
Name:  oatmeal raisin
Quantity:  2 dozen
Price:  12

ID:  3
Name:  coffee cashew biscotti
Quantity:  4 dozen
Price:  16

ID:  4
Name:  ginger molasses
Quantity:  2 dozen
Price:  14

ID:  5
Name:  lemon crinkle
Quantity:  3 dozen
Price:  10

ID:  6
Name:  coconut macaroons
Quantity:  1 dozen
Price:  5

ID:  8
Name:  linzer thumbprints
Quantity:  4 dozen
Price:  15

ID:  9
Name:  maple walnut shortbread bars
Quantity:  3 dozen
Price:  17

ID:  10
Name:  chocolate chip
Quantity:  4 dozen
Price:  15

end cookie recipes - yummm
recipe has been added to table cookies
the price has been updated
recipe deleted from db cookiejar
```  

5. View table **cookies** using sqlite shell  
	`(Internship-python-2)% sqlite3 cookiejar.db`  
  
	`sqlite> .databases`  
	> Output:  
	> main: . . . /Internship-python-2/cookiejar.db r/w  
  
	`sqlite> .tables`  
	> Output:  
	> cookies  
  
	`sqlite> .mode column`  
	`sqlite> SELECT * from cookies;`  
  
```
id_cookies  name                          quantity  price
----------  ----------------------------  --------  -----
1           peanut butter blossom         3 dozen   9    
2           oatmeal raisin                2 dozen   12   
3           coffee cashew biscotti        4 dozen   16   
4           ginger molasses               2 dozen   14   
5           lemon crinkle                 3 dozen   10   
6           coconut macaroons             1 dozen   5    
8           linzer thumbprints            4 dozen   15   
9           maple walnut shortbread bars  3 dozen   17   
10          chocolate chip                4 dozen   15    
```
`sqlite> .quit`  
  
The data checks out:    
ID 10 chocolate chip, 4 dozen, 15 was added  
ID 6 price was changed from 6 to 5  
ID 7 sugar cookies has been deleted  
  
___  
  
## Push to GitHub:  
 
`(Internship-python-2)% git add .`  
  
`(Internship-python-2)% git commit -m "added Cookies class and db table"`   
  
`(Internship-python-2)% git push cookie Internship-py-2-2`  
```  
Output:  
 * [new branch]      Internship-py-2-2 -> Internship-py-2-2
```  
  
---  
  
  
