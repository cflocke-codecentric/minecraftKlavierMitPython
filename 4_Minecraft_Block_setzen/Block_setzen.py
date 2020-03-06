# Importiere zusaetzliche Bibliotheken
from mcpi.minecraft import Minecraft

# Stelle die Verbindung mit Minecraft her.
# Achte darauf, dass Minecraft gestartet ist und
# du dich in einer Welt bewegen kannst.
mc = Minecraft.create()

# Ueber Python mit mc.setBlock hast du die Moeglichkeit
# einen Block an einer bestimmten Position zu setzen.
# Der Funktion musst du einmal die Position (x-Koordinate, y-Koordinate und z-Koordinate) und
# die Art des Blocks mitgeben. Die Zahl 0 steht fuer einen Luft-Block, die Zahl 1 steht fuer Stein.
# Proiere es einfach aus!
mc.setBlock(1,1,1,1)

# Denk dran, sobald du die Datei einmal ausgefuehrt hast, kannst du
# den Befehl auch direkt in die Konsole eintippen!
# Kannst du hiermit ein L- oder ein O-Form erstellen?
