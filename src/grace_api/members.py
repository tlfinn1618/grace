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

def create(member):
    email = member.get("email")
    password = member.get("password")
    firstName = member.get("firstName")
    lastName = member.get("lastName")
    
    if lastName and firstName not in MEMBERS:
        MEMBERS[lastName] = {
            "email": email,
            "password": password,
            "firstName": firstName,
            "lastName": lastName,
            "timestamp": get_timestamp(),
        }
        return MEMBERS[lastName], 201
    else:
        abort(
            406,
            f"A member with the name {firstName} {lastName} already exists"
        )
        
def read_one(lastName):
    if lastName in MEMBERS:
        return MEMBERS[lastName]
    else:
        abort(
            404, f"Person with last name {lastName} was not found"
        )
        
        
        