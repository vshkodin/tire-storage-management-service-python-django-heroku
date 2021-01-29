### Tire Managment Service using Python, Django, Heroku
#### Little web app for Tire Storage Management based on Python, Django. Ready for deploying on Heroku.
##### Please give a "star" if it helped you.
* Django app, which can easily be deployed to Heroku.
* Update with your logo hello/static/logo.png
* Add your username and password to config.py
* This application supports the
[Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python)
article - check it out.

## Running Locally

Make sure you have Python 3.7 [installed locally](http://install.python-guide.org). To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), as well as [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone https://github.com/vsshk/tire-storage-management-service-python-django-heroku.git
$ cd tire-storage-management-service-python-django-heroku

$ python3 -m venv env
$ pip install -r requirements.txt

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
or
$ heroku local web -f Procfile.windows 
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku main

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
