# Hier sollst du eine Funktion definieren welche dir eine einzelne weisse Taste erstellt!
# Sieh dir dazu deine Skizze an und schau dir die Dimensionen an, wie groß eine
# weisse Taste sein soll. Benutze am besten dazu einen hellen Block z.B. mit der
# ID 44.

# Importiere zusaetzliche Bibliotheken
from mcpi.minecraft import Minecraft

# Stelle die Verbindung mit Minecraft her.
# Achte darauf, dass Minecraft gestartet ist und
# du dich in einer Welt bewegen kannst.
mc = Minecraft.create()

# Erstelle die Funktion hier, mithilfe der mc-Variablen:
# (Gehe davon aus, dass die erste Position der Standpunkt des Spielers ist.)
def white_key(x, y, z):
    mc.setBlocks(x, y - 1, z, x + 2, y - 1, z + 14, 44, 7)
