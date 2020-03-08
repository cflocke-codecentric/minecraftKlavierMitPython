# In dieser Aufgabe sollst du nicht nur eine weisse Taste erzeugen,
# sondern die einer ganzen Oktave. Dh. ganze 7 Stueck!
# Du kannst natuerlich selbst sieben mal deine Funktion fuer eine
# einzelne weisse Taste selbst aufrufen, aber wozu hast du dann
# die for-Schleife kennengelernt?

# Importiere zusaetzliche Bibliotheken
from mcpi.minecraft import Minecraft

# Stelle die Verbindung mit Minecraft her.
# Achte darauf, dass Minecraft gestartet ist und
# du dich in einer Welt bewegen kannst.
mc = Minecraft.create()

# Hier hast du ein Muster für eine Funktion, die dir eine weisse
#Taste erzeugt:
def white_key(x, y, z):
    mc.setBlocks(x, y - 1, z, x + 2, y - 1, z + 14, 44, 7)

# Nimm dir wieder deine Skizze zu Hilfe und ueberleg dir,
# welche Schritte nacheinander erforderlich sind um das Tastenfeld zu erzeugen?
for i in range(0, 19, 3):
    white_key(x + i, y, z)

# Kannst du daraus auch eine Funktion machen, die nur eine Position uebergeben bekommt?
def make_octave(x, y, z):
    for i in range(0, 19, 3):
        white_key(x + i, y, z)
