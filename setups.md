# 🎮 How to set up **Pygame** in **VSCode**

## 1. Install Pygame

First, you need to install **Pygame** into your Python environment.

Open the **VSCode terminal** (`Ctrl + ~`) and type:

In terminal run this command:

```
pip install pygame



```

✅ This will download and install Pygame.

## 2. Recommended VSCode Extensions for Pygame Development

You don’t need a special Pygame extension — but the following ones will help when working with  **Pygame games** :

| Extension                           | Why it's useful                                                                               |
| ----------------------------------- | --------------------------------------------------------------------------------------------- |
| **Python (by Microsoft)**     | For running/debugging Python code                                                             |
| **Pylance**                   | Fast autocomplete (especially for Pygame methods like `pygame.draw`,`pygame.mixer`, etc.) |
| **Code Runner**               | Quickly run your `.py`files without manually using the terminal                             |
| **Auto Rename Tag**(optional) | Helps if you also build HTML UI with Pygame + web projects                                    |
| **GitLens**(optional)         | Track changes easily if you make a bigger game project                                        |

## 3. Example: A Tiny Pygame Program

After you install Pygame, you can create a simple game script like this to test:

```
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Hello Pygame")

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))  # Fill the screen with black
    pygame.draw.circle(screen, (255, 0, 0), (300, 200), 50)  # Draw a red circle
    pygame.display.update()

```


✅ Save it as something like `game.py`, then **Run** it inside VSCode

# ❗ Important Notes for Pygame

* Always **save** your script before running.
* Make sure your **Python interpreter** is correctly set inside VSCode (check bottom-left corner).
* If you run into errors like "pygame not found," double-check that you installed Pygame into the  **right Python environment** .


# 🧩 Bonus Tip

If you want even smoother development:

* Install the **Python Environment Manager** extension (`ms-python.python-environment-manager`).
* It helps manage `venv` and dependencies when working on bigger games.

wir machen alles zuzammen,
