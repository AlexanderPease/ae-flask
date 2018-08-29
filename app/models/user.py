from mongoengine import signals

from app.lib.constants import COURSE_TYPES
from app.models import db


class User(db.Document):
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    email = db.StringField(required=True, unique=True)
    password_hash = db.StringField(required=True)

    course_type = db.StringField(
        required=True,
        choices=COURSE_TYPES)

    company = db.StringField()
    employment_status = db.StringField()
    academic_degree = db.StringField()
    age = db.IntField()

    entrepreneurial_essay = db.StringField()
    problem_essay = db.StringField()

    airtable_id = db.StringField()
    airtable_map = dict(
        first_name='First Name',
        last_name='Last Name',
        course_type='Course Type',
        company='Company',
        employment_status='Employment Status',
        academic_degree='Academic Degree',
        age='Age',
        entrepreneurial_essay='Entrepreneurial Essay',
        problem_essay='Problems Essay'
    )

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


#         airtable.get_all(view='MyView', maxRecords=20)

# airtable.insert({'Name': 'Brian'})

# airtable.search('Name', 'Tom')

# airtable.update_by_field('Name', 'Tom', {'Phone': '1234-4445'})

# airtable.delete_by_field('Name', 'Tom')


# def register_signals():
#     signals.post_save.connect(_update_airtable, sender=User)
