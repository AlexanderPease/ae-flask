from flask_admin.contrib.mongoengine import ModelView


class ReadOnlyView(ModelView):
    can_create = False
    can_edit = False
    can_delete = False

    column_exclude_list = []


class UserView(ReadOnlyView):
    column_exclude_list = ['password_hash', 'airtable_id', 'airtable_map']


class LeadView(ReadOnlyView):
    column_exclude_list = ['airtable_id', 'airtable_map']
