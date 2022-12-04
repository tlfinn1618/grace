

from datetime import datetime
from config import app, db
from models import Church, Member

CHURCH_MEMBER = [
    {
        "id": "1",
        "churchId": "1",
        "email": "tlfinn1618@gmail.com",
        "password": "Psa23v.1",
        "firstName": "Thomas",
        "lastName": "Finn",
        "timestamp": "2022-12-03 20:37:35",
    },
]

with app.app_context():
    db.drop_all()
    db.create_all()
    for data in CHURCH_MEMBER:
        new_church_member = Church(churchId=data.get("id"))
        for content, timestamp in data.get("members", []):
            new_member.member.append(
                Member(
                    content=content,
                    timestamp=datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"),
                )
            )
        db.session.add(new_person)
    db.session.commit()