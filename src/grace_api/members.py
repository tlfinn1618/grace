from flask import abort, make_response

from config import db
from models import Member, member_schema, members_schema
  
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
            404, f"Member with last name {lastName} was not found"
        )
        
def update(lastName, member):
    if lastName in MEMBERS:
        MEMBERS[lastName]["firstName"] = member.get("fname", MEMBERS[lastName]["firstName"])
        MEMBERS[lastName]["timestamp"] = get_timestamp()
        return MEMBERS[lastName]
    else:
        abort(
            404,
            f"Member with last name of {lastName} was not found"
        )  
        
def delete(lastName):
    if lastName in MEMBERS:
        del MEMBERS[lastName]
        return make_response(
            f"{lastName} was successfully deleted", 200
        )
    else:
        abort(
            404,
            f"Person with last name {lastName} was not found"
        )