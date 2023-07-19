# Setup the Development Environment (py-2-1)  
  
---  
  
## Set up development environment  
  
#### Installations and upgrades on computer  
  
**1.** macOS Ventura 13.4.1  
  
**2.** Ensure [latest version of Python](https://www.python.org/downloads/) (for Mac) is installed:  
`% python3 --version`  
> Output: Python 3.11.3  
  
-- Download Python 3.11.4 and follow prompts of Installer:  
`% python3 --version`  
> Output: Python 3.11.4  
  
**3.** Upgrade pip:  
`% pip3 install --upgrade pip`  
`% pip3 -V`  
> Output: pip 23.2  
  
**4.** Install [latest version of pipenv](https://pypi.org/project/pipenv/) - a Python virtualenv management tool:  
`% pip3 install pipenv`  
`% python3 -m pipenv --version`  
> Output: pipenv, version 2023.7.11  
  
**5.** Ensure [current version](https://git-scm.com/download/win) of [Git is installed](https://git-scm.com/download/mac) and configured on Mac (using [Homebrew](https://brew.sh/)):  
`% git --version`  
> Output: git version 2.41.0  
  
**6.** Ensure [SQLite3](https://ports.macports.org/port/sqlite3/) is installed. It is pre-installed on Mac:  
`% sqlite3 --version`  
> Output: 3.39.5 2022-10-14  
  
___  
  
## Create new project: Internship-python-2  
  
1. Log in to your GitHub account [or create a GitHub account](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home)    
  
2. Create GitHub repo  
	a. New repository  
	b. Repository name: ***Internship-python-2***  
	c. Choose repository visibility: Public  
	d. Do not initialize the new repository with README, gitignore, or license files  
	e. Create repository  
	f. Copy the remote repository URL  
  
3. Ensure [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/?section=mac) (for Mac) is installed  
    
4. Open PyCharm to [Create a Python project](https://www.jetbrains.com/help/pycharm/pipenv.html):  
***Internship-python-2***  
	a. Configure Python interpreter:  
	-- new environment **pipenv**  
	-- make sure Base interpreter is **Python 3.11**  
  
	b. Launch pipenv subshell in the venv (Internship-python-2):  
	`(Internship-python-2)% pipenv shell`  
  
	c. Install packages (and dependencies):  
	`(Internship-python-2)% pipenv install flask`  
	`(Internship-python-2)% pipenv install pypyodbc`  
	`(Internship-python-2)% pipenv install --dev pycodestyle`  
	
*Pypyodbc connects the database to the Python app  
	A ctypes (foreign function Python library) Open Database Connectivity (ODBC) module,  
	which means it is an API for accessing database management systems independent of database systems and operating systems*  
  
*Pycodestyle is a Python style guide checker*  
  
5. Clone the Internship-python-2 repository  
	a. Copy the HTTPS URL from GitHub  
	b. Paste the link in the git command:
	> (Internship-python-2)% git clone https://github.com/DebJamA/Internship-python-2.git  
	
	c. Create a new branch:  
`(Internship-python-2)% git init`  
`(Internship-python-2)% git checkout -b Internship-py-2-1`  
  
	> Output: Switched to a new branch 'Internship-py-2-1'  
  
6. Create `.gitignore` file in root directory  
	> Copy/paste from [mooowooo repo](https://gist.github.com/MOOOWOOO/3cf91616c9f3bbc3d1339adfc707b08a)  
  
7. Create `README.md`  
	> Setup the Development Environment (py-2-1)    
___  
  
## Create cookie.db and connect to project  
  
1. Create `main.py` in root directory  
  
2. Check the style of main.py:  
`% pycodestyle main.py`  
  
3. Run the app  
`(Internship-python-2)% python3 main.py`  
  
> Output:  
> Database created and Successfully Connected to SQLite  
> SQLite Database Version is:  [('3.42.0',)]  
> The SQLite connection is closed  
  
___  
  
## Push to GitHub:  
  
`% git add .`  
`% git commit -m ‘added project init’`  
`% git push --set-upstream origin Internship-py-2-1`  
  
> Output:  

  
---  
  
  