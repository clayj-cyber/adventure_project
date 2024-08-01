import random

#have to clean up combat but should run OK. Some things need work. Levels will be higher
#combat will be more logic-based in the end product

class Dungeon:
    def __init__(self):
        print("==WELCOME TO THE DUNGEON==")
        self.player = {
            'name': 'Hero',
            'hp': 100,
            'attack': 10,
            'block': 5,
            'magic': 15,
            'weapon': 10,
            'magic_points': 20,
            'burn_duration': 0,
            'burn_damage': 0,
            'score': 0,
            'stamina': 50,
            'fireball_damage': 15,
            'excalir_damage': None,
            'water_nebula': False,
            'ice_magic': False
        }
        self.monsters = [
            {'name': 'Goblin', 'hp': 30, 'attack': 5, 'block': 2, 'burn_duration': 0, 'burn_damage': 0},
            {'name': 'Orc', 'hp': 50, 'attack': 7, 'block': 3, 'burn_duration': 0, 'burn_damage': 0},
            {'name': 'Dragon', 'hp': 80, 'attack': 10, 'block': 5, 'burn_duration': 0, 'burn_damage': 0, 'immune_to_fire': True}
        ]
        self.turn = 0

    def dungeoncombat(self, monster, floor):
        print(f"==Combat with {monster['name']}==")
        while self.player['hp'] > 0 and monster['hp'] > 0:
            self.turn += 1
            print(f"\nTurn {self.turn}:")
            print(f"Player HP: {self.player['hp']} | Monster HP: {monster['hp']}")
            print(f"Player MP: {self.player['magic_points']} | Player Stamina: {self.player['stamina']}")

            # player's turn logic
            player_action = input("Choose action (1: Attack with Weapon, 2: Attack with Magic, 3: Block): ")
            if player_action == '1' and self.player['stamina'] >= 5:
                # attack w/ Weapon
                self.player['stamina'] -= 5
                if self.player['excalir_damage'] is None:
                    damage = self.player['attack']
                else:
                    base_damage = self.player['excalir_damage']
                    if self.player['hp'] <= 25:
                        damage = base_damage * 1.5  # true form of excal.
                    else:
                        damage = base_damage * (1 + (100 - self.player['hp']) // 25 * 0.05)
                monster['hp'] -= max(0, damage - monster['block'])
                print(f"Player attacks {monster['name']} with weapon for {damage} damage.")
            elif player_action == '2' and self.player['magic_points'] >= 5 and self.player['stamina'] >= 5:
                # attack w/ magic
                self.player['stamina'] -= 5
                self.player['magic_points'] -= 5
                magic_action = input("Choose magic (1: Fireball, 2: Water Nebula, 3: Frostbite): ")
                if magic_action == '1':
                    if 'immune_to_fire' in monster and monster['immune_to_fire']:
                        print(f"Player casts Fireball on {monster['name']} but it is immune to fire!")
                    else:
                        monster['hp'] -= max(0, self.player['fireball_damage'] - monster['block'])
                        print(f"Player casts Fireball on {monster['name']} for {self.player['fireball_damage']} damage.")
                        # 30% chance to cause burn damage
                        if random.random() < 0.3:
                            monster['burn_duration'] = 3  # Burn lasts for 3 turns
                            monster['burn_damage'] = self.player['burn_damage']  # burn does additional damage per turn
                            print(f"{monster['name']} is now burning!")
                        else:
                            print("The Fireball did not cause a burn effect.")
                elif magic_action == '2' and self.player['water_nebula']:
                    monster['hp'] -= max(0, self.player['magic'] - monster['block'])
                    print(f"Player casts Water Nebula on {monster['name']} for {self.player['magic']} damage.")
                    if random.random() < 0.3:
                        monster['drowned'] = True  # 30% chance to drown
                        print(f"{monster['name']} is drowned and unable to move for one turn!")
                    if 'burn_duration' in monster:
                        monster['burn_duration'] = 0  # cancel burn effect
                        print(f"The burn effect on {monster['name']} has been canceled.")
                elif magic_action == '3' and self.player['ice_magic']:
                    damage = 20
                    if 'Dragon' in monster['name']:
                        damage *= 2  #double damage to dragons
                    monster['hp'] -= max(0, damage - monster['block'])
                    print(f"Player casts Frostbite on {monster['name']} for {damage} damage.")
                    # apply freeze effect
                    monster['frozen'] = True
                    print(f"{monster['name']} is frozen and cannot move for the next turn.")
                else:
                    print("Invalid action or not enough magic points/stamina.")
            elif player_action == '3' and self.player['stamina'] >= 5:
                # block
                self.player['stamina'] -= 5
                self.player['block'] += 5
                print("Player blocks, increasing block value temporarily.")
            else:
                print("Invalid action or not enough magic points/stamina.")

            # apply burn damage to monster
            if monster['burn_duration'] > 0:
                monster['hp'] -= monster['burn_damage']
                monster['burn_duration'] -= 1
                print(f"{monster['name']} takes {monster['burn_damage']} burn damage.")

            if monster['hp'] <= 0:
                print(f"{monster['name']} is defeated!")
                self.collect_loot()
                return True

            # Monster's turn
            if 'frozen' in monster and monster['frozen']:
                print(f"{monster['name']} is frozen and cannot move this turn.")
                monster['frozen'] = False  # Reset frozen status
            elif 'drowned' in monster and monster['drowned']:
                print(f"{monster['name']} is drowned and cannot move this turn.")
                monster['drowned'] = False  # Reset drowned status
            else:
                monster_action = random.choice(['attack', 'block'])
                if monster_action == 'attack':
                    self.player['hp'] -= max(0, monster['attack'] - self.player['block'])
                    print(f"{monster['name']} attacks Player for {monster['attack']} damage.")
                elif monster_action == 'block':
                    monster['block'] += 3
                    print(f"{monster['name']} blocks, increasing block value temporarily.")

            # apply burn damage to player if burned
            if self.player['burn_duration'] > 0:
                self.player['hp'] -= self.player['burn_damage']
                self.player['burn_duration'] -= 1
                print(f"Player takes {self.player['burn_damage']} burn damage.")

            # reset block [increases for x turns]
            if player_action == '3':
                self.player['block'] -= 5
            if monster_action == 'block':
                monster['block'] -= 3
            #player hp
            if self.player['hp'] <= 0:
                print("Player is defeated!")
                return False
        return True

    def collect_loot(self):
        print("You found loot!")
        self.player['hp'] = min(100, self.player['hp'] + 20)  # Restores up to 20 HP
        self.player['magic_points'] = min(20, self.player['magic_points'] + 10)  # Restores up to 10 MP
        self.player['stamina'] = min(50, self.player['stamina'] + 20)
        # Restores up to 20 stamina
        print("Loot collected: +20 HP, +10 MP, +20 Stamina")

    def dungeonmonster(self, floor):
        monster = random.choice(self.monsters).copy()
        monster['hp'] = int(monster['hp'] * (1 + 0.1 * (floor - 1)))
        monster['attack'] = int(monster['attack'] * (1 + 0.1 * (floor - 1)))
        monster['block'] = int(monster['block'] * (1 + 0.1 * (floor - 1)))
        return monster

    def dungeonconquered(self):
        print("Congratulations! You have conquered the dungeon!")
        print(f"Your final score is: {self.player['score']}")
        # implementing more reward logic here eventually

    def dungeonpuzzle(self):
        print("== You have encountered a puzzle room in the dungeon! ==")
        print("Solve the puzzle to earn a reward.")
        number_to_guess = random.randint(1, 10)
        attempts = 3
        while attempts > 0:
            guess = int(input(f"Guess the number (1-10), {attempts} attempts remaining: "))
            if guess == number_to_guess:
                print("Correct! You have solved the puzzle.")
                self.grant_reward()
                return
            else:
                print("Incorrect guess.")
            attempts -= 1
        print("You failed to solve the puzzle. No reward this time.")
#maybe some sort of debuff for failing dungeon puzzles
    #dialogue-based dungeon games with specific moves that must be made
    def grant_reward(self):
        rewards = [
            {"name": "Fire Magic Book", "effect": self.learn_fire_magic},
            {"name": "Water Magic Book", "effect": self.learn_water_magic},
            {"name": "Ice Magic Book", "effect": self.learn_ice_magic},
            {"name": "Excalir Sword", "effect": self.obtain_excalir}
        ]
        reward = random.choice(rewards)
        print(f"You have received a {reward['name']}!")
        reward['effect']()

    def learn_fire_magic(self):
        self.player['fireball_damage'] += 10
        self.player['burn_damage'] += 5
        print("Your fireball damage has increased by 10 and burn damage by 5!")

    def learn_water_magic(self):
        self.player['water_nebula'] = True
        print("You have learned the Water Nebula spell! It can affect dragons and has a chance to drown enemies.")

    def learn_ice_magic(self):
        self.player['ice_magic'] = True
        print("You have learned the Frostbite spell! It deals 20 damage and can freeze monsters. It's super effective against dragons.")

    def obtain_excalir(self):
        self.player['excalir_damage'] = 30
        print("You have obtained the Excalir sword! It does 30 base damage and its damage increases as you lose HP.")

    def play_game(self):
        for floor in range(1, 11):
            print(f"\n== Floor {floor} ==")
            if floor % 5 == 0:
                self.dungeonpuzzle()
            else:
                encounter_prob = 0.1
                if random.random() > encounter_prob:  # Probability to encounter a monster
                    monster = self.dungeonmonster(floor)
                    if not self.dungeoncombat(monster, floor):
                        print("Game Over!")
                        return
                else:
                    print("No encounters. Moving to the next floor.")

        self.mother_dragon_boss()
        self.dungeonconquered()

    def mother_dragon_boss(self):
        print("== You have reached the final floor and encountered the Mother Dragon! ==")
        mother_dragon = {
            'name': 'Mother Dragon',
            'hp': 240,
            'attack': 30,
            'block': 15,
            'burn_duration': 0,
            'burn_damage': 0,
            'immune_to_fire': True,
            'egg_minions': 0
        }
        while self.player['hp'] > 0 and mother_dragon['hp'] > 0:
            self.turn += 1
            print(f"\nTurn {self.turn}:")
            print(f"Player HP: {self.player['hp']} | Mother Dragon HP: {mother_dragon['hp']}")
            print(f"Player MP: {self.player['magic_points']} | Player Stamina: {self.player['stamina']}")

            # player
            player_action = input("Choose action (1: Attack with Weapon, 2: Attack with Magic, 3: Block): ")
            if player_action == '1' and self.player['stamina'] >= 5:
                # attack w. weapon
                self.player['stamina'] -= 5
                if self.player['excalir_damage'] is None:
                    damage = self.player['attack']
                else:
                    base_damage = self.player['excalir_damage']
                    if self.player['hp'] <= 25:
                        damage = base_damage * 1.5
                    else:
                        damage = base_damage * (1 + (100 - self.player['hp']) // 25 * 0.05)
                mother_dragon['hp'] -= max(0, damage - mother_dragon['block'])
                print(f"Player attacks Mother Dragon with weapon for {damage} damage.")
            elif player_action == '2' and self.player['magic_points'] >= 5 and self.player['stamina'] >= 5:
                # attack w/ magic
                self.player['stamina'] -= 5
                self.player['magic_points'] -= 5
                magic_action = input("Choose magic (1: Fireball, 2: Water Nebula, 3: Frostbite): ")
                if magic_action == '1':
                    print(f"Player casts Fireball on Mother Dragon but she is immune to fire!")
                elif magic_action == '2' and self.player['water_nebula']:
                    mother_dragon['hp'] -= max(0, self.player['magic'] - mother_dragon['block'])
                    print(f"Player casts Water Nebula on Mother Dragon for {self.player['magic']} damage.")
                    if random.random() < 0.3:
                        mother_dragon['drowned'] = True  # 30% chance to drown!
                        print(f"Mother Dragon is drowned and unable to move for one turn!")
                elif magic_action == '3' and self.player['ice_magic']:
                    damage = 20
                    damage *= 2  #double dmg to Mother Dragon
                    mother_dragon['hp'] -= max(0, damage - mother_dragon['block'])
                    print(f"Player casts Frostbite on Mother Dragon for {damage} damage.")
                    # apply freeze [still deciding if this is applicable]
                    mother_dragon['frozen'] = True #will implement probability for this soon.
                    print(f"Mother Dragon is frozen and cannot move for the next turn.")
                else:
                    print("Invalid action or not enough magic points/stamina.")
            elif player_action == '3' and self.player['stamina'] >= 5:
                # block
                self.player['stamina'] -= 5
                self.player['block'] += 5
                print("Player blocks, increasing block value temporarily.")
            else:
                print("Invalid action or not enough magic points/stamina.")

            # apply burn dmg to mother dragon
            if mother_dragon['burn_duration'] > 0:
                mother_dragon['hp'] -= mother_dragon['burn_damage']
                mother_dragon['burn_duration'] -= 1
                print(f"Mother Dragon takes {mother_dragon['burn_damage']} burn damage.")

            if mother_dragon['hp'] <= 0:
                print("Mother Dragon is defeated!")
                return

            #mother dragon's turn logic
            if 'frozen' in mother_dragon and mother_dragon['frozen']:
                print("Mother Dragon is frozen and cannot move this turn.")
                mother_dragon['frozen'] = False  # Reset frozen status
            elif 'drowned' in mother_dragon and mother_dragon['drowned']:
                print("Mother Dragon is drowned and cannot move this turn.")
                mother_dragon['drowned'] = False  # Reset drowned status
            else:
                mother_dragon_action = random.choice(['attack', 'lay_egg'])
                if mother_dragon_action == 'attack':
                    self.player['hp'] -= max(0, mother_dragon['attack'] - self.player['block'])
                    print(f"Mother Dragon attacks Player for {mother_dragon['attack']} damage.")
                elif mother_dragon_action == 'lay_egg' and mother_dragon['egg_minions'] < 2:
                    mother_dragon['egg_minions'] += 1
                    print("Mother Dragon lays an egg. A baby dragon will hatch in 3 turns.")
                    egg_turns = 3

            #block
            if player_action == '3':
                self.player['block'] -= 5

            if self.player['hp'] <= 0:
                print("Player is defeated!")
                return False

        return True

#still needs experience system

#running the game cmd
dungeon = Dungeon()
dungeon.play_game()
