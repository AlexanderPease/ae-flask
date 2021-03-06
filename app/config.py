"""Defines the environment variables to load from prod/dev servers."""
from datetime import datetime

VARS = {
    'COMPANY_NAME': 'Prehype',
    'CURRENT_YEAR': datetime.today().year,
    # 'DEBUG': True,
    # 'FLASK_LOG_LEVEL': 'DEBUG',
    'PRODUCT_NAME': 'Applied Entrepreneurship',
    'TEMPLATES_AUTO_RELOAD': True,
    'AIRTABLE_AE': 'appCVnjZ57nX6jkJb'
}

ENV_VARS = [
    'FLASK_ENV',
    'FLASK_LOG_LEVEL',
    'SECRET_KEY',
    'MONGODB_HOST'
]
