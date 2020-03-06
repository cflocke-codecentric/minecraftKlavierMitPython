# In Python haben wir bisher die Befehle
print("eine Zeichenkette")
# und
str(42) # wandelt eine Zahl in eine Zeichenkette um
# kennengelernt.
# Hier ein Beispiel um eine längere Begruessung ueber print auf die Konsole
# auszugeben
print("Hallo Zusammen,")
print("Was fuer interessante Sachen")
print("wir mit Python machen können!")

# In dem Beispiel haben wir drei Mal hintereinander
# den print-Befehl aufgerufen. Stell dir jetzt vor
# du willst diese Begruessung sechs Mal hintereinander
# auf der Konsole sehen.
# Wir müssten also 18 Mal hintereinander den print-Befehl nutzen.
# Gluecklicherweise stellt Pyhton uns die Möglichkeit zur Verfuegung
# eigene Befehle/Funktionen zu definieren.
# Damit können wir die Begruessung oben, zusammenfassen.

# Eine Funktion kann ich mit dem Schluesselwort def schreiben, z.B.:
def einFunktionsname():
    print("Test")

# Du siehst nach dem Schluesselwort def kannst du dir einen Funktionsnamen ausdenken.
# Nach diesem Funktionsnamen musst du eine oeffnende und eine schliessende, runde Klammer
# schreiben. Zuletzt einen Doppelpunkt.

# def sitzeEinfachHerum():

# Dieses ist der erste Teil, die Funktionsdefinition. Nun folgt der
# Teil in dem wir der Funktion mitteilen, was sie ausfuehren soll.
# WICHTIG ist dabei, dass alle folgenden Anweisungen eingerueckt sind.
# Zum Beispiel:
def langeGrussFormel():
    print("Hallo Zusammen,")
    print("Was fuer interessante Sachen")
    print("wir mit Python machen können!")

# Achte darauf, dass alle Anweisungen unter der Funktionsdefinition
# alle eingerückt sind! Nur dadurch weiss Python, dass diese
# Anweisungen zu der Funktionsdefinition gehoeren.

# Aufrufen kannst du deine Funktion ueber den Namen gefolgt von
# den beiden runden Klammern:
langeGrussFormel()

# Ruf deine Funktion nun mehrmals hintereinander auf!
