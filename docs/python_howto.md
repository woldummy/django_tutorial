# How-To: Python Interpreter, Virtual Environments und PIP

Python ist eine moderne, leicht verständliche Programmiersprache, die in vielen Bereichen eingesetzt wird.

Diese Anleitung erklärt die wichtigsten Schritte für die Arbeit mit Python:

- Installation des Interpreters
- Überprüfung der Version
- Erstellung und Nutzung virtueller Umgebungen
- Umgang mit PIP und `requirements.txt`

---

## Grundlegende Konzepte der Konsole

### Das Dateisystem

Das Dateisystem lässt sich als Baum vorstellen. Die Wurzel ist der oberste Punkt dieses Baumes und der Ausgangspunkt für alles andere. Unter Windows ist die Wurzel typischerweise `C:\` oder ein anderes Laufwerk wie `D:\`. Auf Linux und macOS ist die Wurzel `/`.

Jeder dieser Ordner kann wieder weitere Ordner und Dateien enthalten. So entsteht eine Baumstruktur: Von der Wurzel aus verzweigen sich alle weiteren Verzeichnisse und Dateien.

Die Wurzel ist also der absolute Anfang des Dateisystems. Wenn du einen Pfad mit der Wurzel beginnst, spricht man von einem absoluten Pfad. Ein absoluter Pfad beschreibt den kompletten Weg vom Anfang des Dateisystems bis zu einer Datei oder einem Ordner. Deshalb ist ein absoluter Pfad immer eindeutig und unabhängig davon, wo du gerade im Terminal bist.

Ein relativer Pfad beginnt nicht bei der Wurzel, sondern dort, wo du dich gerade befindest. Beispiel: Wenn du im Ordner `C:\Users\Max` bist, dann ist `./Desktop` derselbe Ordner wie `C:\Users\Max\Desktop`. Das gleiche Prinzip gilt auch auf Linux/macOS: Wenn du in `/home/max` bist, dann ist `./projekt` dasselbe wie `/home/max/projekt`.

Beispiele für Pfade können entweder absolut oder relativ sein:

- absolut: `/home/max/projekt` oder `C:\Users\Max\projekt`
- relativ: `./projekt`, `../docs`

Der Pfadtrenner unterscheidet sich je nach Betriebssystem:

- auf Linux/macOS verwendet man `/` als Trennzeichen, z. B. `/home/max/projekt`
- auf Windows verwendet man `\` als Trennzeichen, z. B. `C:\Users\Max\projekt`

### Das Terminal bzw. Konsole

Das Terminal ist ein Programm, das es dir ermöglicht, direkt mit dem Betriebssystem zu kommunizieren. Der Prompt ist die Eingabezeile des Terminals und zeigt normalerweise den aktuellen Ordner an, z. B. `C:\Users\Max>` unter Windows oder `~/projekte/python$` auf Linux/macOS.

Wenn du im Terminal arbeitest, bist du immer in einem bestimmten Ordner. Der Prompt zeigt dir genau diesen Ort an, damit du weißt, wo die Shell gerade arbeitet. Unter MS Windows gibt es die Eingabeaufforderung (CMD) und PowerShell. Beide sind Terminals, die sich in der Syntax unterscheiden.

Auf Linux und macOS gibt es verschiedene Shells, z. B. `bash`, `zsh` oder `fish`. Die meisten Tutorials verwenden `bash` oder `zsh`.

Wichtige Befehle sind:

- `ls` bzw. `dir` = Inhalte eines Ordners anzeigen
- `cd` = in einen anderen Ordner wechseln
- `mkdir` = neuen Ordner anlegen
- `cp` = Dateien oder Ordner kopieren
- `pwd` = aktuellen Ordner anzeigen

---

## Python Interpreter installieren

### Windows

#### Alternative 1: Installer von https://www.python.org/downloads/ herunterladen

1. Python von https://www.python.org/downloads/ herunterladen.
2. Den Installer starten.
3. Wichtig: **"Add Python to PATH"** aktivieren.
4. Auf **Install Now** klicken.

#### Alternative 2: über `winget` installieren

```powershell
winget install --id Python.Python.3.14 -e
```

Danach kann Python mit `python`, `python3` oder `py` verwendet werden. Wenn das PATH-Setup durch `winget` nicht korrekt gesetzt wurde, sollte das Terminal oder VS Code neu gestartet werden.

#### Starten des Interpreters

Python kann auf verschiedenen Betriebssystemen unterschiedlich aufgerufen werden:

```bash
python
python3
py
```

- Auf Linux/macOS wird häufig `python3` verwendet.
- Auf Windows wird oft `py` oder `python` verwendet.

#### Installation prüfen

```powershell
python --version
```

oder

```powershell
py --version
```

Beispielausgabe:

```text
Python 3.14.7
```

---

### Linux (Ubuntu/Debian)

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

### macOS

Installation über Homebrew:

```bash
brew install python
```

Prüfen:

```bash
python3 --version
```

---

## Interpreter und Version prüfen

### Python-Version anzeigen

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

### POSIX (Linux/macOS)

Um den Python-Befehl auf POSIX-Systemen zu prüfen, kann `type` oder `which` verwendet werden:

```bash
type python
type python3
which python
which python3
```

Beispiel:

```text
/usr/bin/python3
```

### Windows

In der Windows-Eingabeaufforderung wird der Pfad meistens mit `where.exe` überprüft:

```cmd
where.exe python
where.exe python3
```

`where.exe` funktioniert nur, wenn das Verzeichnis mit den ausführbaren Dateien korrekt im `PATH` enthalten ist. Das gilt insbesondere für `%windir%\System32`.

### PowerShell

```powershell
Get-Command python
gcm *python*
```

`gcm` ist ein Alias von `Get-Command` und hilft dabei, die passenden ausführbaren Programme zu finden.

---

### Python im interaktiven Modus starten

Mit dem Python-Interpreter kann man direkt Befehle eingeben. Dafür startet man Python ohne Skriptdatei:

```bash
python
```

oder

```bash
python3
```

Danach erscheint die interaktive Eingabeaufforderung:

```text
>>> print("Hallo Welt")
Hallo Welt
```

Das ist ein einfaches erstes Programm, das den Text `Hallo Welt` auf der Konsole ausgibt.

---

### Pfad des Interpreters anzeigen

#### Windows

```powershell
where python
```

#### Linux / macOS

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

## Virtuelle Umgebungen (Virtual Environments)

Virtuelle Umgebungen ermöglichen projektbezogene Python-Installationen und verhindern Konflikte zwischen Abhängigkeiten verschiedener Projekte.

### Virtuelle Umgebung erstellen

```bash
python -m venv .venv
```

oder

```bash
python3 -m venv .venv
```

### Virtuelle Umgebung aktivieren

#### Windows (PowerShell)

```powershell
.\.venv\Scripts\Activate.ps1
```

#### Windows (CMD)

```cmd
.venv\Scripts\activate.bat
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

### Virtuelle Umgebung deaktivieren

```bash
deactivate
```

---

## 4. PIP Grundlagen

PIP ist der Standard-Paketmanager für Python.

```bash
pip --version
```

---

## Pakete installieren

### Einzelnes Paket installieren

```bash
pip install requests
```

### Bestimmte Version installieren

```bash
pip install requests==2.32.3
```

### Paket aktualisieren

```bash
pip install --upgrade requests
```

### Mehrere Pakete installieren

```bash
pip install requests pandas numpy
```

---

## Wichtige PIP-Befehle

### Installierte Pakete anzeigen

```bash
pip list
```

### Detailinformationen zu einem Paket

```bash
pip show requests
```

### Paket deinstallieren

```bash
pip uninstall requests
```

---

## PIP Freeze

```bash
pip freeze
```

---

##  requirements.txt erstellen

```bash
pip freeze > requirements.txt
```

---

## Pakete aus requirements.txt installieren

```bash
pip install -r requirements.txt
```

---

## Typischer Workflow

```bash
mkdir my_project
cd my_project
python -m venv .venv
source .venv/bin/activate
pip install requests pandas
pip freeze > requirements.txt
deactivate
```

### Best Practice

✅ Immer mit einer virtuellen Umgebung arbeiten  
✅ `requirements.txt` ins Git-Repository aufnehmen  
✅ Vor dem Commit `pip freeze > requirements.txt` aktualisieren  
✅ Keine globalen Paketinstallationen für Projektabhängigkeiten verwenden  
✅ Versionsnummern in `requirements.txt` festhalten
