# Work with Django (py-2-4)  
  
---  
  
## Configure dev env to include Django  
  
1. Make sure you are in the pipenv **(Internship-python-2) %** directory  
  
2. Create and switch to new branch ***Internship-py-2-4***  
  
3. Install packages with pipenv:  
  
	a. `pipenv install Django`  
		`pipenv install django-environ`  
  
	b. *Note: mistakenly installed flask
	`pipenv uninstall flask`*  
  
	c. Check Pipfile:  
	>[[source]]  
	>url = "https://pypi.org/simple"  
	>verify_ssl = true  
	>name = "pypi"  
	>  
	>[packages]  
	>pypyodbc = "\*"  
	>django = "\*"    
	>django-environ = "\*"
	> 
	>[dev-packages]  
	>pycodestyle = "\*"  
	>  
	>[requires]  
	>python_version = "3.11"  
	>python_full_version = "3.11.4"
  
4. Launch subshell in the pipenv:  
	`pipenv shell`  
  
5. Initialize Django project - **coolsite**:  
	`django-admin startproject coolsite .`  
  
:file_folder:`Internship-python-2`  
  `├──`:file_folder:`coolsite`  
  `│ ├──__init__.py`  
  `│ ├──asgi.py`  
  `│ ├──settings.py`  
  `│ ├──urls.py`  
  `│ └──wsgi.py`  
  `└──manage.py`  
  
6. Confirm Django local webserver  
  
	a. `python3 manage.py runserver`  
	```
	Django version 4.2.4, using settings 'coolsite.settings'
	Starting development server at http://127.0.0.1:8000/
	```  
  
	b. Visit `http://127.0.0.1:8000/` on a web browser to see the Django install confirmation page  
  
	c. Stop local server: `control+C`  
  
7. Use [django-environ](https://pypi.org/project/django-environ/) to manage environment variables:  
  
	a. Refactor  `settings.py` to a `settings` directory  
  
`├──`:file_folder:`settings.py`  
`│ ├── __init__.py`  
`│ ├── base.py`  
`│ ├── development.py`  
`│ └── prouction.py`  
`├──__init__.py`  
`├──asgi.py`  
`├──urls.py`  
`└──wsgi.py`  
  
b. Update `base.py` (replaces `settings.py`)  
  
c. Create `.env` in root directory (with `manage.py`)  
		`DEBUG=True`  
		`SECRET_KEY=<your-secret-key>`  
  
- Use [Djecrety](https://djecrety.ir/) to generate a Django secret key to replace `<your-secret-key>`  
  
- Environment variables will be read on startup from a `.env` file (instead of hardcoded in the `base.py` file)  
  
- Create `.env.example` in root directory (with `manage.py`)  
		`DEBUG=True`  
		`SECRET_KEY=<try-using-djecrety-to-generate-a-secret-key>`    
  
- Some values in `base.py` need to be kept secret so only `.env.example` is pushed to GitHub  
  
d. Make sure Django places all directories where static files can be found into the `STATIC_ROOT` so that static files will be served from the `STATIC_ROOT` in production 
	- `python3 manage.py collectstatic`  
  
8. Confirm Django local webserver  
  
	a. `python3 manage.py runserver`  
  
	b. Visit `http://127.0.0.1:8000/`  
  
	c. `control+C`  
  
9. Update `.gitignore`  
	```
	# setting up django project with pipenv  
	# https://python.plainenglish.io/setting-up-a-basic-django-project-with-pipenv-7c58fa2ec631  
	# config secrets with django-environ and created .env file  
	**/*.pyc  
	**/__pycache__  
	.DS_Store  
	*.sqlite3  
	# .env already in this file
	```  
  
___  
  
## Database query  
  
1. Update `coolsite`/`urls.py`  
	```
	from django.contrib import admin  
	from django.urls import path, include  
  
	urlpatterns = [  
	path('admin/', admin.site.urls),  
	path('cookiejar/', include('cookiejar.urls')),  
	]
	```
  
2. Create new Python Package in root directory: `cookiejar`  
  
- Update `cookiejar`/`apps.py`  
  
3. Create db tables  
  `python3 manage.py migrate`  
  
4. Define and activate the models  
  	
	a. Update `cookiejar`/`models.py`  
  
	- Be sure to add `__str__()` methods to the models
  
	b. Tell Django there are changes to the models  
	`python3 manage.py makemigrations cookiejar`  
  
	c. Return the SQL of the migration  
	`python3 manage.py sqlmigrate cookiejar 0001`  
  
	d. Create model tables in the db and synchronize changes  
	`python3 manage.py migrate`  
  
5. Use the database API to create Cookie and Ingredient data  
	`python3 manage.py shell`  
```
Python 3.11.4 . . .
(InteractiveConsole)
>>> from cookiejar.models import Cookie, Ingredient, CookieIngredient

#no cookie in the table yet
>>> Cookie.objects.all()
<QuerySet []>

#create cookies
>>> Cookie.objects.bulk_create([Cookie(cookie_name='first cookie',instructions='step1, step2, step3',price=5),Cookie(cookie_name='second cookie',instructions='step1, step2, step3',price=11),Cookie(cookie_name='third cookie',instructions='step1, step2, step3, step4',price=7),Cookie(cookie_name='fourth cookie',instructions='step1, step2, step3',price=3),Cookie(cookie_name='fifth cookie',instructions='step1, step2, step3, step4',price=9)])

[<Cookie: first cookie, step1, step2, step3, 5>, <Cookie: second cookie, step1, step2, step3, 11>, <Cookie: third cookie, step1, step2, step3, step4, 7>, <Cookie: fourth cookie, step1, step2, step3, 3>, <Cookie: fifth cookie, step1, step2, step3, step4, 9>]

#display all cookie in db
>>> cc = Cookie.objects.all()
>>> for c in cc:
...  print(c)
... 
fifth cookie, 9, step1, step2, step3, step4
fourth cookie, 3, step1, step2, step3
third cookie, 7, step1, step2, step3, step4
second cookie, 11, step1, step2, step3
first cookie, 5, step1, step2, step3

#create ingredients
>>> Ingredient.objects.bulk_create([Ingredient(ingredient_name='first ingredient',cost=2.49),Ingredient(ingredient_name='second ingredient',cost=4.99),Ingredient(ingredient_name='third ingredient',cost=3.28),Ingredient(ingredient_name='fourth ingredient',cost=1.67),Ingredient(ingredient_name='fifth ingredient',cost=3.97)])

[<Ingredient: first ingredient, 2.49>, <Ingredient: second ingredient, 4.99>, <Ingredient: third ingredient, 3.28>, <Ingredient: fourth ingredient, 1.67>, <Ingredient: fifth ingredient, 3.97>]

#display all ingredient in db
>>> ii = Ingredient.objects.all()
>>> for i in ii:
...  print(i)
... 
fifth ingredient, 3.97
first ingredient, 2.49
fourth ingredient, 1.67
second ingredient, 4.99
third ingredient, 3.28

>>> quit()
```  
  	
6. Use DB Browser for SQLite to create CookieIngredient data then view in the shell  
`python3 manage.py shell`  
```
>>> from cookiejar.models import Cookie, Ingredient, CookieIngredient
>>> xx = CookieIngredient.objects.all()
>>> for x in xx:
...  print(x)
... 
fifth cookie, 9, step1, step2, step3, step4_1 stick_fifth ingredient, 3.97
fifth cookie, 9, step1, step2, step3, step4_1 tsp_fourth ingredient, 1.67
fifth cookie, 9, step1, step2, step3, step4_1/4 tbsp_second ingredient, 4.99
fifth cookie, 9, step1, step2, step3, step4_2 cup_third ingredient, 3.28
fourth cookie, 3, step1, step2, step3_1/4 tsp_fourth ingredient, 1.67
fourth cookie, 3, step1, step2, step3_1 tbsp_second ingredient, 4.99
fourth cookie, 3, step1, step2, step3_1 cup_third ingredient, 3.28
third cookie, 7, step1, step2, step3, step4_1/2 stick_fifth ingredient, 3.97
third cookie, 7, step1, step2, step3, step4_2 tsp_fourth ingredient, 1.67
third cookie, 7, step1, step2, step3, step4_1/2 cup_third ingredient, 3.28
second cookie, 11, step1, step2, step3_2 stick_fifth ingredient, 3.97
second cookie, 11, step1, step2, step3_9 oz_first ingredient, 2.49
second cookie, 11, step1, step2, step3_3/4 tsp_fourth ingredient, 1.67
second cookie, 11, step1, step2, step3_1/2 tbsp_second ingredient, 4.99
second cookie, 11, step1, step2, step3_2 cup_third ingredient, 3.28
first cookie, 5, step1, step2, step3_14 oz_first ingredient, 2.49
first cookie, 5, step1, step2, step3_1/2 tbsp_second ingredient, 4.99
first cookie, 5, step1, step2, step3_1 1/3 cup_third ingredient, 3.28  
```  
  
7. Create class based views that print to console  
  
a. Update `cookiejar`/`views.py`  
  
- `class CookieListView(ListView):` - to list all cookies  
  
- `class CookiePriceListView(ListView):` - to list all cookies by price  
  
- `class class CookieDetailView(UpdateView)` - to view selected cookie info and ingredients info  
  
- `class CookieCreateView(CreateView)` - to add a new cookie to db  
  
- `class CookieUpdateView(UpdateView)` - to update a cookie in db  
  
- `class CookieDeleteView(DeleteView):` - to confirm deleting a selected cookie  
  
b. Create `templates` directory in root directory  
- Get [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/#separate) v5.3 CDN
- Create `layout.html`  
  
c. Create `cookiejar/templates/cookiejar` directory  
  
- Create `cookie_list.html`  
  
- Create `cookie_price_list.html`  
  
- Create `cookie_detail.html`  
  
- Create `cookie_add.html`  
  
- Create `cookie_update.html`  
  
- Create `cookie_confirm_delete.html`  
    
d. Update `cookiejar`/`urls.py`  
  
e. If the models were changed:  
  
- `python3 manage.py makemigrations`  
  
- `python3 manage.py migrate`  
  
___  
  
## Run the app  
  
1. Make sure the app works  
	`(Internship-python-2)% python3 manage.py runserver`  
  
2. Create requirements.txt to share project and others can easily reproduce the environment  
	`(Internship-python-2)% pipenv requirements > requirements.txt`  
  
3. Push to GitHub:  
 
	a. `(Internship-python-2)% git add .`  
  
	b. `(Internship-python-2)% git commit -m "connect Django to project"`   
  
	c. `(Internship-python-2)% git push cookie Internship-py-2-4`  
  
---  
