from app.models import db


class User(db.Document):
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    email = db.StringField(required=True, unique=True)
    password_hash = db.StringField(required=True)

    company = db.StringField()
    employment_status = db.StringField()
    academic_degree = db.StringField()
    age = db.IntField()

    entrepreneurial_essay = db.StringField()
    problems_essay = db.StringField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    ###########################################################################
    # flask_login required methods
    ###########################################################################
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
