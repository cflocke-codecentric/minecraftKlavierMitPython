# Python bietet die Moeglichkeit eine Menge von Informationen,
# als eine Liste darzustellen.
# Wie eine Einkaufsliste koennen wir eine solche Menge
# an Daten in Python darstellen.
# Listen in Python werden mit eckigen Klammern erstellt. z.B.:
[2,5,3,6,7] # eine Liste mit Zahlen
["Ein","Koch","traegt","normalerweise","eine","Kochmuetze"] # eine Liste mit einzelnen Worten

# Eine Liste kann ebenfalls in einer Variablen gespeichert werden:
meineListe = [] # eine leere Liste
zahlenListe = [3,5,7,9] # Eine Variable mit einer Zahlen-Liste
gemischteListe = [3, "fuenf","eine",6,8] # Eine Variable mit Zahlen und Zeichenketten in einer Liste

# Haeufig wird bei der Programmierung ein einzelner Wert aus einer solchen Liste benoetigt.
# Der Zugriff erfolgt ueber die Angabe der Stelle, an welcher sich der gesuchte Wert
# In der Liste befindet.
# Gehen wir von der gemischteListe-Variable aus, befindet sich das Wort "eine" an der dritten Stelle.
# Jedoch ist es in den meisten Programmiersprachen ueblich, dass eine Zaehlung nicht bei 1 beginnt,
# sondern bei 0. Ebenso in Python.
# Der Zugriff auf ein Element in der Liste erfolgt ueber den Variablennamen gefolgt von eckigen Klammern.
gemischteListe[2] # Gibt das dritte Element der Liste zurueck.
print(gemischteListe[1]) # Gibt "fuenf" auf der Konsole aus.

# Oft ist es hilfreich zu ermitteln wie viele Elemente
# in einer Liste vorhanden sind. Hierzu kann die len()-Funktion aus Python
# verwendet werden.
len(zahlenListe)
