import os


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

INSTALLED_APPS = (
    ('/', 'core'),
    ('/media/', 'pynta.apps.simple.Static'),
)

STORAGE_MONGODB = {
    'database': 'whois',
}

TEMPLATES_MAKO = {
    'directories': os.path.join(PROJECT_ROOT, 'templates'),
    'input_encoding': 'utf-8',
}

SESSION_STORAGE = 'pynta.storage.Mongodb'
