from flask_wtf import FlaskForm as Form
from mongoengine import DoesNotExist
from wtforms import PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email, Required
from werkzeug.security import check_password_hash

from app.models.user import User


class LoginForm(Form):
    email = EmailField('Email', [Required(), Email()])
    password = PasswordField('Password', [Required()])

    def validate(self):
        """
        Validation process attaches User object.
        """
        rv = Form.validate(self)
        if not rv:
            return False
        try:
            self.user = User.objects.get(email__iexact=self.email.data)
        except DoesNotExist:
            return False

        if check_password_hash(self.user.password_hash, self.password.data):
            return True
        return False
