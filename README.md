# TimeKeeper
## Problem and motivation
For popular sports activities such as running competitions or triathlon always require a timing system. In most cases, there are many volunteers with stopwatches. Professional timing systems with an RFI chip or light barriers are very expensive and not affordable for small clubs. Voluntary helpers at such sporting events are usually few and far between. Therefore, there is the consideration of writing a program that makes time-keeping simple and feasible with only one or two people - TimeKeeper.

## Improvements always wanted
Maybe you will find a programmer or two who wants to support the small project. I am just a layman and “just” a programming enthusiast. So the code may look a lot like spaghetti to some people - but unfortunately I can't do it better (yet).

## Program description
TimeKeeper is a program written in Python (with Tkinter), which includes a starter list from a csv file and records the start and finish time. Each participant can be stopped individually, or in blocks by entering the start numbers in the input field. The race starts at adjustable intervals according to the start number. After each acquisition, a backup file in the form of a csv file is written to the hard disk. After the complete time recording of all participants, the final csv file can be exported and further processed with any table program. During the time measurement, TimeKeeper sorts the participants according to the best times after each stop.

## Specs
* easy handling
* timekeeping with only 1 or 2 people
* evaluation of results
* export function of the results (csv, xls, etc.)
* creation of certificates
* split times (laps, triathlon, etc.)

_______________________________________________________________________


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

