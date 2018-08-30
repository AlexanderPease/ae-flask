from app.models import db


class Lead(db.Document):
    email = db.StringField(required=True, unique=True)

    airtable_id = db.StringField()
    airtable_map = dict(
        email='Email'
    )

    def __str__(self):
        return f'{self.email}'
