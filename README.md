# TimeKeeper
## Problemstellung und Motivation
Für Breitensportaktivitäten wie z.B. Laufwettkämpfe oder Triathlon wird immer ein Zeitmesssystem benötigt. In den meisten Fällen sind das viele freiwillige Helfer mit Stoppuhren.
Professionelle Zeitmesssysteme mit RFI-Chip oder Lichtschranken sind sehr teuer und für kleine Vereine nicht bezahlbar.
Freiwillige Helfer bei solchen Sportveranstaltungen sind meistens auch eher rar gesät. Daher gibt es die Überlegung ein Programm zu schreiben, welches das Zeitnehmen einfach und mit nur mit ein bis zwei Personen durchführbar macht - TimeKeeper.

## Verbesserungen immer gewünscht
Vielleicht findet sich die ein oder andere Programmiererin oder Programmierer, der Lust hat das kleine Projekt zu unterstützen.
Ich selbst bin nur Laie und „einfach nur“ Enthusiast was das Programmieren angeht.
Daher mag dem einen oder anderen der Code sehr nach Spaghetti aussehen – ich kann es aber leider (noch) nicht besser.

## Programmbeschreibung
TimeKeeper ist ein in Python (mit Tkinter) geschriebenes Programm, welches eine Starterliste aus einer csv-Datei einließt und die Start- und Zielzeit erfasst.
Dabei kann jeder Teilnehmer einzeln gestoppt werden, oder aber in Blöcken über Eingabe der Startnummern im ansprechenden Eingabefeld.
Gestartet wird in einstellbaren Zeitabständen nach Startnummer.
Nach jedem Erfassen wird eine Sicherungsdatei in Form einer csv-Datei auf die Festplatte geschrieben. Nach der kompletten Zeiterfassung aller Teilnehmer kann die finale csv-Datei exportiert werden und mit jedem beliebigen Tabellenprogramm weiterverarbeitet werden.
Während der Zeitmessung sortiert TimeKeeper nach jedem Stop-Vorgang die Teilnehmer nach den Bestzeiten.

## Specs
* Einfache Bedienung
* Zeitnahme mit nur 1 oder 2 Personen
* Auswertung der Ergebnisse
* Exportfunktion der Ergebnisse (csv, xls, usw.)
* Urkundenerzeugung
* Zwischenzeiten (Runden, Triathlon, usw.)

