from mods.sqlhandler import SQLHandler
from mods.hasher import Hasher
from os import system
from time import sleep

handler = SQLHandler("db.db")
hasher = Hasher(2)

class App:
    def __init__(self):
        self.author = "harimtim"
        self.date = "07.07.2025"
        self.github = "https://github.com/harimtim/PassManager"
        self.banner = f"""PassManager - {self.author}

[1] Speicher neues Passwort
[2] Zeige alle Passwörter
[3] Datenbank zurücksetzen
        
Auswahl: """
        
    def cls(self):
        system("clear")

    def main(self):
        while True:
            self.cls()
            auswahl = int(input(self.banner))
            print("-"*25)
            if auswahl == 1:
                handler.add(input("\n[*] Account: "), hasher.hash_password(input("[*] Passwort: ")))
                sleep(.5)
                print("[*] Passwort wurde verschlüsselt gespeichert!")
                sleep(1.5)
            if auswahl == 2:
                sleep(1)
                all = handler.showall()
                if len(all) <= 0:
                    print("\n[*] Die Datenbank ist leider leer!")
                else:
                    for tup in all:
                        print(f"\n[*] Eintrag: {tup[0]}\n-----\n[*] Account: {tup[1]}\n[*] Password: {hasher.unhash(tup[2])}\n")
                sleep(1)
                input("\n[*] Drücke etwas um ins Menü zu kommen...")
                sleep(.5)
            if auswahl == 3:
                sleep(1)
                print("\n[*] Datenbank wird zurückgesetzt...")
                sleep(2)
                handler.reset()
                print("[*] Datenbank erfolgreich zurückgesetzt!")
                sleep(2)

app = App()
app.main()