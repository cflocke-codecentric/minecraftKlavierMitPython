# In den vorherigen Beispielen haben wir schon ermittelt,
# wie die Spielerposition in Minecraft ausgelesen werden kann.
# Zusammen mit dem Wissen, wie man einen ganzen Blockbereich setzen
# kann, wollen wir uns nun ein wenig Platz schaffen, wo
# unser Klavier entstehen kann

# Importiere zusaetzliche Bibliotheken
from mcpi.minecraft import Minecraft

# Stelle die Verbindung mit Minecraft her.
# Achte darauf, dass Minecraft gestartet ist und
# du dich in einer Welt bewegen kannst.
mc = Minecraft.create()

# Liess dir die aktuellen Koordinaten des Spielers aus,
# nutze dazu die Variable mc:


# Sieh dir nun Folie 17 nochmal genauer an. Hier wird nochmal beschrieben, wie man einen Punkt,
# abhaengig von einer bestimmten Position beschreiben kann.
# Nutze jetzt den setBlocks-Befehl um einen Bereich um den Spieler mit Luftbloecken zu füllen.
# Luftbloecke haben die ID 0. Nutze den setBlocks-Befehl mit der Variablen mc und denk dran, dass
# du zwei Positionen in einem 3 dimensionalem Raum angeben musst:

