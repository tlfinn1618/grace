

from datetime import datetime
from config import db, ma

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
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
class ChurchSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Church
        load_instance = True
        sqla_session = db.session
        
church_schema = ChurchSchema()
churches_schema = ChurchSchema(many=True)
    