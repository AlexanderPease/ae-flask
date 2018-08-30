from airtable import Airtable


class AEAirtable(object):
    def init_app(self, app):
        self.user = Airtable(app.config['AIRTABLE_AE'], 'Applications')
        self.lead = Airtable(app.config['AIRTABLE_AE'], 'Leads')
