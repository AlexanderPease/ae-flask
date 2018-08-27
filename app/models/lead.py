from app.models import db


class Lead(db.Document):
    email = db.StringField(required=True)

    def __str__(self):
        return f'{self.first} {self.last_name}'