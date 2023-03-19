

from datetime import datetime
from config import db, ma

class Address(db.Model):
    __tablename__ = "addresses"
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey("member.id"))
    address1 = db.Column(db.String)
    address2 = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    postCode = db.Column(db.String)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

class Member(db.Model):
    __tablename__ = "member"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    lastName = db.Column(db.String)
    firstName = db.Column(db.String)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    addresses = db.relationship(
        Address,
        backref="member",
        cascade="all, delete, delete-orphan",
        single_parent=True,
        order_by="desc(Address.timestamp)"
    )
    

class MemberSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Member
        load_instance = True
        sqla_session = db.session
        
member_schema = MemberSchema()
members_schema = MemberSchema(many=True)
