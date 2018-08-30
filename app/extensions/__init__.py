from app.lib.airtable import AEAirtable as AEAirtableBase

AEAirtable = AEAirtableBase()


def register_extensions(app):
    """Register extensions with config vars defined."""
    AEAirtable.init_app(app)
