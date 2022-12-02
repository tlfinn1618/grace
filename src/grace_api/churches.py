

from flask import abort, make_response
from config import db
from models import Church, church_schema, churches_schema

def read_all():
    churches = Church.query.all()
    return churches_schema.dump(churches)

def create(church):
    name = church.get("name")
    existing_church = Church.query.filter(Church.name == name).one_or_none()
    
    if existing_church is None:
        new_church = church_schema.load(church, session=db.session)
        db.session.add(new_church)
        db.session.commit()
        return church_schema.dump(new_church), 201
    else:
        abort(
            406,
            f"{name} already exists in the list"
        )
        
def read_one(name):
    name = Church.query.filter(Church.name == name).one_or_none()
    
    if name is not None:
        return church_schema.dump(name)
    else:
        abort(
            404, f"{name} is not found"
        )
        
def update(name, church):
    existing_church = Church.query.filter(Church.name == name).one_or_none()
    
    if existing_church:
        update_church = church_schema.load(church, session=db.session)
        existing_church.name = update_church.name
        db.session.merge(existing_church)
        db.session.commit()
        return church_schema.dump(existing_church), 201
    else:
        abort(
            404,
            f"User with last name {name} is not found"
        )
        
def delete(name):
    existing_church = Church.query.filter(Church.name == name).one_or_none()
    
    if existing_church:
        db.session.delete(existing_church)
        db.session.commit()
        return make_response(f"{name} successfully deleted", 200)
    else:
        abort(
            404, 
            f"The church with the name of {name} is not found"
        )
        