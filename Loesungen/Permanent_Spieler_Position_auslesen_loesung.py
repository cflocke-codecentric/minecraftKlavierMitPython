# Importiere die notwendigen Bibliotheken, damit wir
# loslegen koennen.
from mcpi.minecraft import Minecraft

# Stelle die Verbindung mit Minecraft her.
# Achte darauf, dass Minecraft gestartet ist und
# du dich in einer Welt bewegen kannst.
mc = Minecraft.create()

# Lese die Spielerposition in Minecraft aus.
# player_x, player_y, player_z  = mc.player.getTilePos()

# Eine while-Schleife laueft so lange bis die Bedigung
# nach dem while-Schluesselwort falsch wird/ist.
# Die folgenden Anweisungen, die zur Schleife dazu gehoeren sollen,
# muessen wieder eingerueckt darunter geschrieben werden.
while True:
    # Positon auslesen
    player_x, player_y, player_z  = mc.player.getTilePos()
    # Position ausgeben
    print(player_x + " " + player_y + " " + player_z)
    
