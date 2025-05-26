# 📚 Lektion: Einführung in Pygame (Spieleprogrammierung in Python)

---

## 🎮 Was ist Pygame?

- **Pygame** ist eine **Bibliothek** für Python.
- Sie hilft dir, **Spiele** und **grafische Programme** zu erstellen.
- Du kannst damit **Bilder anzeigen**, **Töne abspielen** und **Tastatur/Maus-Eingaben** verarbeiten.

**Kurz gesagt:**

> Mit Pygame kannst du eigene kleine Spiele programmieren!

---

## 🚀 Installation

Zuerst musst du Pygame installieren:

```bash
pip install pygame
```

---

## 📘 Erstes einfaches Pygame-Programm

```python
import pygame
import sys

# Pygame initialisieren
pygame.init()

# Fenster erstellen
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Mein erstes Pygame-Programm")

# Farben definieren
WEISS = (255, 255, 255)
BLAU = (0, 0, 255)

# Hauptschleife
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Bildschirm weiß färben
    screen.fill(WEISS)

    # Blaues Rechteck zeichnen
    pygame.draw.rect(screen, BLAU, (100, 100, 50, 50))

    # Fenster aktualisieren
    pygame.display.update()
```

---

## 📚 Wichtige Begriffe in Pygame

| Begriff                                | Bedeutung                                   |
| :------------------------------------- | :------------------------------------------ |
| `pygame.init()`                      | Startet Pygame                              |
| `screen = pygame.display.set_mode()` | Erstellt ein Fenster                        |
| `screen.fill(farbe)`                 | Färbt den Hintergrund                      |
| `pygame.draw.rect()`                 | Zeichnet ein Rechteck                       |
| `pygame.display.update()`            | Aktualisiert das Fenster                    |
| Ereignisse (`event`)                 | Z.B. Maus, Tastatur oder Fenster schließen |

---

## 🔍 Was passiert hier genau?

- **Pygame wird gestartet**.
- **Ein Fenster wird erstellt**.
- **Eine Endlosschleife** wartet auf Aktionen (z.B. Fenster schließen).
- **Zeichnen** wird immer wieder gemacht.
- **Der Bildschirm wird aktualisiert**.

---

## 🧐 Typische Pygame-Elemente in Spielen

- Spielfiguren (**Sprites**)
- Bewegung durch **Tastatur/Maus-Eingaben**
- **Kollisionen** zwischen Objekten
- **Level** und **Punktestände**
- **Töne** und **Musik**

---

## 📖 Mini-Übung: Dein erstes Spiel erweitern

✅ Aufgaben:

- Ändere die Hintergrundfarbe.
- Zeichne zwei verschiedene Formen (z.B. ein Rechteck und einen Kreis).
- Lass die Figur sich mit den Pfeiltasten bewegen.

**Tipp:** Mit `pygame.key.get_pressed()` kannst du Tasten abfragen!

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    x -= 5
if keys[pygame.K_RIGHT]:
    x += 5
```

---

# 📊 Zusammenfassung

| Thema    | Erklärung                             |
| :------- | :------------------------------------- |
| Pygame   | Bibliothek für Spieleprogrammierung   |
| Fenster  | `pygame.display.set_mode()`          |
| Zeichnen | `pygame.draw`-Funktionen             |
| Schleife | Warten auf Ereignisse und neu zeichnen |

---

# 🚀 Nächste Schritte

- Bilder laden und anzeigen
- Musik abspielen
- Kollisionserkennung
- Eigenes kleines Spiel entwickeln!

---

**Viel Spaß beim Coden und Spielen! 🎮💪**
