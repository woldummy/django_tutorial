# Create Django App manually

### Preparation
- Create directory
- visit dir
- to create virtual environment without packages

    ```python3 -m venv ./venv```

- To activate virtual environment:
     ```source ./bin/activate```

- check packages
    ```python3 -m pip list```

- To upgrade pip to current version :
    ```python3 -m pip install --upgrade pip```

### PIP Tipps
* Install pip
* pip and pip2, pip3
* Check installed packages:
    ```python3 -m pip show```
* List installed packages:
    ```python3 -m pip list```
    ```python3 -m pip freeze```
* Install a package from local or GitHub:
    ```python3 -m pip install <package>```
* Update a package:
    ```python3 -m pip install --upgrade  <package>```
* Update pip itself
    ```python3 -m pip3 install --upgrade pip```
* Uninstall a package:
    ```python3 -m pip --uninstall <package>```
* Check for dependencies:
    ```python3 -m pip check```

### Install Django
    ```python3 -m pip install Django```
* Check Django version
    ```python3 -m django --version```

* Install the startproject with name ___mysite___
    ```django-admin startproject mysite```

This creates folder ___mysite___ in folder mysite
* Check folder creation
* Start the server from within upper folder mysite: otherwise NOT FOUND ERROR

    ```python3 manage.py runserver 8080```

* Create polls project from within upper folder mysite

    ```python3 manage.py startapp polls```

* Check folder creation
* If everything works fine, deactivate virtual environment
	```deactivate```

— DONE —
# Create Django App using Pycharm with Django support

### How to manage project in PyCharm
* open folder mysite as project
* Virtualenv is recognized :)
* Enable Django Support under _Settings - languages and frameworks - Django_
* Enable Django Support **with upper folder mysite**
    * Show wizard the manage.py

### adjust Django settings to Germany
* change settings for German websites in ___settings.py___

    ```LANGUAGE_CODE = 'de-de'```
    ```TIME_ZONE = 'Europe/Berlin'```
