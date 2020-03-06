# Importiere zusaetzliche Bibliotheken
from mcpi.minecraft import Minecraft

# Stelle die Verbindung mit Minecraft her.
# Achte darauf, dass Minecraft gestartet ist und
# du dich in einer Welt bewegen kannst.
mc = Minecraft.create()

# Damit wir zum Erstellen des Pianos genug Platz haben,
# wollen wir zunächst einen ganzen Bereich an Bloecken
# frei raeumen.
# Hierzu koennen wir den Befehl mc.setBlocks() nutzen.
# Diesem Befehl müssen wir zwei Positionen nennen in welchem Bereich
# Blöcke gesetzt werden sollen.
# Eine Position besteht immer aus den Koordinaten der X-, der Y- und der Z-Achse.
# x = Links oder Rechts auf der X-Achse
# y = Höhe oder Tiefe auf der Y-Achse
# z = Nach hinten oder vorne auf der Z-Achse
# Dh. ihr gebt dem Befehl sechs Zahlenwerte für die Positionen und ein Zahlenwert für die Blockart.
mc.setBlocks(0,6,0,6,2,6,0)

# Verändere die Werte und schau dir im Spiel die Auswirkungen an!
# Was ist einzugeben, wenn du einen großen freien Platz schaffen möchtest?

