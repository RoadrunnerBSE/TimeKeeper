from tkinter import *
import time
from dataclasses import dataclass

# Globale Variabeln
laengstername = 0
starterfeld = {}            # Dict mit Startnummern als Keys und Teilnehmern als Objekte als Values
START_ZEIT = 0.0
START_INTERVALL = 0         # Nach 5 Sek. startet der nächste Läufer (nach Startnummer)
label_liste = {}            # Dict mit Startnummern als Keys
knopf_liste = {}            # Dict mit Startnummern als Keys
anzahl_teilnehmer_auf_der_strecke = 0
stop_liste = []             # Liste mit den Startnummern, die gemeinsam gestoppt werden sollen
zaehler_gruppeneinlauf = 1


@dataclass
class Teilnehmer:
    name: str
    vorname: str
    alter: int
    startnummer: int
    geschlecht: str
    startzeit: float = 0
    zielzeit: float  = 0
    platzierung: int = 999
    zeitdiff: float  = 0            # Wenn am kleinsten, dann auch beste Platzierung
    zeitformatiert: str = "00:00:00.0"
    im_ziel: bool = False
    gruppen_einlauf: int = 0        # laufende Nummer für das Stoppen per Gruppe


# Funktion zum Importieren aus CSV-Datei --> die Datei muss UTF-8 Codiert sein!
def import_data(dateiname):
    global laengstername
    global anzahl_teilnehmer_auf_der_strecke
    starterfeld = {}
    with open(dateiname, "r") as datei:
        for i, zeile in enumerate(datei):
            if i > 0:
                teilnehmer = Teilnehmer(zeile.strip().split(";")[0],       # Name
                                        zeile.strip().split(";")[1],       # Vorname
                                        int(zeile.strip().split(";")[2]),  # Alter
                                        int(zeile.strip().split(";")[3]),  # Startnummer
                                        zeile.strip().split(";")[4])       # Geschlecht
                starterfeld[teilnehmer.startnummer] = teilnehmer           # Dict mit Startnummer als Key
                if laengstername < len(teilnehmer.name) + len(teilnehmer.vorname) + 2:
                    laengstername = len(teilnehmer.name) + len(teilnehmer.vorname) + 2
        datei.close()
    anzahl_teilnehmer_auf_der_strecke = len(starterfeld)
    return starterfeld


# Erfassen der Startzeit für alle Läufer
def start():
    global starterfeld
    global START_ZEIT
    global START_INTERVALL
    START_INTERVALL = int(e_intervall.get())
    b_start["state"] = "disabled"
    e_intervall["state"] = "disabled"
    START_ZEIT = time.time()
    time_display()
    for i, teilnehmer in enumerate(starterfeld.values()):
        teilnehmer.startzeit = START_ZEIT + (START_INTERVALL * i)
    e_mehrfach_stoppen.delete(0, END)
    e_mehrfach_stoppen.focus()


# Funktion zum Stoppen der einzelnen Zeiten der Läufer
def stop(id):
    global starterfeld
    global START_INTERVALL
    global anzahl_teilnehmer_auf_der_strecke
    anzahl_teilnehmer_auf_der_strecke -= 1
    # welcher Knopf mit Index i aus knopf_liste wurde gedrückt?
    i = id
    starterfeld.get(i).zielzeit = time.time()
    starterfeld.get(i).zeitdiff = starterfeld.get(i).zielzeit - starterfeld.get(i).startzeit
    starterfeld.get(i).zeitformatiert = convert_time(starterfeld.get(i).zeitdiff)
    starterfeld.get(i).im_ziel = True
    sort_plazierung()
    export_data(convert_time(time.time() - START_ZEIT, True))


# Mehrfaches Stoppen von Teilnehmern -> aus Liste im Eingabefeld "Startnummern"
def mehrfach_stoppen(*args):
    global stop_liste
    global starterfeld
    global anzahl_teilnehmer_auf_der_strecke
    global zaehler_gruppeneinlauf
    stop_liste = e_mehrfach_stoppen.get().split()
    stop_liste_unique = set()
    for nummer in stop_liste:
        stop_liste_unique.add(nummer)       # Dubletten entfernen, damit die anzahl_teilnehmer_auf_der_strecke stimmt
    for startnummer in stop_liste_unique:
        if int(startnummer) in starterfeld.keys() and starterfeld.get(int(startnummer)).im_ziel == False:
            starterfeld.get(int(startnummer)).zielzeit = time.time()
            starterfeld.get(int(startnummer)).zeitdiff = starterfeld.get(int(startnummer)).zielzeit - starterfeld.get(int(startnummer)).startzeit
            starterfeld.get(int(startnummer)).zeitformatiert = convert_time(starterfeld.get(int(startnummer)).zeitdiff)
            starterfeld.get(int(startnummer)).im_ziel = True
            anzahl_teilnehmer_auf_der_strecke -= 1
            if len(stop_liste_unique) > 1:
                starterfeld.get(int(startnummer)).gruppen_einlauf = zaehler_gruppeneinlauf
    if len(stop_liste_unique) > 1:
        zaehler_gruppeneinlauf += 1
    e_mehrfach_stoppen.delete(0, END)
    e_mehrfach_stoppen.focus()
    sort_plazierung()
    export_data(convert_time(time.time() - START_ZEIT, True))


# Funktion um die laufende Zeit anzuzeigen
def time_display():
    global START_ZEIT
    global anzahl_teilnehmer_auf_der_strecke
    l_ges_zeit["text"] = convert_time(time.time() - START_ZEIT)
    tabelle()
    if anzahl_teilnehmer_auf_der_strecke > 0:
        root.after(200, time_display)


# Funktion für die die Anzeige von: Platzierung   Start-Nr.   Name, Vorname    Zeit
def tabelle(erstaufruf = False):
    global starterfeld
    i = 0
    for startnummer, teilnehmer in sorted(starterfeld.items(), reverse=False, key=lambda item: item[1].platzierung):
        label_liste.get(startnummer).grid(row=i, column=0)
        knopf_liste.get(startnummer).grid(row=i, column=1)
        ges_name = teilnehmer.name + ", " + teilnehmer.vorname
        if teilnehmer.im_ziel:
            zeile = f"{teilnehmer.platzierung:03}   {teilnehmer.startnummer:03}      {ges_name:<{laengstername}} {teilnehmer.zeitformatiert:>9}"
            label_liste.get(startnummer)["text"] = zeile
            knopf_liste.get(startnummer)["state"] = "disabled"
            i += 1
            continue
        if erstaufruf:
            zeile = f"{teilnehmer.platzierung:03}   {teilnehmer.startnummer:03}      {ges_name:<{laengstername}} {teilnehmer.zeitformatiert:>9}"
            label_liste.get(startnummer)["text"] = zeile
        else:
            teilnehmer.zielzeit = time.time()
            teilnehmer.zeitdiff = teilnehmer.zielzeit - teilnehmer.startzeit
            teilnehmer.zeitformatiert = convert_time(teilnehmer.zeitdiff)
            zeile = f"{teilnehmer.platzierung:03}   {teilnehmer.startnummer:03}      {ges_name:<{laengstername}} {teilnehmer.zeitformatiert:>9}"
            label_liste.get(startnummer)["text"] = zeile
        i += 1


# Funktion um die Zeitdiff in hh:mm:ss,000 umzurechnen.
def convert_time(sekunden, als_dateiname = False):
    if sekunden < 0:
        sekunden = sekunden * (-1)
        std = int(sekunden // (60 * 60))
        min = int((sekunden - (std * 60 * 60)) // 60)
        sek = int(((sekunden - (std * 60 * 60) - (min * 60))))
        formatiert = f"-{std:02}:{min:02}:{sek:02}"
        return formatiert
    else:
        std = int(sekunden // (60 * 60))
        min = int((sekunden - (std * 60 * 60)) // 60)
        sek = round(((sekunden - (std * 60 * 60) - (min * 60))), 1)
        if als_dateiname:
            formatiert = f"{std:02}_{min:02}_{sek:02.0f}_export.csv"
        else:
            formatiert = f"{std:02}:{min:02}:{sek:04.1f}"
        return formatiert


# Funktion zum Sortieren nach Zielzeit und update der Plazierung
def sort_plazierung():
    global starterfeld
    i = 1
    # starterfeld = sorted(starterfeld, key=lambda Teilnehmer: Teilnehmer.platzierung)
    for startnummer, teilnehmer in sorted(starterfeld.items(), reverse=False, key=lambda item: item[1].zeitdiff):
        if teilnehmer.im_ziel:
            teilnehmer.platzierung = i
            i += 1


# Funktion zum Schreiben in eine Datei
def export_data(dateiname = "export.csv"):
    global starterfeld
    with open(dateiname, "w") as datei:
        datei.write("Platzierung;Name;Vorname;Startnummer;Ergebniszeit;Gruppeneinlauf\n")
        for startnummer, teilnehmer in sorted(starterfeld.items(), reverse=False, key=lambda item: item[1].platzierung):
            datei.write(f"{teilnehmer.platzierung};{teilnehmer.name};{teilnehmer.vorname};"
                        f"{teilnehmer.startnummer};{teilnehmer.zeitformatiert};{teilnehmer.gruppen_einlauf}\n")
        datei.close()


# Importieren von Teilnehmern in eine Liste
starterfeld = import_data("teilnehmer.csv")

# Hauptfenster
root = Tk()
root.title("Zeitmessung by UI")
root.geometry("700x800")

# Frame: frame_obere_zeile mit Labels und Buttons
frame_obere_zeile = Frame(root)
b_start = Button(frame_obere_zeile, font="Arial 20", text="   Start   ", command=start)
l_ges_zeit = Label(frame_obere_zeile, font="Arial 80", fg="red", text="00:00:00.0")
b_export = Button(frame_obere_zeile, font="Arial 20", text="  Export  ", command=export_data)
e_intervall = Entry(frame_obere_zeile, font="Arial 20", width=3)
e_intervall.insert(1, "10")
e_mehrfach_stoppen = Entry(frame_obere_zeile, font="Arial 20", width=30)
e_mehrfach_stoppen.bind("<Return>", mehrfach_stoppen)
l_intervall = Label(frame_obere_zeile, font="Arial 20", text="Startintervall:")
l_mehrfach_stoppen = Label(frame_obere_zeile, text="Startnummern:", font="Arial 20")
b_mehrfach_stoppen = Button(frame_obere_zeile, font="Arial 20", text="   Stop   ", command=mehrfach_stoppen)
# Positionierung der Labels/Buttons im Frame
b_start.grid(row=0, column=0)
l_ges_zeit.grid(row=0, column=1)
b_export.grid(row=0, column=2)
l_intervall.grid(row=1, column=0)
e_intervall.grid(row=1, column=1, sticky=W)
l_mehrfach_stoppen.grid(row=2, column=0, sticky=W)
e_mehrfach_stoppen.grid(row=2, column=1, sticky=W)
b_mehrfach_stoppen.grid(row=2, column=2)
frame_obere_zeile.grid(row=0, column=0, sticky=W)

# Frame: frame_tab_ueberschrift mit Labels und Buttons
frame_tab_ueberschrift = Frame(root)
l_tab_ueberschrift = Label(frame_tab_ueberschrift, text="Platz   Start-Nr.   Name                                     Zeit", font="Arial 20")
# Positionierung der Labels/Buttons im Frame
l_tab_ueberschrift.grid(row=1, column=0)
frame_tab_ueberschrift.grid(row=1, column=0, sticky=W)

# Frame: frame_tab mit Labels und Buttons
frame_tab = Frame(root)
leinwand = Canvas(frame_tab, width=600, height=600)
scrollbar = Scrollbar(frame_tab, orient="vertical", command=leinwand.yview)
scrollable_frame = Frame(leinwand)
scrollable_frame.bind("<Configure>", lambda e: leinwand.configure(scrollregion=leinwand.bbox("all")))
leinwand.create_window((0, 0), window=scrollable_frame, anchor="nw")
leinwand.configure(yscrollcommand=scrollbar.set)
# Positionierung der Labels/Buttons im Frame
frame_tab.grid(row=2, column=0, columnspan=3, sticky=W)
leinwand.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Code
for startnummer in starterfeld.keys():
    label_liste[startnummer] = Label(scrollable_frame, font="Courier 16")
    knopf_liste[startnummer] = Button(scrollable_frame, font="Courier 16", text=" Stop ", command=lambda c=startnummer: stop(c))
tabelle(True)

root.mainloop()
