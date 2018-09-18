from flask import redirect, url_for, request
from flask_admin.contrib.mongoengine import ModelView
from flask_login import current_user


class AEModelView(ModelView):
    can_create = False
    can_edit = False
    can_delete = False

    column_exclude_list = []

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('login', next=request.url))


class UserView(AEModelView):
    column_exclude_list = ['password_hash', 'airtable_id', 'airtable_map']


class LeadView(AEModelView):
    column_exclude_list = ['airtable_id', 'airtable_map']
