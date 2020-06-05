# Instagram Clone
#### Author **[martin Gathu.](https://github.com/martingathu)**

## Description
This is a simple web based application for instagram features like posting,liking and commenting on images.



## Live link

https://myintagramclone.herokuapp.com/

### Prerequsites
    - Python 3.6
    - Django

### Clone the Repo
Run the following command on the terminal:

`git clone https://github.com/martingathu/intagram`

Install  [Postgres](https://www.postgresql.org/download/)
 
### Create a Virtual Environment
Run the following commands in the same terminal:
`pip install virtualenv`
`python3.6 -m venv virtual`
`source virtual/bin/activate`

### Install dependencies
Install dependencies that will create an environment for the app to run
`pip3 install -r requirements`

### Create a database

```
psql

CREATE DATABASE <database_name>;

```

### .env file

```
SECRET_KEY = '<Secret_key>'
DBNAME = '<database_name>'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '<your-email>'
EMAIL_HOST_PASSWORD = '<your-password>'

```

## Run initial Migration
```
python3.6 manage.py makemigrations instagram
python3.6 manage.py migrate

```


### Running the app in development
In the same terminal type:
`python3 manage.py runserver`

Open the browser on `http://localhost:8000/`

## Known bugs

Follow functionality issues. Fix coming soon.


## Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 3
    - Django
    - Postgresql

## Support and contact details
Contact me on martin5gathu@gmail.com  for any comments, reviews or collaboration.

### License
MIT - Licence