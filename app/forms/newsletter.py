from flask_wtf import FlaskForm as Form

from wtforms.fields.html5 import EmailField
from wtforms.validators import Email,  Required


class NewsletterForm(Form):
    email = EmailField('Email', [Required(), Email()])
