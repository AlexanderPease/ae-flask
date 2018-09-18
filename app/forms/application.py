from flask_wtf import FlaskForm as Form
from wtforms import (
    PasswordField, TextField, SelectField, TextAreaField)
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email, Required

from app.lib.constants import COURSE_TYPES

COURSE_TYPES.insert(0, (None, '-----'))


class ApplicationEmailForm(Form):
    """Step 1: Basic Information."""
    first_name = TextField('First Name', [Required()])
    last_name = TextField('Last Name', [Required()])
    email = EmailField('Email', [Required(), Email()])
    password = PasswordField('Password', [Required()])
    course_type = SelectField(
        'Which course are you most interested in?',
        [Required()],
        choices=COURSE_TYPES
    )


class ApplicationFullForm(Form):
    """Step 2: Professional Info."""
    company = TextField('Company', [Required()])
    age = SelectField(
        'Age',
        [Required()],
        choices=[(i, i) for i in range(18, 100)],
        coerce=int)
    employment_status = SelectField(
        'Employment Status',
        [Required()],
        choices=[('unemployed', 'Unemployed'), ('employed', 'Employed')]
    )
    academic_degree = SelectField(
        'Highest Academic Degree',
        [Required()],
        choices=[
            ('high_school', 'High School'),
            ('bachelors', 'Bachelors'),
            ('masters', 'Masters'),
            ('phd', 'PhD')
        ]
    )
    entrepreneurial_essay = TextAreaField(
        'In your own words, what does it mean for a person to act entrepreneurial?',
        [Required()])
    problem_essay = TextAreaField(
        'What are problem areas in your life/work that you think could be interesting to solve? *',
        [Required()])
