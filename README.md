# Install Django Debug Toolbar (py-2-5)  
  
---  
  
## Make sure the system is set up properly  
  
1. Make sure you are in the pipenv **(Internship-python-2) %** directory  
  
2. Create and switch to new branch ***Internship-py-2-5***  
  
3. Forgot to register models `Ingredeint`, `Cookie`, `CookieIngredient` to Django admin  
  
- Update `cookiejar/admin.py`  
- `% python3 manage.py createsuperuser`  
- `% python3 manage.py runserver`  
- `http://127.0.0.1:8000/admin` to view the models  
  
4. If not already created in root directory, create `assets/css` and `assets/js`  
  
---  
  
## Install and Set Up the Django Debug Toolbar  
  
1. `% python3  -m  pip  install  django-debug-toolbar`  
  
- To include in pipenv and update `requirements.txt`:  
	- `% pipenv install --dev django-debug-toolbar`  
	- `% pipenv requirements > requirements.txt`  
  
2. Update `coolsite/settings/base.py`  
  
- Ensure `INSTALLED_APPS` includes this:  
	```
	'django.contrib.staticfiles',  
	'debug_toolbar',
	```  
  
- Ensure `MIDDLEWARE` includes this after SecurityMiddleware:  
	```
	'debug_toolbar.middleware.DebugToolbarMiddleware',
	```  
  
- Add `INTERNAL_IPS = ['127.0.0.1']` after `ROOT_URLCONF`  
  
- Ensure `TEMPLATES` includes this:  
	```
	'BACKEND': 'django.template.backends.django.DjangoTemplates',
	'APP_DIRS': True,
	```  
  
- Ensure `STATIC_URL = 'static/'`  
  
3. Update `coolsite/urls.py`  
	```
	if settings.DEBUG:  
	    import debug_toolbar  
	    urlpatterns = [  
	        path('__debug__/', include(debug_toolbar.urls)),  
	    ] + urlpatterns
	```  
  
4. Collect static files:  
  
- `python3 manage.py collectstatic`  
- `% python3 manage.py runserver`  
- `http://127.0.0.1:8000/` to view the toolbar column on the right  
  
---  
  
## Improve User Experience  
  
- Note: In order to change `User` registration from `username` to `email`, I had to wipe database, delete migration files, and delete `__pycache__` files to create  an `AbstractBaseUser` since a `CustomUser` model was NOT set up at the start of this project  
  
- Create Sign up with extra fields, Log in, and log out  
  
- Add `user` `ForeignKeY` to model `Cookie`  
  
- Password reset (no SMTP so copy/paste link from the *"email"*  in the `sent_emails` folder)  
  
- Install [whitenoise](https://whitenoise.readthedocs.io/en/latest/django.html) for static files to be served in production  
  
- Be sure to `collectstatic`, `makemigrations` and `migrate`  
  
---  
  

## Run the app  
  
1. Make sure the app works  
	`% python3 manage.py runserver`  
  
2. Push to GitHub:  
 
	a. `% git add .`  
  
	b. `% git commit -m "enable Django debug toolbar"`   
  
	c. `% git push cookie Internship-py-2-5`  
  
---  
  