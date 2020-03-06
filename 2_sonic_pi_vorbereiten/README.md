Damit das Programm Sonic-Pi arbeitet, musst du das 
Programm in der Kategorie "Entwicklung" starten.
(Es dauert einen kleinen Moment bis das Logo verschwindet und
das Hauptfenster angezeigt wird.)
Anschließend kontrolliere ob die folgenden Zeilen
im Hauptfenster stehen:

live_loop :listen do
    use_real_time
    note = sync "/osc/play_this"
    play note[0]
end

Sollte das Hauptfenster etwas anderes enthalten,
ersetze bitte den Inhalt mit dem "live_loop".

Zuletzt klicke links oben auf den Knopf "Run" mit dem Play-Symbol.
Wenn du willst kannst du das Fenster minimieren mit einem 
Klick auf die Pfeilspitze nach unten, in der rechten oberen Ecke
des Fensters.
