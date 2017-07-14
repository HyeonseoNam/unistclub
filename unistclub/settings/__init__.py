import os
from .base import *

ENV_TYPE = os.getenv('UNICLUB_ENV', 'development')

if ENV_TYPE == 'production':
    from .production import *
else:
    from .local import *