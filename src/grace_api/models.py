

from datetime import datetime
from config import db, ma

class Member(db.Model):
    __tablename__ = "member"
    id = db.Column(db.Integer, primary_key=True)
    churchId = db.Column(db.Integer, db.ForeignKey("church.id"))
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    firstName = db.Column(db.String)
    lastName = db.Column(db.String)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
class Church(db.Model):
    __tablename__ = "church"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    address = db.Column(db.String)
    address2 = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    zip = db.Column(db.String)
    phone = db.Column(db.String)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    members = db.relationship(
        Member,
        backref="church",
        cascade="all, delete, delete-orphan",
        single_parent=True,
        order_by="desc(Member.id)"
    )
    
class ChurchSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Church
        load_instance = True
        sqla_session = db.session
        
church_schema = ChurchSchema()
churches_schema = ChurchSchema(many=True)
    