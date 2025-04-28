# 📚 Lektion: Ausdrücke (Expressions) in Python verstehen

---

## 💭 Was sind Ausdrücke (Expressions)?

Ein **Ausdruck** (englisch: **Expression**) ist jede Kombination von **Werten**, **Variablen**, **Operatoren** und **Funktionen**, die **einen Wert ergeben**.

**Kurz gesagt:**

> Ein Ausdruck ist ein Stück Code, das ausgewertet werden kann und ein Ergebnis produziert.

Beispiele:

```python
2 + 3
"Hallo" + " Welt"
x * y
len("Python")
```

Alle diese Beispiele **liefern einen Wert**.

---

## 🔄 Unterschied: Ausdruck vs. Anweisung

| Ausdruck                                  | Anweisung                             |
| :---------------------------------------- | :------------------------------------ |
| Gibt einen Wert zurück                   | Tut etwas (z.B. eine Variable setzen) |
| Kann Teil eines größeren Ausdrucks sein | Steht für sich alleine               |

**Beispiele:**

- Ausdruck:

  ```python
  5 + 7
  ```

  (ergibt 12)
- Anweisung:

  ```python
  x = 5 + 7
  ```

  (setzt x auf 12)

---

## 🛠️ Woraus bestehen Ausdrücke?

- **Literale**: Zahlen, Zeichenketten, Listen usw.
  - `42`, `'Hallo'`, `[1, 2, 3]`
- **Variablen**:
  - `alter`, `name`, `punktzahl`
- **Operatoren**:
  - `+`, `-`, `*`, `/`, `//`, `%`, `==`, `!=`, `<`, `>`, `and`, `or`, etc.
- **Funktionsaufrufe**:
  - `len(name)`, `sum([1,2,3])`
- **Kombinationen daraus**:
  - `(a + b) * (c - d)`

---

## ✨ Beispiele für Ausdrücke in Python

```python
# Einfacher mathematischer Ausdruck
4 * 5

# String-Verkettung
"Guten" + " Tag"

# Listenoperation
[1, 2, 3] + [4, 5]

# Funktionsaufruf
len("Python")

# Logischer Ausdruck
5 > 3 and 2 < 4
```

Jeder dieser Ausdrücke kann "ausgewertet" werden und ergibt einen Wert.

---

## 🤔 Wie kann man Ausdrücke besser verstehen?

- **Schrittweise denken**: Zerlege komplexe Ausdrücke in kleinere Teile.
- **Ergebnisse anschauen**: Lass Python Ausdrücke auswerten und beobachte die Rückgabewerte.
- **Mit der Konsole üben**: Schreibe kleine Ausdrücke in der Python-Konsole und teste sofort.

---

## 📘 Mini-Übung: Was sind die Ergebnisse dieser Ausdrücke?

```python
3 * (2 + 5)

"Hallo" + " Welt"

10 // 3

len([1, 2, 3, 4])

7 > 2 and 1 == 0
```

> **Antworten:** 21, "Hallo Welt", 3, 4, False

---

# 💚 Zusammenfassung

| Begriff   | Bedeutung                         |
| :-------- | :-------------------------------- |
| Ausdruck  | Code, der einen Wert ergibt       |
| Anweisung | Code, der eine Aktion durchführt |
| Beispiele | `4+5`, `len("Test")`, `a*b` |

---

# ✨ Tipp zum Weiterlernen

- Experimentiere mit eigenen Ausdrücken!
- Kombiniere Operatoren und Funktionen.
- Übe, Unterschiede zwischen Ausdrücken und Anweisungen zu erkennen.
