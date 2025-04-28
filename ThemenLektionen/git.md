# 📚 Git Lektion: Einführung und wichtige Befehle

## 🧠 Was ist Git?

**Git** ist ein Programm, das hilft, den Verlauf deiner Dateien zu speichern und zu verwalten.

Es merkt sich:

* Was du geändert hast,
* Wer die Änderung gemacht hat,
* Wann du etwas geändert hast.

Man nennt das auch  **Versionskontrolle** .

Mit Git kannst du:

* Fehler rückgängig machen,
* alte Versionen deiner Arbeit wiederherstellen,
* im Team arbeiten, ohne euch gegenseitig zu stören.

## 🛠 Installation

* **Git herunterladen** :

  [https://git-scm.com/downloads](https://git-scm.com/downloads)
* **Prüfen, ob Git installiert ist** :
* ```
  git --version

  ```

Wenn eine Versionsnummer erscheint, ist Git richtig installiert.

## 🏗️ Dein erstes Git-Projekt

### 1. Neues Projekt starten:

Gehe in dein Projektverzeichnis und schreibe:

git init

👉 Damit wird ein neues Git-Repository (unsichtbarer `.git`-Ordner) erstellt.

---

### 2. Dateien überwachen

Um zu sehen, welche Dateien geändert wurden:

```
git status
```

### 3. Dateien zur Speicherung vormerken

Wenn du eine Datei gespeichert hast und Git sagen möchtest:

"Ich möchte diese Datei speichern", schreibst du:

git add dateiname

```

```

Um **alle** Dateien auf einmal hinzuzufügen:

```
git add .
```

👉 Beispiel:

```
git add main.py

```

### 4. Änderungen speichern (Commit)

Jetzt sagst du Git:

"Speichere diese Änderungen mit einer kleinen Beschreibung."

```
git commit -m "Startprojekt erstellt"

```

```

```



### 5. Verlauf anzeigen

Alle gespeicherten Versionen anzeigen:

```
git log

```


## 🌐 Arbeiten mit GitHub (Online-Backup)

Wenn du deine Arbeit online speichern willst:

1. Repository auf [Git](https://github.com/)
2. [Hub.com](https://github.com/) erstellen.
3. Verbinden:

```
git remote add origin https://github.com/dein-benutzername/dein-repo.git

```

```

```

## 🏃‍♂️ Die wichtigsten Git-Befehle auf einen Blick

| Befehl                        | Bedeutung                            |
| ----------------------------- | ------------------------------------ |
| `git init`                  | Neues Git-Repository erstellen       |
| `git status`                | Status der Dateien anzeigen          |
| `git add dateiname`         | Datei zum Commit vormerken           |
| `git add .`                 | Alle Änderungen vormerken           |
| `git commit -m "Nachricht"` | Änderungen speichern                |
| `git log`                   | Verlauf anzeigen                     |
| `git remote add origin URL` | GitHub-Repository verbinden          |
| `git push -u origin main`   | Projekt auf GitHub hochladen         |
| `git pull`                  | Änderungen vom Server herunterladen |



## 🎯 Kleine Übung

1. Erstelle einen neuen Ordner.
2. Schreibe ein kleines Python-Programm (`hello.py`).
3. Initialisiere Git (`git init`).
4. Füge die Datei hinzu (`git add hello.py`).
5. Committe die Datei (`git commit -m "Mein erstes Commit"`).
6. (Optional) Erstelle ein GitHub-Repo und pushe dein Projekt hoch


# 🚀 Zusammenfassung

* **Git** hilft dir, deine Projekte sicher zu speichern.
* Du solltest regelmäßig  **commiten** , damit du deine Arbeit nachvollziehen kannst.
* Mit **GitHub** kannst du deine Projekte überall verfügbar machen!
