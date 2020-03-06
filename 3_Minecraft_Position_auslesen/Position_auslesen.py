# Importiere zusaetzliche Bibliotheken
from mcpi.minecraft import Minecraft

# Stelle die Verbindung mit Minecraft her.
# Achte darauf, dass Minecraft gestartet ist und
# du dich in einer Welt bewegen kannst.
mc = Minecraft.create()

# Lese die Spielerposition in Minecraft aus.
player_x, player_y, player_z  = mc.player.getTilePos()
# Du kannst den Befehl auch direkt in die Konsole einfuegen.
# Was kommt dabei heraus? Du kannst auch die Variablen player_x usw. mit print ausgeben!
# Vergleiche die Ausgabe mit den Zahlen oben links im Spielefenster! Was ist der Unterschied?
