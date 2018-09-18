import flask_admin

from app.lib.airtable import AEAirtable as AEAirtableBase
from app.lib.admin import UserView, LeadView
from app.models.lead import Lead
from app.models.user import User


AEAirtable = AEAirtableBase()


def register_extensions(app):
    """Register extensions with config vars defined."""
    AEAirtable.init_app(app)

    # Admin
    AEAdmin = flask_admin.Admin(app, 'AE Admin')
    AEAdmin.add_view(UserView(User))
    AEAdmin.add_view(LeadView(Lead))
