# Importiere die notwendigen Bibliotheken, damit wir
# loslegen koennen.
from pythonosc import udp_client
from time import sleep
from mcpi.minecraft import Minecraft
# Das hier ist nochmal notwendig um alle Verbindungen zu den
# anderen beiden Programmen herzustellen.
sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)
mc = Minecraft.create()

# Hier merken wir uns die Nummern, der Toene fuer die einezelnen
# Tasten. In der unteren Liste steht eine 0 an der dritten Stelle,
# da wir nur 5 schwarze Tasten fuer eine Oktave benoetigen
white_notes = [60, 62, 64, 65, 67, 69, 71]
black_notes = [61, 63, 0,  66, 68, 70]

#Funktion um eine Note abzuspielen gib einen Ton zu spielen
def play_note(note):
    '''Take an integer note value and send it to Sonic Pi'''
    sender.send_message('/play_this', note)
    sleep(0.5)

# Hier muss die Player-Position ausgelesen werden und in
# drei Variablen gespeichert werden fuer die drei Koordinaten-Achsen X,Y,Z
player_x, player_y, player_z  = mc.player.getTilePos()

# Die Funktion zum freiraeumen eines ganzen Bereichs um eine
# Position herum
def bulldozer(x, y, z):
    mc.setBlocks(x - 30, y - 3, z - 30, x + 30, y + 20, z + 30, 0)

# Fuege hier bitte deine Funktion zur Erstellung einer schwarzen Taste ein:
def black_key(x, y, z):
    mc.setBlocks(x, y - 1, z, x + 1, y - 1, z + 8, 49)

# Fuege hier bitte deine Funktion zur Erstellung einer weissen Taste ein:
def white_key(x, y, z):
    mc.setBlocks(x, y - 1, z, x + 2, y - 1, z + 14, 44, 7)

# Zuletzt definiere die Funktion zur Erstellung der ganzen Oktave
# Die Funktion soll eine bestimmte Position uebergeben bekommen
def make_octave(x, y, z):
    for i in range(0, 19, 3):
        white_key(player_x + i, player_y, player_z)
    for i in range(2, 18, 3):
        if i != 8:	## Lasse einen Platz an der 8 Position, einer schwarzen Taste
            black_key(player_x + i, player_y, player_z)

# Jetzt wollen wir die Funktionen einsetzen fuer folgende Aufgabe:
# 1. Schaffe Platz in der Minecraft-Welt
# 2. Erstelle die Oktave
# 3. Setze den Spieler auf die Oktave
bulldozer(player_x, player_y, player_z)
make_octave(player_x, player_y, player_z)

#Hilfsmittel um den Spieler auf die Oktave zu setzen:
mc.player.setPos(player_x + 8, player_y + 3, player_z + 12)

# Bis hierher haben wir die Welt erstellt, sodass wir jetzt
# bereit sind, staendig zu ermitteln ob der Spieler
# auf einer Taste steht und dann den passenden Ton zu spielen.
while True:
    # Lese die aktuelle Spielerposition aus

    # Ermittle den Block UNTERHALB des Spielers



    # Ermittle die relative Position auf dem Klavier indem du die urspruengliche
    # X-Position von der aktuellen X-Position subtrahierst:


    # Jetzt musst du nur noch zwischen weissen und schwarzen Tasten
    # differenzieren, was fuer einen Ton du spielen musst!
    # Fange einfach an und nimm erstmal zwei unterschiedliche Toene.
    # Spiele einen Ton wenn es sich um eine weisse Taste handelt

    # Spiele einen Ton wenn es sich um eine schwarze Taste handelt

