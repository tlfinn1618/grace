from flask import abort, make_response

from config import db
from models import Member, member_schema, members_schema
  
def read_all():
    members = Member.query.all()
    return members_schema.dump(members)

def create(member):
    lastName = member.get("lastName")
    firstName = member.get("firstName")
    existing_member = Member.query.filter(Member.lastName == lastName).one_or_none()
    
    if existing_member is None:
        new_member = member_schema.load(member, session=db.session)
        db.session.add(new_member)
        db.session.commit()
        return member_schema.dump(new_member), 201
    else:
        abort(
            406,
            f"A member with the name {firstName} {lastName} already exists"
        )
        
def read_one(lastName):
    member = Member.query.filter(Member.lastName == lastName).one_or_none()
    
    if member is not None:
        return member_schema.dump(member)
    else:
        abort(
            404, f"Member with last name {lastName} was not found"
        )
        
def update(lastName, member):
    existing_member = Member.query.filter(Member.lastName == lastName).one_or_none()
    
    if existing_member:
        update_member = member_schema.load(member, session=db.session)
        existing_member.firstName = update_member.firstName
        db.session.merge(existing_member)
        db.session.commit()
        return member_schema.dump(existing_member), 201
    else:
        abort(
            404,
            f"Member with last name of {lastName} was not found"
        )  
        
def delete(lastName):
    existing_member = Member.query.filter(Member.lastName == lastName).one_or_none()
    
    if existing_member:
        db.session.delete(existing_member)
        db.session.commit()
        return make_response(f"{lastName} was successfully deleted", 200)
    else:
        abort(
            404,
            f"Member with last name {lastName} was not found"
        )