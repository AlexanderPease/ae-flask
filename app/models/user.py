from flask_login import UserMixin
from mongoengine import signals

from app.lib.constants import (
    COURSE_TYPES, PERMISSION_TYPES, COURSE_DATES, NULL_CHOICE)
from app.models import db


class User(db.Document, UserMixin):
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    email = db.StringField(required=True, unique=True)
    password_hash = db.StringField(required=True)

    course_type = db.StringField(choices=COURSE_TYPES + NULL_CHOICE)
    course_date = db.StringField(choices=COURSE_DATES + NULL_CHOICE)
    country_origin = db.StringField()

    company = db.StringField()
    employment_status = db.StringField()
    academic_degree = db.StringField()
    age = db.IntField()

    entrepreneurial_essay = db.StringField()
    problem_essay = db.StringField()

    permissions = db.ListField(
        db.StringField(choices=PERMISSION_TYPES)
    )

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

    @property
    def is_admin(self):
        return 'admin' in self.permissions
