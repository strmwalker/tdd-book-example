#!/usr/bin/env python
import os
import sys

import dotenv

if __name__ == "__main__":
    dotenv.read_dotenv()

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "superlists.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldnt import Django. Are you sure its installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)

