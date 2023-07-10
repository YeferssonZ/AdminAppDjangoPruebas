#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import subprocess
# Ruta al archivo mqtt.py dentro de tu proyecto
ruta_mqtt = os.path.join(os.path.dirname(__file__), 'api/mqtt.py')

# Ejecuta el archivo mqtt.py usando subprocess
subprocess.Popen(['python', ruta_mqtt])


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AdminApp.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
