

from datetime import datetime
from config import app, db
from models import Member, Address

MEMBER_ADDRESSES = [
    {
        "lastName": "Finn",
        "firstName": "Thomas",
        "address1": "123 Some St",
        "address2": "",
        "city": "Surprise",
        "state": "AZ",
        "postCode": "85374",
    }
]

with app.app_context():
    db.drop_all()
    db.create_all()
    for data in MEMBER_ADDRESSES:
        new_member = Member(lastName=data.get("lastName"), firstName=data.get("firstName"))
        for content in data.get("addresses", []):
            new_member.addresses.append(
                Address(
                    address1=address1,
                    address2=address2,
                    city=city,
                    state=state,
                    postCode=postCode,
                )
            )
        db.session.add(new_member)
    db.session.commit()