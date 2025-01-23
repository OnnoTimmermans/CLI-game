import random

class NPC:
    def __init__(self, name, role, hint):
        self.name = name
        self.role = role
        self.hint = hint

    def introduce(self):
        print(f"{self.name}: Hallo, avonturier! Ik ben een {self.role} en ik ben hier om je te helpen.")

    def give_hint(self):
        print(f"{self.name}: Hier is een hint: {self.hint}")

class AdventureGame:
    def __init__(self):
        self.has_key = False
        self.secret_item = False
        self.final_key = False
        self.completed = False

    def start_game(self):
        print("Welkom bij het CLI Adventure Game!")
        print("Je avontuur begint nu...")
        self.intro_story()

    def intro_story(self):
        print("\nJe missie is om een verloren schat te vinden, diep verborgen in een mysterieuze tempel.")
        self.first_choice()

    def first_choice(self):
        print("\nJe staat voor een splitsing.")
        choice = input("Kies je pad: links (A) of rechts (B)? ").lower()
        if choice == "a":
            self.meet_npc()
        elif choice == "b":
            self.find_key()
        else:
            print("Ongeldige keuze. Probeer opnieuw.")
            self.first_choice()

    def meet_npc(self):
        npc = NPC(name="Wijze Gids", role="wijze gids", hint="De sleutel ligt verborgen in een verlaten huis.")
        npc.introduce()
        npc.give_hint()
        self.obstacle()

    def find_key(self):
        print("\nJe hebt een sleutel gevonden in een verlaten huis!")
        self.has_key = True
        self.obstacle()

    def obstacle(self):
        print("\nJe komt bij een gesloten deur.")
        if self.has_key:
            print("Je gebruikt de sleutel om de deur te openen.")
            self.find_secret_item()
        else:
            print("Je hebt geen sleutel. Zoek een andere weg.")
            self.battle()

    def find_secret_item(self):
        print("\nAchter de deur vind je een mysterieus object!")
        self.secret_item = True
        self.battle()

    def battle(self):
        print("\nEen vijand blokkeert je pad!")
        choice = input("Wat doe je? Vlucht (V) of Vecht (F)? ").lower()
        if choice == "v":
            print("Je vlucht terug naar de deur.")
            self.obstacle()
        elif choice == "f":
            if random.choice([True, False]):
                print("Je hebt de vijand verslagen!")
                self.puzzle()
            else:
                print("Je bent verslagen! Probeer opnieuw.")
                self.obstacle()
        else:
            print("Ongeldige keuze. Probeer opnieuw.")
            self.battle()

    def puzzle(self):
        print("\nJe moet een raadsel oplossen om verder te gaan.")
        answer = input("Wat heeft vier benen in de ochtend, twee in de middag, en drie in de avond? ").lower()
        if answer == "mens":
            print("Het raadsel is opgelost!")
            self.find_map()
        else:
            print("Dat is niet correct. Probeer opnieuw.")
            self.puzzle()

    def find_map(self):
        print("\nJe hebt een schatkaart gevonden!")
        self.path_split()

    def path_split(self):
        print("\nDe kaart toont twee routes: de bergtop of het donkere bos.")
        choice = input("Kies je pad: Bergtop (B) of Donker Bos (D)? ").lower()
        if choice == "b":
            self.mountain_path()
        elif choice == "d":
            self.forest_path()
        else:
            print("Ongeldige keuze. Probeer opnieuw.")
            self.path_split()

    def mountain_path(self):
        print("\nOp de bergtop ontmoet je een wijze man.")
        print("Hij geeft je een cryptisch advies over de locatie van de schat.")
        self.final_challenge()

    def forest_path(self):
        print("\nIn het donkere bos vecht je tegen een krachtige vijand.")
        if random.choice([True, False]):
            print("Je hebt de vijand verslagen en de laatste sleutel gevonden!")
            self.final_key = True
        else:
            print("Je bent verslagen! Probeer opnieuw.")
            self.path_split()
        self.final_challenge()

    def final_challenge(self):
        print("\nJe bereikt de schatkamer.")
        if self.final_key or self.secret_item:
            print("Met je ontdekkingen open je de schatkamer!")
            print("Gefeliciteerd! Je hebt het spel gewonnen!")
            self.completed = True
        else:
            print("Je mist iets belangrijks om de schatkamer te openen.")
            self.path_split()

# Start het spel
game = AdventureGame()
game.start_game()