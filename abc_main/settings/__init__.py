
from .base import *

if config('CURRENT_ENV') == 'LOCAL':
    from .local import *
else:
    from .prod import *
