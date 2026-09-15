# How-To: Python Interpreter, Virtual Environments und PIP

Diese Anleitung erklärt die wichtigsten Schritte für die Arbeit mit Python: Installation des Interpreters, Überprüfung der Version, virtuelle Umgebungen sowie den Umgang mit PIP und `requirements.txt`.

---

# 1. Python Interpreter installieren

## Windows

#x### Alternative 1: Installer von https://www.python.org/downloads/ herunterladen.

1. Python von https://www.python.org/downloads/ herunterladen.
2. Installer starten.
3. Wichtig: **"Add Python to PATH"** aktivieren.
4. Auf **Install Now** klicken.

#### Alternative 2: über winget installieren.

```powershell
winget install --id Python.Python.3.14 -e
```

Danach kann Python mit `python` bzw. `py` verwendet werden. Wenn winget das PATH-Setup nicht korrekt setzt, bitte den Terminal- oder VS-Code-Ordner neu starten.

### Installation prüfen

```powershell
python --version
```

oder

```powershell
py --version
```

Beispielausgabe:

```text
Python 3.12.4
```

---

## Linux (Ubuntu/Debian)

Installation:

```bash
sudo apt update
sudo apt install python3 python3-pip
```

Prüfen:

```bash
python3 --version
```

---

## macOS

Installation über Homebrew:

```bash
brew install python
```

Prüfen:

```bash
python3 --version
```

---

# 2. Interpreter und Version prüfen

## Python-Version anzeigen

```bash
python --version
```

oder

```bash
python3 --version
```

Ergebnis:

```text
Python 3.12.4
```

---

## Pfad des Interpreters anzeigen

### Windows

```powershell
where python
```

### Linux / macOS

```bash
which python
```

oder

```bash
which python3
```

Beispiel:

```text
/usr/bin/python3
```

---

# 3. Virtuelle Umgebungen (Virtual Environments)

Virtuelle Umgebungen ermöglichen projektbezogene Python-Installationen und verhindern Konflikte zwischen Abhängigkeiten verschiedener Projekte.

## Virtuelle Umgebung erstellen

```bash
python -m venv .venv
```

oder

```bash
python3 -m venv .venv
```

## Virtuelle Umgebung aktivieren

### Windows (PowerShell)

```powershell
.\.venv\Scripts\Activate.ps1
```

### Windows (CMD)

```cmd
.venv\Scripts\activate.bat
```

### Linux / macOS

```bash
source .venv/bin/activate
```

## Virtuelle Umgebung deaktivieren

```bash
deactivate
```

---

# 4. PIP Grundlagen

PIP ist der Standard-Paketmanager für Python.

```bash
pip --version
```

---

# 5. Pakete installieren

## Einzelnes Paket installieren

```bash
pip install requests
```

## Bestimmte Version installieren

```bash
pip install requests==2.32.3
```

## Paket aktualisieren

```bash
pip install --upgrade requests
```

## Mehrere Pakete installieren

```bash
pip install requests pandas numpy
```

---

# 6. Wichtige PIP-Befehle

## Installierte Pakete anzeigen

```bash
pip list
```

## Detailinformationen zu einem Paket

```bash
pip show requests
```

## Paket deinstallieren

```bash
pip uninstall requests
```

---

# 7. PIP Freeze

```bash
pip freeze
```

---

# 8. requirements.txt erstellen

```bash
pip freeze > requirements.txt
```

---

# 9. Pakete aus requirements.txt installieren

```bash
pip install -r requirements.txt
```

---

# Typischer Workflow

```bash
mkdir my_project
cd my_project
python -m venv .venv
source .venv/bin/activate
pip install requests pandas
pip freeze > requirements.txt
deactivate
```

## Best Practice

✅ Immer mit einer virtuellen Umgebung arbeiten  
✅ `requirements.txt` ins Git-Repository aufnehmen  
✅ Vor dem Commit `pip freeze > requirements.txt` aktualisieren  
✅ Keine globalen Paketinstallationen für Projektabhängigkeiten verwenden  
✅ Versionsnummern in `requirements.txt` festhalten
