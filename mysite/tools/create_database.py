# Importieren Sie das Django-Modul
import os
from django.conf import settings

DATABASE_NAME = 'db.sqlite3'

# Setzen Sie die Einstellungen für das Django-Projekt
settings.configure(
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(os.getcwd(), '%s' % DATABASE_NAME),
        }
    }
)

# Überprüfen, ob die Datenbank bereits existiert
if not os.path.exists(DATABASE_NAME):
    # Wenn die Datenbank nicht existiert, erzeugen Sie sie
    import django
    django.setup()

    # Fügen Sie hier Ihre Django-Modelle hinzu, falls erforderlich

    # Erzeugen Sie die leere Datenbank
    from django.core.management import call_command
    call_command('migrate')

    print("Leere SQLite-Datenbank: '%s' wurde erfolgreich erstellt." % DATABASE_NAME)
else:
    print("Die SQLite-Datenbank '%s' existiert bereits!" % DATABASE_NAME)


