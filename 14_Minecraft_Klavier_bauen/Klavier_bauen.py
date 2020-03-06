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


# Die Funktion zum freiraeumen eines ganzen Bereichs um eine
# Position herum


# Fuege hier bitte deine Funktion zur Erstellung einer schwarzen Taste ein:


# Fuege hier bitte deine Funktion zur Erstellung einer weissen Taste ein:


# Zuletzt definiere die Funktion zur Erstellung der ganzen Oktave
# Die Funktion soll eine bestimmte Position uebergeben bekommen


# Jetzt wollen wir die Funktionen einsetzen fuer folgende Aufgabe:
# 1. Schaffe Platz in der Minecraft-Welt
# 2. Erstelle die Oktave
# 3. Setze den Spieler auf die Oktave --> ist mit mc.player.setPos(..) schon geloest.


#Hilfsmittel um den Spieler auf die Oktave zu setzen:
mc.player.setPos(player_x + 8, player_y + 3, player_z + 12)
