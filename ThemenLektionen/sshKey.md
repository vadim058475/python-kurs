```

```


# 📚 Lektion: Was ist SSH und wie benutzt man es?

## 🧐 Was ist SSH?

**SSH** steht für **Secure Shell**.

👉 Es ist ein **sicheres Protokoll**, mit dem du dich auf einem anderen Computer anmelden kannst – so, als ob du direkt davor sitzt.

SSH wird oft verwendet:

- Um Server fernzusteuern
- Um Dateien sicher zu übertragen
- Um GitHub sicher zu nutzen (ohne jedes Mal Benutzername und Passwort einzugeben!)

---

## 🔒 Wie funktioniert SSH?

- Dein Computer erstellt ein **Schlüsselpaar**:
  - **Privater Schlüssel** (private key): bleibt **geheim** auf deinem Computer.
  - **Öffentlicher Schlüssel** (public key): wird an den Server (oder GitHub) geschickt.
- Wenn du dich verbindest, beweist dein Computer mit dem privaten Schlüssel, dass er zu dir gehört.
- **Benutzername/Passwort** sind nicht mehr nötig!

👉 **SSH = sicheres Einloggen ohne Passwort.**

---

## 🛠️ SSH Schüsselpaar erstellen (lokal)

Hier lernst du, wie du **lokal ein SSH-Schlüsselpaar erstellst** und **mit GitHub verbindest**.

### 1. Prüfen: Gibt es schon einen Schlüssel?

Terminal öffnen und tippen:

```bash
ls ~/.ssh
```

Wenn du Dateien wie `id_rsa` oder `id_ed25519` siehst, hast du bereits einen Schlüssel.

---

### 2. Neuen SSH-Schlüssel erstellen

```bash
ssh-keygen -t ed25519 -C "deine.email@beispiel.com"
```

- `-t ed25519`: moderne, sichere Verschlüsselung.
- `-C`: Kommentar (deine E-Mail).

**Enter** drücken für Standardspeicherort `~/.ssh/id_ed25519`.

Optional ein Passwort setzen (oder Enter für kein Passwort).

---

### 3. SSH-Agent starten und Schlüssel laden

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

---

### 4. Öffentlichen Schlüssel kopieren

```bash
cat ~/.ssh/id_ed25519.pub
```

Den gesamten Text kopieren (beginnt mit `ssh-ed25519` und endet mit deiner E-Mail).

---

## 🌐 SSH-Schlüssel bei GitHub einfügen

1. Gehe zu [GitHub.com](https://github.com/).
2. Profilbild > **Settings** > **SSH and GPG keys**.
3. **New SSH key** klicken.
4. Name vergeben und den kopierten Schlüssel einfügen.
5. Speichern.

---

## 🔗 Testen der Verbindung

```bash
ssh -T git@github.com
```

Erwartete Antwort:

```
Hi deinBenutzername! You've successfully authenticated, but GitHub does not provide shell access.
```

---

## 🚀 Git verwenden mit SSH

Ab jetzt über **SSH-URL klonen**:

```bash
git clone git@github.com:deinBenutzername/deinRepository.git
```

Kein Passwort mehr nötig bei `git push` oder `git pull`!

---

# 📄 Zusammenfassung: SSH in Kürze

| Begriff              | Bedeutung                                       |
| :------------------- | :---------------------------------------------- |
| SSH                  | Sicheres Protokoll zum Anmelden und Übertragen |
| SSH-Schlüsselpaar   | Privater + Öffentlicher Schlüssel             |
| Verbindung zu GitHub | Öffentlichen Schlüssel auf GitHub hochladen   |
| Vorteil              | Kein Passwort nötig bei Git-Befehlen           |

---

# 🧹 Bonus: Wichtige SSH-Befehle

| Befehl                        | Erklärung                    |
| :---------------------------- | :---------------------------- |
| `ssh-keygen -t ed25519`     | Neues Schüsselpaar erstellen |
| `eval "$(ssh-agent -s)"`    | SSH-Agent starten             |
| `ssh-add ~/.ssh/id_ed25519` | Privaten Schlüssel laden     |
| `ssh -T git@github.com`     | Verbindung testen             |

---

**Viel Erfolg beim sicheren Arbeiten mit SSH! 🚀**
