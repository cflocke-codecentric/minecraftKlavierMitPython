# Fast geschafft! Jetzt muessen nur noch die schwarzen
# Tasten oben auf die weissen drauf setzen und dann haben wir
# unsere komplette Oktave!

# Importiere zusaetzliche Bibliotheken
from mcpi.minecraft import Minecraft

# Stelle die Verbindung mit Minecraft her.
# Achte darauf, dass Minecraft gestartet ist und
# du dich in einer Welt bewegen kannst.
mc = Minecraft.create()

# Hier hast du ein Muster für eine Funktion, die dir eine weisse
#Taste erzeugt:
def white_key(x, y, z):
    mc.setBlocks(x, y - 1, z, x + 2, y - 1, z + 14, 44)

# Und hier das Muster für eine Funktion fuer eine
# schwarze Taste:
def black_key(x, y, z):
    mc.setBlocks(x, y - 1, z, x + 1, y - 1, z + 8, 49)

# Hier hast du eine Funktion, die dir bisher nur die weissen
# Tasten erzeugt. Kannst du die Funktion erweitern, damit
# sie auch schwarze Tasten auf die weissen Tasten oben drauf setzt?
# (Vll. in einer separaten for-Schleife?)
def make_octave(x, y, z):
    for i in range(0, 19, 3):
        white_key(x + i, y, z)
    for i in range(2, 18, 3):
        black_key(x + i, y, z)


# Guck dir deine Oktave genau an! Kann es sein, dass eine schwarze Taste
# zu viel erstellt wurde?
def make_octave(x, y, z):
    for i in range(0, 19, 3):
        white_key(x + i, y, z)
    for i in range(2, 18, 3):
        if i != 8:
            black_key( x + i, y, z)
