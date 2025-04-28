# 📚 Lektion: Variablen in Python verstehen

---

## 🤔 Was ist eine Variable?

Eine **Variable** ist ein **Name**, der auf einen **Wert** zeigt.
Mit Variablen kannst du Werte speichern und später im Programm wiederverwenden.

**Kurz gesagt:**

> Eine Variable merkt sich etwas für dich.

Beispiele:

```python
name = "Anna"
alter = 12
punktzahl = 95.5
```

Jetzt speichert `name` den Text **"Anna"**, `alter` die Zahl **12**, usw.

---

## 🫠 Wie erstellt man eine Variable?

Ganz einfach:

```python
variablenname = wert
```

Beispiele:

```python
x = 5
y = "Hallo"
```

---

## 🛠️ Regeln für Variablennamen

- Nur **Buchstaben**, **Zahlen** und **Unterstriche** (`_`).
- **Keine** Leerzeichen oder Sonderzeichen (!, ?, %, ...).
- **Darf nicht** mit einer Zahl beginnen.
- Variablennamen sind **case-sensitive** (Groß-/Kleinschreibung wichtig).
- Verwende **aussagekräftige Namen** (nicht nur `x` oder `y`).

**Gültig:**

```python
alter = 15
user_name = "Tom"
punktzahl_gesamt = 88
```

**Ungültig:**

```python
2alter = 15   # Fehler: Name beginnt mit einer Zahl
user-name = "Tom"  # Fehler: Bindestrich nicht erlaubt
```

---

## 🔯 Unterschiedliche Typen von Variablen

| Typ                  | Beispiel                          |
| :------------------- | :-------------------------------- |
| Zahl (int, float)    | `alter = 12`, `preis = 19.99` |
| Text (string)        | `name = "Lisa"`                 |
| Liste                | `punkte = [10, 20, 30]`         |
| Wahrheitswert (bool) | `ist_fertig = True`             |

Python erkennt den Typ automatisch!

---

## 💪 Beispiele für Variablen

```python
# Zahl
anzahl = 5

# Text
stadt = "Berlin"

# Wahrheitswert
ist_kalt = False

# Liste
farben = ["rot", "blau", "grün"]
```

---

## ✨ Variablen verwenden

Du kannst mit Variablen rechnen oder sie ausgeben:

```python
# Mathematische Operation
breite = 10
hoehe = 5
flaeche = breite * hoehe
print(flaeche)

# Text verketten
vorname = "Max"
nachname = "Muster"
voller_name = vorname + " " + nachname
print(voller_name)
```

---

## 📘 Mini-Übung: Erstelle eigene Variablen!

1. Erstelle eine Variable `hundename` und speichere deinen Lieblings-Hundenamen.
2. Erstelle zwei Zahlen `a` und `b` und berechne ihre Summe.
3. Erstelle eine Liste `obst` mit drei Fruchtnamen.

---

# 💚 Zusammenfassung

| Begriff         | Erklärung                           |
| :-------------- | :----------------------------------- |
| Variable        | Speicher für einen Wert             |
| Erstellen       | `name = wert`                      |
| Typen           | Zahl, Text, Liste, Boolescher Wert   |
| Wichtige Regeln | Keine Sonderzeichen, sinnvolle Namen |

---

# 🚀 Tipp für Fortgeschrittene

- Variablen können ihren Wert ändern!
- Python ist dynamisch: Eine Variable kann verschiedene Typen übernehmen.

Beispiel:

```python
x = 5
x = "Jetzt ein Text!"
print(x)
```

Python erlaubt das - aber **achte auf Klarheit** im Code!
