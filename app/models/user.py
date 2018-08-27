from app.models import db


class User(db.Document):
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    email = db.StringField(required=True, unique=True)
    password_hash = db.StringField(required=True)

    company = db.StringField()
    employment_status = db.StringField()
    academic_degree = db.StringField()
    age = db.StringField()

    entrepreneurial_essay = db.StringField()
    problems_essay = db.StringField()

    def __str__(self):
        return f'{self.first} {self.last_name}'
