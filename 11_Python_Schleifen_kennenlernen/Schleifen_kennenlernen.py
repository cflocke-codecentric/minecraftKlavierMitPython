# Schleifen in Python sind dazu da um Anweisungen beliebig oft zu wiederholen.
# Eine Art von Schleife ist die For-Schleife. Definiert wird eine for-Schleife
# ueber das Schluesselwort for in Kombination mit in.
# Also komplett for ... in ...:
# In der ersten Luecke definieren wir einen Platzhalter und
# in der zweiten Luecke eine Menge, die durchgegangen werden soll. z.B.:
zahlenListe = [0,1,2,3,4,5,6,7,8,9]

# Um diese Liste Element fuer Element durchzugehen schreibt man:
for platzhalter in zahlenListe:
    print(platzhalter)

# Achte wieder auf die Doppelpunkte am Ende, sowie die eingerückten Anweisungen,
# die in der For-Schleife enthalten sein sollen.
# Eine begraeuchliche Bezeichnung fuer die Variable des Platzhalters,
# wird auch haeufig der Buchstabe i verwendet.
# Fuehre die For-Schleife einfach mal aus! Wie sieht die Ausgabe aus?

# Zusaetzlich gibt es die Hilfsfunktion range() in Python. Damit ist es moeglich
# simpel eine Liste zu erstellen, die durchlaufen werden kann.
for i in range(0,9):
    print(i)

# Wie sieht hier die Ausgabe aus? Veraendere die Grenzen dh. die 0 und die 9, was passiert dann?

# Die range-Funktion kann auch mit einer dritten Variablen aufgerufen werden, die die "Schritt-Weite"
# angibt. range(von, bis, schrittweite)
for i in range(0,9,3):
    print(i)
# Veraendere auch hier die Zahlen und sieh dir das Ausgabe-Ergebnis an.

