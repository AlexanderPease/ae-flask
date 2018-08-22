"""Defines the environment variables to load from prod/dev servers."""
from datetime import datetime

VARS = {
    'COMPANY_NAME': 'Prehype',
    'CURRENT_YEAR': datetime.today().year,
    'DEBUG': True,
    'FLASK_LOG_LEVEL': 'DEBUG',
    'PRODUCT_NAME': 'Applied Entrepreneurship',
    'TEMPLATES_AUTO_RELOAD': True
    # 'SECRET_KEY': 'secret key',
}

ENV_VARS = [
    'DEBUG',
    'FLASK_LOG_LEVEL',
]
