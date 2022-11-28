

from datetime import datetime
from flask import abort, make_response

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

CHURCHES = {
    "GID": {
        "name": "Grace",
        "phone": "123-456-7890",
        "address": "1234 N Some St",
        "city": "Peoria",
        "state": "Arizona",
        "zip": "12345",
    },
    "GID2": {
        "name": "Grace in the Desert Adventist Church2",
        "phone": "234-567-8901",
        "address": "1334 N Some St",
        "city": "Sun City",
        "state": "Arizona",
        "zip": "23456",
    },
    "GID3": {
        "name": "Grace in the Desert Adventist Church3",
        "phone": "987-654-3210",
        "address": "12234 N Some St",
        "city": "Glendale",
        "state": "Arizona",
        "zip": "98756",
    }
}

def read_all():
    return list(CHURCHES.values())

def create(church):
    name = church.get("name")
    phone = church.get("phone")
    address = church.get("address")
    city = church.get("city")
    state = church.get("state")
    zip = church.get("zip")
    
    if name not in CHURCHES:
        CHURCHES[name] = {
            "name": name,
            "phone": phone,
            "address": address,
            "city": city,
            "statestate":state,
            "zip": zip,
            "timestamp": get_timestamp(),
        }
        return CHURCHES[name], 201
    else:
        abort(
            406,
            f"{name} already exists in the list"
        )
        
def read_one(name):
    if name in CHURCHES:
        return CHURCHES[name]
    else:
        abort(
            404, f"The church by the name of {name} is not found"
        )
        
def update(name, church):
    if name in CHURCHES:
        CHURCHES[name] = church.get("name", CHURCHES[name])
        CHURCHES[name]["timestamp"] = get_timestamp()
        return CHURCHES[name]
    else:
        abort(
            404,
            f"User with last name {name} is not found"
        )
        
def delete(name):
    if name in CHURCHES:
        del CHURCHES[name]
        return make_response(
            f"{name} has been successfully deleted", 200
        )
    else:
        abort(
            404, 
            f"The church with the name of {name} is not found"
        )
        