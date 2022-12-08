

from datetime import datetime
from config import db, ma

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
    

class MemberSchema(ma.SQLAchemyAutoSchema):
    class Meta:
        model = Member
        load_instance = True
        sqla_session = db.session
        
member_schema = MemberSchema()
members_schema = MemberSchema(many=True)
