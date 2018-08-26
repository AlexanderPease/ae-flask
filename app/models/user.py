from flask_mongoengine import MongoEngine as db

class User(db.Document):
    name = db.StringField(required=True)
    email = db.StringField(required=True)

    company = db.StringField()
    employment_status = db.StringField()
    academic_degree = db.StringField()
    age = db.StringField()

    entrepreneurial_essay = db.StringField()
    problems_essay = db.StringField()
