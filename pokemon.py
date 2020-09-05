"""
Terminal Game
"""
import atexit
import json
import numpy as np
import sys
import time
from game_functions import *


def exit_handler():
    # exit handler so that user doesnt abruptly exit the game (we can add a function that saved user's progress here)
    print("My application is ending!")


atexit.register(exit_handler)


# -------------------------------------------------------


class Trainer:
    def __init__(self, name: str, pokemon: dict, location: str, money=1000):
        self.name = name
        self.money = money
        self.pokemon = pokemon
        self.location = location

    def current_location(self):
        return f"You are currently in {self.location}"

    def __str__(self):
        return f"Pkmn Trainer {self.name}'s Trainer Card'\nStats:\nPokemon: {self.pokemon}\nMoney: {self.money}"

    # def PokemonInventory(self): just commenting for a test

    # def CapturePokemon(self):
    # global capture
    # capture = True


class Pokemon:
    def __init__(self, name, types, moves, EVs, health="=" * 25, exp=0):
        self.name = name
        self.moves = moves
        self.attack = EVs["ATTACK"]
        self.defense = EVs["DEFENSE"]
        self.health = health
        self.types = types
        self.bars = 20  # Amount of health bars
        self.exp = exp

    def fight(self, Pokemon2):
        # This allow 2 pokemons fight each other
        # Print fight information
        self.Pokemon2 = Pokemon2
        print("-------POKEMON BATTLE-------")
        print(f"\n{self.name}")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL/", 3 * (1 + np.mean([self.attack, self.defense])))
        print("\nVS")
        print(f"\n{Pokemon2.name}")
        print("TYPE/", Pokemon2.types)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        print("LVL/", 3 * (1 + np.mean([Pokemon2.attack, Pokemon2.defense])))
        print("\nVS")

        time.sleep(2)

        # Consider type advantages
        version = ["Fire", "Water", "Grass"]
        for i, k in enumerate(version):
            if self.types == k:
                # Both are the same type
                if Pokemon2.types == k:
                    string_1_attack = "It's not very effective..."
                    string_2_attack = "It's not very effective..."
                # Pokemon2 is STRONG against pokemon1
                if Pokemon2.types == version[(i + 1) % 3]:
                    Pokemon.attack *= 2
                    Pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = "It's not very effective..."
                    string_2_attack = "It's super effective!"
                # Pokemon 2 is WEAK against Pokemon 1
                if Pokemon2.types == version[(i + 2) % 3]:
                    self.attack *= 2
                    self.defense *= 2
                    Pokemon2.attack /= 2
                    Pokemon2.defense /= 2
                    string_1_attack = "It's super effective!"
                    string_2_attack = "It's not very effective..."
        while (self.bars > 0) and (Pokemon2.bars > 0):
            # Print the health of each pokemon
            print(f"{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")

            print(f"Go {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            index = int(input("Pick a move: "))
            printf(f"{self.name} used {self.moves[index-1]}!")
            time.sleep(1)
            printf(string_1_attack)

            # Determine damage
            Pokemon2.bars -= self.attack
            Pokemon2.health = ""

            # Add back bars plus give a defense boost
            for j in range(int(Pokemon2.bars + 0.1 * Pokemon2.defense)):
                Pokemon2.health += "="
            time.sleep(1)
            print(f"{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(0.5)

            # Check if the pokemon has fainted
            if Pokemon2.bars <= 0:
                printf(f"\n... {Pokemon2.name} fainted")
                break
            # ----------------------------------If Pokemon2's hasn't fainted, then it's Pokemon2's turn-------------------------
            print(f"Go {Pokemon2.name}!")
            for i, x in enumerate(Pokemon2.moves):
                print("f{i+1}.", x)
            index = int(input("Pick a move: "))
            printf(f"{Pokemon2.name} used {moves[index-1]}!")
            time.sleep(1)
            printf(string_2_attack)

            # Determine damage
            self.bars -= Pokemon2.attack
            self.health = ""

            # Add back bars plus give a defense boost
            for j in range(int(self.bars + 0.1 * self.defense)):
                Pokemon2.health += "="
            time.sleep(1)
            print(f"{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(0.5)

            # Check if the pokemon has fainted
            if self.bars <= 0:
                printf("\n...", self.name + " fainted")
                break
        money = np.random.choice(5000)
        printf(f"Opponent paid you {money}.")


if __name__ == "__main__":
    # Create a pokemon
    Charizard = Pokemon(
        "Charizard",
        "Fire",
        ["Flamethrower", "Fly", "Blast Burn", "Fire Punch"],
        {"ATTACK": 12, "DEFENSE": 8},
    )
    Blastoise = Pokemon(
        "Blastoise",
        "Water",
        ["Water Gun", "Bubblebeam", "Hydro Pump", "Surf"],
        {"ATTACK": 10, "DEFENSE": 10},
    )
    Venusaur = Pokemon(
        "Venusaur",
        "Grass",
        ["Vine Wip", "Razor Leaf", "Earthquake", "Frenzy Plant"],
        {"ATTACK": 8, "DEFENSE": 12},
    )

    def PokemonState(self):
        print(
            "Your pokemon has: ",
            self.hp,
            "\nYour pokemon has: ",
            self.exp,
            "\nYour pokemon has: ",
            self.speed,
            "speed",
            "\nYour pokemon has: ",
            self.attack,
            "attack",
            "\nYour pokemon has: ",
            self.defense,
            "defense",
        )


# start the BATTLE!
# Charizard.fight(Venusaur)

# -----------------------------------------------------------------------------------------------------------

# ----------Story-----------
dialogue(
    {
        "???": "Hello there! Welcome to the world of Pokemon! My name is Oak!",
        "Prof.Oak": [
            "People call me the Pokemon Professor!",
            "This world is inhabited by creatures called Pokemon!",
            "For some people, Pokemon are pets. Others use them for fights. Myself...",
            "I study Pokemon as a profession.",
            "First, what is your name?",
        ],
    }
)

player = Trainer(confirm("Enter your name:\t"), 0, {}, "Pallet Town")
printf(f"Right! So your name is {player.name}!")
print()

dialogue(
    {
        "Prof.Oak": [
            "This is my grandson. He's been your rival since you were a baby.",
            "...Erm, what is his name again?",
        ]
    }
)

rival = Trainer(confirm("Enter your rival's name:\t"), 0, {}, player.location)
printf(f"That's right! I remember now! His name is {rival.name}!")
print()

dialogue(
    {
        "Prof.Oak": "Your very own POKEMON legend is about to unfold! A world of dreams and adventures with POKEMON awaits! Let's go!"
    }
)

print(
    """Scene: You are in your bedroom now. You go downstairs to find your mother watching a program on T.V.
Talk to her?
"""
)

event_choice(
    {
        "Yes": "Mother: Right. All boys leave home some day. It said so on TV.\nProf.Oak, next door, is looking for you.",
        "No": "You rude! Go talk to her anyway.\nMother: Right. All boys leave home some day. It said so on TV.\nProf.Oak, next door, is looking for you.",
    }
)

printf(
    """
You step outside the house and see explore your hometown.
You look at the boundless blue sky above you, while the sweet scent of oddish in the forests
reminds you of the amazing journey you're about to embark on!

'There's no place like Pallet Town', you say as you run towards Prof. Oak's Lab.

You arrive at the lab, and look around but Prof.Oak seems to be nowhere in sight.
Upon asking one of the aides, you find out that Prof.Oak has gone to run an errand.

What do you do?
"""
)

event_choice(
    {
        "Wait for Prof.Oak at the lab": [
            "You wait for long but Professor still hasn't returned,\nYou decide to venture into the town and find clues to where he might have gone.",
            "You see a young kid wearing shorts, Talk to him?",
            {
                "Yes": "You talk to the kid\nYoungster Jimmy: When you hear grass rustling, it's usually a pokemon.\nProf.Oak told us so in his orientation class.",
                "No": "You aimlessly roam around the town waiting for Prof.Oak to show up",
            },
        ],
        "Go out and explore the town": [
            "You start exploring the town and try to ask if anyone has seen where Prof. Oak has gone.",
            "You see a young kid wearing shorts, Talk to him?",
            {
                "Yes": "You talk to the kid\nYoungster Jimmy: When you hear grass rustling, it's usually a pokemon.\nProf.Oak told us so in his orientation class.",
                "No": "You aimlessly roam around the town waiting for Prof.Oak to show up",
            },
        ],
        f"Go to {player.name}'s house": [
            f"You enter {player.name}'s house.",
            {
                "Talk to mom?": "Mom: Prof. Oak is the authority on Pokemon, Many pokemon trainers hold him in high regard.\nYou then come out of your house and explore the town again.",
                "Go back to town": "You come out of your house and roam aimlessly hoping Prof. Oak would arrive soon.",
            },
        ],
    }
)


printf(
    "As you're waiting outside in the town, you hear rustling grass in distance. Do you check it out?\n"
)
event_choice(
    {
        "Yes": "You carefully tiptoe towards the grass so you don't scare the pokemon in grass",
        "No": "You decide to not pay attention to the rustling, but after a few minutes your curiosity gets the better of you\nYou carefully tiptoe towards the grass.",
    }
)

printf(
    f"""You see the silhouette of a mouse like pokemon feasting on berries.
'That's a pikachu!' you shout in excitment. The wild Pikachu notices you and prepares to attack.
You notice the electricity crackling near Pikachu's cheeks and suddenly you hear someone shout
"""
)

dialogue({"Prof.Oak": "Hey! Wait! Don't get closer!"})
printf(
    "Prof.Oak throws a pokeball at Pikachu... The pokeball shakes a few times before sparking slightly indicating Pikachu has been captured."
)

dialogue(
    {
        "Prof.Oak": [
            "Whew...",
            "A pokemon can appear anytime in tall grass. You need your own pokemon for your protection.",
            "I know!",
        ]
    }
)

printf(
    """
Prof.Oak asks you to come with him to his lab, to which you happilly agree.

==========================================================================================================

At Prof.Oak's Lab:
"""
)

dialogue(
    {
        rival.name: "Gramps! I'm fed up with waiting!",
        "Prof.Oak": [
            f"{rival.name}? Let me think... Oh, that's right, I told you to come!",
            "Just wait!",
            "",
            f"Here, {player.name}! There are 3 Pokemon here! Haha! They are inside the pokeballs."
            "When I was young, I was a serious Pokemon trainer."
            "In my old age I have only 3 left, but you can have one! Choose!",
        ],
        rival.name: "Hey! Gramps! What about me?",
        "Prof.Oak": f"Be patient! {rival.name}, you can have one too!",
    }
)
