## About
Simple Django read/write only e-shop REST API.\
Made as an assignment for a job interview.\
Original assignment is at `product_catalog_api/doc/zadani.txt`\
The assignment and some names in the code are in Czech language.

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
Make sure you have your virtual environment activated.\
`. ../venv/bin/activate`\
Then run:\
`python manage.py runserver`

Note: There is `test/test_data.json` file whose contents you can import at `http://127.0.0.1:8000/import` and try things out, for example at http://127.0.0.1:8000/detail/AttributeName

## How to Run Tests
In `product_catalog_api/apina` folder:\
Make sure you have your virtual environment activated.\
`. ../venv/bin/activate`\
Then run:\
`robot data_api/testing/api_tests.robot`

Note: Output files such as log and report will be in the folder you run the tests from.

## Known bugs and my notes
Listed in `doc/notes.txt`
