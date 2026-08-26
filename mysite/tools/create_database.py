"""Erstellt eine leere SQLite-Datenbank für das Django-Projekt.

Dieses Skript prüft, ob eine lokale SQLite-Datenbank bereits existiert.
Wenn nicht, konfiguriert es Django für SQLite und führt alle Migrationen
aus, damit die benötigten Tabellen für die Anwendung angelegt werden.

Verwendung:
    python create_database.py
"""

# Importieren Sie das Django-Modul
import os
from django.conf import settings

# Name der SQLite-Datenbankdatei.
DATABASE_NAME = 'db.sqlite3'

# Setzen Sie die Einstellungen für das Django-Projekt.
settings.configure(
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(os.getcwd(), '%s' % DATABASE_NAME),
        }
    }
)

# Überprüfen, ob die Datenbank bereits existiert.
if not os.path.exists(DATABASE_NAME):
    # Wenn die Datenbank nicht existiert, initialisieren Sie Django und legen Sie die Tabellen an.
    import django
    django.setup()

    # Fügen Sie hier Ihre Django-Modelle hinzu, falls erforderlich.

    # Erzeugen Sie die leere Datenbank durch Ausführen aller Migrationen.
    from django.core.management import call_command
    call_command('migrate')

    print("Leere SQLite-Datenbank: '%s' wurde erfolgreich erstellt." % DATABASE_NAME)
else:
    # Die Datenbank existiert bereits, daher wird nichts neu erstellt.
    print("Die SQLite-Datenbank '%s' existiert bereits!" % DATABASE_NAME)
