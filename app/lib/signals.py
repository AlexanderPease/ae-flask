import logging
from mongoengine import signals

from app.extensions import AEAirtable
from app.models.lead import Lead
from app.models.user import User


def register_signals():
    signals.pre_save.connect(
        _update_airtable, sender=User)
    signals.pre_save.connect(
        _update_airtable, sender=Lead)


def _update_airtable(sender, document, created=False, **kwargs):
    """Update user airtable."""
    json = dict()
    print(document)

    for k, v in document.airtable_map.items():
        json[v] = getattr(document, k)

    print(json)
    # Ex. AEAirtable.user for User model
    table = getattr(
        AEAirtable,
        str(document.__class__.__name__).lower()
    )
    print(table)

    if document.airtable_id:
        try:
            table.update(document.airtable_id, json)
        except Exception:
            logging.error(
                f'Failed to update document {json} to Airtable')
    else:
        try:
            rv = table.insert(json)
            document.airtable_id = rv.get('id')
        except Exception:
            logging.error(
                f'Failed to insert document {json} to Airtable')
