# 📚 Lektion: Code-Formatierung und PEP8 (Python Stilregeln)

---

## 🧐 Warum ist Code-Formatierung wichtig?

- **Lesbarkeit**: Gut formatierter Code ist für dich und andere leichter zu verstehen.
- **Wartbarkeit**: Sauberer Code kann später einfacher verbessert oder repariert werden.
- **Teamarbeit**: Wenn alle denselben Stil benutzen, gibt es weniger Missverständnisse.
- **Professionalität**: Gute Projekte folgen einem Standard, den andere sofort erkennen.

**💡 Merksatz:**  
_"Code wird öfter gelesen als geschrieben!"_

---

## 🛁 Was ist PEP8?

- **PEP** steht für **Python Enhancement Proposal**.
- **PEP8** ist das Dokument, das Regeln und Empfehlungen zur **Formatierung von Python-Code** beschreibt.

**Kurz gesagt:**  
👉 **PEP8 ist der offizielle Python-Style-Guide.**

---

## 🛠️ Wichtige Regeln aus PEP8

| Regel | Erklärung | Beispiel |
|:------|:-----------|:---------|
| Einrückung | 4 Leerzeichen pro Ebene | `if x:\n    print(x)` |
| Zeilenlänge | Maximal **79 Zeichen** pro Zeile | Lange Zeilen umbrechen |
| Leere Zeilen | 2 Leerzeilen zwischen Klassen/Funktionen | `def foo():` (2 Zeilen Abstand) |
| Variablennamen | **Klein** mit Unterstrichen | `user_name`, `total_sum` |
| Klassennamen | **CamelCase** (Anfangsbuchstaben groß) | `class UserProfile:` |
| Abstand | Nach `,`, `=`, `+`, `-`, etc. ein Leerzeichen | `a = b + c` |
| Kommentare | Kurz, sinnvoll, immer aktuell halten | `# Berechnung des Endwerts` |

---

## 🔥 Beispiele: Schlechter vs. guter Stil

**❌ Schlecht:**

```python
def add(a,b):return a+b
```

**✅ Gut:**

```python
def add(a, b):
    return a + b
```

---

## ⚡ Tools für automatische Formatierung

Beliebte Tools:

- **`black`**: automatisch schöner Code.
- **`flake8`**: überprüft, ob dein Code PEP8 folgt.
- **`pylint`**: noch gründlichere Analyse deines Codes.

👉 Installation:

```bash
pip install black flake8 pylint
```

👉 Code automatisch formatieren mit `black`:

```bash
black .
```

(Das formatiert alle Python-Dateien im aktuellen Ordner.)

---

## ✏️ PEP8 in VSCode aktivieren

1. Erweiterung **Python** von Microsoft installieren.
2. Einstellungen öffnen:
   - Datei > Einstellungen > Suche: `Format On Save`
   - Haken setzen bei **Format On Save**.
3. Formatter auswählen:
   - Python > Formatting > Provider auf `black` oder `autopep8` setzen.

Jetzt wird dein Code **beim Speichern** automatisch formatiert! 🛠️

---

# 📄 Zusammenfassung: Wichtigste Punkte

| Thema | Tipp |
|:------|:-----|
| Einrückung | 4 Leerzeichen |
| Variablennamen | Klein_mit_unterstrichen |
| Kommentare | Sinnvoll und aktuell |
| Zeilenlänge | Max. 79 Zeichen |
| Klassen | CamelCase-Stil |
| Tools | black, flake8, pylint |

---

# 🧹 Übungsaufgabe

👉 Korrigiere diesen Code nach PEP8:

```python
def greeting(name):print("Hallo,"+name+"!")
greeting("Anna")
```

### Erwartetes Ergebnis:

```python
def greeting(name):
    print("Hallo, " + name + "!")

greeting("Anna")
