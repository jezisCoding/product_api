## About
Simple Django read/write only e-shop REST API.\
Made as an assignment for a job interview.\
Some names are in Czech.

A database diagram and test data are also here.

## Started with this tutorial:
https://blog.logrocket.com/django-rest-framework-create-api/#setting-up-django-rest-framework

## How to Install
First make sure you have latest Python 3 and venv.
Installation depends on your system.\
Then, in `product_catalog_api` folder run:\
`python3 -m venv venv`\
`. venv/bin/activate`\
`pip install --upgrade pip`\
`pip install -r requirements.txt`\
`cd apina`\
`python manage.py migrate`

## How to Run
In `product_catalog_api/apina` folder:\
Make sure you have your virtual environment activated.
`. ../venv/bin/activate`\
Then run:\
`python manage.py runserver`

## Known bugs and my notes
Listed in `notes.txt`

## Test data
Is in project root, named `test-data.json`
