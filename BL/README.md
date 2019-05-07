# Business layer

## Description
The logic tier contains the "business rules" that take requests from the interface, extract data from the data tier and perform any needed processing of the data.

This layer was written by **Miruna Serian** as part of the Biocomputing II project

## Prerequisites
* aceess to the databse (instructions in the Database Layer /myproject/DB/)
* pytest 

## Installation
Apart from the installation required to get access to the database(provided in the DB layer) there are no installations required apart from pytest to carry out the tests.

Pytest can be installed:
`pip install -U pytest`

## Tests
To run the test:
`pytest tests.py`


### If access to hope server is not possible
and thus not being able to use the DB api I reccommend using the **bl_api_for_testing.py**, which uses the dummy version of the database layer functions to test the code. 
