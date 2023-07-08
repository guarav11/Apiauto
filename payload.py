from utilities.configurations import *


def create_user():
    body = {
            'name': 'morpheus',
            'email': 'leader'
        }
    return body


def update_user():
    body = {
            'name': 'morpheus',
            'job': 'zion resident'
        }
    return body


def register_user():
    body = {
            'email': 'eve.holt@reqres.in',
            'password': 'pistol'
        }
    return body


def register_unsuccessful():
    body = {
            'email': 'sydney@fife',
        }
    return body


def login_successful():
    body = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
    return body


def login_unsuccessful():
    body = {
            "email": "peter@klaven",
        }
    return body











# if u want to pass payload from this file
def addBookPayload():
    body = {
        "name": "Learn Appium Automation with Java",
        "isbn": "bcd",
        "aisle": "227",
        "author": "John foe"
    }
    return body


# if u want to pass payload from db
def buildPayLoadFromDB(query):
    addBody = {}  # dict
    tp = getQuery(query)  # tp is a tuple
    addBody['name'] = tp[0]
    addBody['isbn'] = tp[1]
    addBody['aisle'] = tp[2]
    addBody['author'] = tp[3]
    return addBody
