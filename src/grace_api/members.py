from datetime import datetime
from flask import abort

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


MEMBERS = {
    "Fairy": {
        "firstName": "Tooth",
        "lastName": "Fairy",
        "email": "sayAh@somemail.com",
        "password": "password123",
        "timestamp": get_timestamp(),
    },
    "Ruprecht": {
        "firstName": "Knecht",
        "lastName": "Ruprecht",
        "email": "kramps@somemail.com",
        "password": "password123",
        "timestamp": get_timestamp(),
    },
    "Bunny": {
        "firstName": "Peter",
        "lastName": "Bunny",
        "email": "hops@somemail.com",
        "password": "password123",
        "timestamp": get_timestamp(),
    }
}
    
def read_all():
    return list(MEMBERS.values())