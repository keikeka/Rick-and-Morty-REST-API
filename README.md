<p>
<h4 align="center">4Geeks Academy</h4>
<h2 align="center" style="margin: 0">Build a Rick and Morty REST API</h2>
<h3 align="center" style="margin-top: 0">Keili Rosales</h3>
</p>

## Objective

The objective of this exercise is to build an API to manage the Rick and Morty blog, where users will be able to list characters, locations and create or delete favorites. 

In order for users to be able to do all these actions, it is necessary to apply the following steps:

- Model the database: Create a database and the necessary tables to store that information.
- Build endpoints in this case using Flask.
- Constantly testing the endpoints with postman.

## Installation (automatic if you are using gitpod)

> Important: The boiplerplate is made for python 3.7 but you can easily change the `python_version` on the Pipfile.

The following steps are automatically runned withing gitpod, if you are doing a local installation you have to do them manually:

```sh
pipenv install;
mysql -u root -e "CREATE DATABASE example"; Replace with mysql -u root -e "USE example" if the database example is already created".
pipenv run init;
pipenv run migrate;
pipenv run upgrade;
```
## Manual Installation for Ubuntu & Mac

⚠️ Make sure you have `python 3.6+` and `MySQL` installed on your computer and MySQL is running, then run the following commands:
```sh
$ pipenv install (to install pip packages)
$ pipenv run migrate (to create the database)
$ pipenv run start (to start the flask webserver)
```

## Technologies
- Python
- Flask
- SQLAlchemy

## Contributions

I´d love to get your appreciation or report on the code at https://github.com/keikeka/Rick-and-Morty-REST-API

Thank you so much!