

from datetime import datetime
from flask import abort, make_response

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

CHURCHES = {
    "GID": {
        "id": "1",
        "name": "Grace in the Desert Adventist Church",
        "phone": "123-456-7890",
        "address": "1234 N Some St",
        "city": "Peoria",
        "state": "Arizona",
        "zip": "12345",
    },
    "GID2": {
        "id": "2",
        "name": "Grace in the Desert Adventist Church2",
        "phone": "234-567-8901",
        "address": "1334 N Some St",
        "city": "Sun City",
        "state": "Arizona",
        "zip": "23456",
    },
    "GID3": {
        "id": "3",
        "name": "Grace in the Desert Adventist Church3",
        "phone": "987-654-3210",
        "address": "12234 N Some St",
        "city": "Glendale",
        "state": "Arizona",
        "zip": "98756",
    }
}

def read_all():
    return list(USERS.values())

def create(user):
    email = user.get("email")
    password = user.get("password")
    fname = user.get("fname")
    lname = user.get("lname")
    
    if email and email not in USERS:
        USERS[email] = {
            "fname": fname,
            "lname": lname,
            "email": email,
            "password": password,
            "timestamp": get_timestamp(),
        }
        return USERS[email], 201
    else:
        abort(
            406,
            f"The email address of {email} already exists"
        )
        
def read_one(fname, lname):
    if fname and lname in USERS:
        return USERS[fname, lname]
    else:
        abort(
            404, f"The user with the name of {fname} {lname} is not found"
        )
        
def update(lname, fname, user):
    if lname and fname in USERS:
        USERS[lname]["fname"] = user.get("fname", USERS[lname]["fname"])
        USERS[lname]["timestamp"] = get_timestamp()
        return USERS[lname]
    else:
        abort(
            404,
            f"User with last name {lname} is not found"
        )
        
def delete(fname, lname):
    if fname and lname in USERS:
        del USERS[fname, lname]
        return make_response(
            f"{fname} {lname} has been successfully deleted", 200
        )
    else:
        abort(
            404, 
            f"The user with the name of {fname} {lname} is not found"
        )
        