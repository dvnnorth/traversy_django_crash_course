# Traversy Media Django Crash Course
This repo just serves to store the work I'm doing following along with Traversy Media's Django crash course. Follow along [here](https://www.youtube.com/watch?v=D6esTdOLXh4).

## Running This App
This particular application was built using Python 3.
To run this app, first clone the repo. Create a virtual environment for the project and run `pip install -r requirements.txt` to install dependencies.

### Secret Key
The application expects a file named `secrets.json` in the project directory (same level as `settings.py`). The file should have this format:
```
{
  "SECRET_KEY": "your_secret_key_here",
  "DATABASE_NAME": "your_database_name_here",
  "DATABASE_USER": "your_database_username_here",
  "DATABASE_PASSWORD": "your_database_password_here"
}
```
Replace `your_secret_key_here` and all other pertinent strings with the pertinent information, of course. Need to generate a secret key? Run this simple Python script (it's how Django generates the key to begin with). 
```
import random
''.join(random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50))
```
(that information taken from [this website](https://foxrow.com/generating-django-secret-keys))

## A note about migrations, MariaDB, and Fedora
Just a quick note, I had to install `mariadb-devel`, `redhat-rpm-config`, `python2-devel` and `python3-devel` to be able to `pip install mysqlclient`. Just a note, if for nobody else than for myself in the future.

Follow those instructions and you should be all set.