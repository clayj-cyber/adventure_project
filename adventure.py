import random

class Stats:
    def __init__(self):
        self.strength = 5
        self.defense = 5
        self.magic_defense = 5
        self.speed = 5
        self.magic_power = 5
        self.stamina = 5
        self.magic_cost = 5
        self.stat_points = 0
        self.skill_points = 0

    def allocate_stat_points(self):
        while self.stat_points > 0:
            print("\nAllocate your stat points:")
            print(f"1. Strength: {self.strength}")
            print(f"2. Defense: {self.defense}")
            print(f"3. Magic Defense: {self.magic_defense}")
            print(f"4. Speed: {self.speed}")
            print(f"5. Magic Power: {self.magic_power}")
            print(f"6. Stamina: {self.stamina}")
            print(f"7. Magic Cost: {self.magic_cost}")
            print(f"Stat points available: {self.stat_points}")
            choice = int(input("Choose a stat to increase (1-7): "))
            if choice in range(1, 8):
                points = int(input("Enter the number of points to allocate: "))
                if points <= self.stat_points:
                    if choice == 1:
                        self.strength += points
                    elif choice == 2:
                        self.defense += points
                    elif choice == 3:
                        self.magic_defense += points
                    elif choice == 4:
                        self.speed += points
                    elif choice == 5:
                        self.magic_power += points
                    elif choice == 6:
                        self.stamina += points
                    elif choice == 7:
                        self.magic_cost += points
                    self.stat_points -= points
                else:
                    print("Not enough stat points.")
            else:
                print("Invalid choice.")
        print("Stat points allocated successfully.")

class Player:
    def __init__(self):
        self.name = 'Hero'
        self.level = 1
        self.hp = 100
        self.base_attack = 10
        self.magic = 15
        self.weapon = 10
        self.magic_points = 50
        self.burn_duration = 0
        self.burn_damage = 0
        self.score = 0
        self.stamina = 100
        self.experience = 0
        self.stats = Stats()
        self.inventory = {
            'potions': [],
            'elixirs': [],
            'rings': [],
            'weapons': []
        }
        self.spells = {
            'fireball': True,
            'water_nebula': False,
            'frostbite': False
        }
        self.equipped_ring = None
        self.equipped_weapon = 'Basic Weapon'
        self.excalir = False

    def level_up(self):
        self.level += 1
        self.stats.stat_points += 5
        self.experience -= self.experience_to_next_level()
        if self.level % 5 == 0:
            self.stats.skill_points += 1
        print(f"You leveled up to level {self.level}! You have {self.stats.stat_points} stat points to allocate.")
        self.stats.allocate_stat_points()

    def experience_to_next_level(self):
        return 100 * (1.1 ** (self.level - 1))

    def gain_experience(self, amount):
        self.experience += amount
        while self.experience >= self.experience_to_next_level():
            self.level_up()

    def equip_ring(self):
        if not self.inventory['rings']:
            print("You have no rings to equip.")
            return

        print("Available rings:")
        for i, ring in enumerate(self.inventory['rings']):
            print(f"{i + 1}: {ring}")

        choice = int(input("Choose a ring to equip: ")) - 1
        if 0 <= choice < len(self.inventory['rings']):
            self.equipped_ring = self.inventory['rings'][choice]
            print(f"You have equipped the {self.equipped_ring}.")
        else:
            print("Invalid choice.")

    def equip_weapon(self):
        if not self.inventory['weapons']:
            print("You have no weapons to equip.")
            return

        print("Available weapons:")
        for i, weapon in enumerate(self.inventory['weapons']):
            print(f"{i + 1}: {weapon}")

        choice = int(input("Choose a weapon to equip: ")) - 1
        if 0 <= choice < len(self.inventory['weapons']):
            self.equipped_weapon = self.inventory['weapons'][choice]
            print(f"You have equipped the {self.equipped_weapon}.")
        else:
            print("Invalid choice.")

    def obtain_excalir(self):
        self.excalir = True
        print("You have obtained the Excalir sword! It does 30 base damage and its damage increases as you lose HP.")

class Dungeon:
    def __init__(self):
        self.player = Player()
        self.monsters = [
            {'name': 'Goblin', 'hp': 30, 'attack': 5, 'burn_duration': 0, 'burn_damage': 0, 'exp': 100},
            {'name': 'Orc', 'hp': 50, 'attack': 7, 'burn_duration': 0, 'burn_damage': 0, 'exp': 80},
            {'name': 'Dragon', 'hp': 80, 'attack': 10, 'burn_duration': 0, 'burn_damage': 0, 'immune_to_fire': True, 'exp': 400}
        ]
        self.turn = 0

    def dungeoncombat(self, monster, floor):
        print(f"==Combat with {monster['name']}==")
        while self.player.hp > 0 and monster['hp'] > 0:
            self.turn += 1
            print(f"\nTurn {self.turn}:")
            print(f"Player HP: {self.player.hp} | Monster HP: {monster['hp']}")
            print(f"Player MP: {self.player.magic_points} | Player Stamina: {self.player.stamina}")

            # Player's turn
            if self.player.excalir:
                player_action = input("Choose action (1: Attack with Excalir, 2: Attack with Magic, 3: Inventory, 4: Stats, 5: Flee): ")
            else:
                player_action = input("Choose action (1: Attack with Weapon, 2: Attack with Magic, 3: Inventory, 4: Stats, 5: Flee): ")

            if player_action == '1' and self.player.stamina >= 5:
                # Attack with Weapon or Excalir
                self.player.stamina -= 5
                damage = self.player.base_attack * (1 + self.player.stats.strength / 100)
                if self.player.excalir:
                    if self.player.hp <= 25:
                        damage *= 1.5  # True form of Excalir
                    else:
                        damage *= 1 + (100 - self.player.hp) // 25 * 0.05
                monster['hp'] -= max(0, damage)
                print(f"Player attacks {monster['name']} with weapon for {damage} damage.")
            elif player_action == '2' and self.player.magic_points >= 5 and self.player.stamina >= 5:
                # Attack with Magic
                self.player.stamina -= 5
                self.player.magic_points -= 5
                available_spells = self.get_available_spells()
                if available_spells:
                    magic_action = input(f"Choose magic {available_spells}: ")
                    self.cast_spell(magic_action, monster)
                else:
                    print("You have no spells available.")
            elif player_action == '3':
                # Inventory
                self.use_inventory()
            elif player_action == '4':
                # Stats breakdown
                self.display_stats()
            elif player_action == '5':
                # Flee
                if self.flee():
                    print("You successfully fled the combat.")
                    return False
                else:
                    print("Failed to flee.")
            else:
                print("Invalid action or not enough magic points/stamina.")

            # Apply burn damage to monster
            if monster['burn_duration'] > 0:
                burn_damage = monster['burn_damage']
                monster['hp'] -= burn_damage
                monster['burn_duration'] -= 1
                print(f"{monster['name']} takes {burn_damage} burn damage.")

            if monster['hp'] <= 0:
                print(f"{monster['name']} is defeated!")
                self.player.score += 2 if floor % 10 == 0 else 1  # Double score for bosses
                self.player.gain_experience(monster['exp'])
                self.collect_loot()
                self.replenish_resources()
                return True

            # Monster's turn
            if 'frozen' in monster and monster['frozen']:
                print(f"{monster['name']} is frozen and cannot move this turn.")
                monster['frozen'] = False  # Reset frozen status
            elif 'drowned' in monster and monster['drowned']:
                print(f"{monster['name']} is drowned and cannot move this turn.")
                monster['drowned'] = False  # Reset drowned status
            else:
                monster_action = random.choice(['attack'])
                if monster_action == 'attack':
                    self.player.hp -= max(0, monster['attack'] * (1 + floor * 0.01))
                    print(f"{monster['name']} attacks Player for {monster['attack']} damage.")

            # Apply burn damage to player if burned
            if self.player.burn_duration > 0:
                burn_damage = self.player.burn_damage
                self.player.hp -= burn_damage
                self.player.burn_duration -= 1
                print(f"Player takes {burn_damage} burn damage.")

            if self.player.hp <= 0:
                print("Player is defeated!")
                return False
        return True

    def flee(self):
        flee_chance = 0.5  # 50% chance to flee
        return random.random() < flee_chance

    def get_available_spells(self):
        spells = []
        if self.player.spells['fireball']:
            spells.append('1: Fireball')
        if self.player.spells['water_nebula']:
            spells.append('2: Water Nebula')
        if self.player.spells['frostbite']:
            spells.append('3: Frostbite')
        return spells

    def cast_spell(self, magic_action, monster):
        if magic_action == '1' and self.player.spells['fireball']:
            if 'immune_to_fire' in monster and monster['immune_to_fire']:
                print(f"Player casts Fireball on {monster['name']} but it is immune to fire!")
            else:
                damage = self.player.magic * (1 + self.player.stats.magic_power / 100)
                monster['hp'] -= max(0, damage)
                print(f"Player casts Fireball on {monster['name']} for {damage} damage.")
                # 30% chance to cause burn damage
                if random.random() < 0.3:
                    monster['burn_duration'] = 3  # Burn lasts for 3 turns
                    monster['burn_damage'] = 5 + self.player.stats.magic_power  # Burn does additional damage per turn
                    print(f"{monster['name']} is now burning!")
                else:
                    print("The Fireball did not cause a burn effect.")
        elif magic_action == '2' and self.player.spells['water_nebula']:
            damage = self.player.magic * (1 + self.player.stats.magic_power / 100)
            monster['hp'] -= max(0, damage)
            print(f"Player casts Water Nebula on {monster['name']} for {damage} damage.")
            if random.random() < 0.3:
                monster['drowned'] = True  # 30% chance to drown
                print(f"{monster['name']} is drowned and unable to move for one turn!")
            if 'burn_duration' in monster:
                monster['burn_duration'] = 0  # Cancel burn effect
                print(f"The burn effect on {monster['name']} has been canceled.")
        elif magic_action == '3' and self.player.spells['frostbite']:
            damage = 20
            if 'Dragon' in monster['name']:
                damage *= 2  # Double damage to dragons
            monster['hp'] -= max(0, damage)
            print(f"Player casts Frostbite on {monster['name']} for {damage} damage.")
            # Apply freeze effect
            monster['frozen'] = True
            print(f"{monster['name']} is frozen and cannot move for the next turn.")
        else:
            print("Invalid magic action or spell not learned.")

    def use_inventory(self):
        print("== Inventory ==")
        print("1: Equip Ring")
        print("2: Equip Weapon")
        for i, item in enumerate(self.player.inventory['potions']):
            print(f"{i + 3}: {item}")

        choice = int(input("Choose an inventory option: ")) - 1
        if choice == 0:
            self.player.equip_ring()
        elif choice == 1:
            self.player.equip_weapon()
        elif 2 <= choice < 2 + len(self.player.inventory['potions']):
            potion = self.player.inventory['potions'].pop(choice - 2)
            self.apply_potion_effect(potion)
        else:
            print("Invalid choice.")

    def apply_potion_effect(self, potion):
        if potion == 'Health Potion':
            self.player.hp += 50
            print("You used a Health Potion and restored 50 HP.")
        elif potion == 'Stamina Potion':
            self.player.stamina += 50
            print("You used a Stamina Potion and restored 50 Stamina.")
        elif potion == 'Magic Elixir':
            self.player.magic_points += 40
            print("You used a Magic Elixir and restored 20 Magic Points.")

    def replenish_resources(self):
        self.player.stamina += 10
        self.player.magic_points += 10
        print("You have replenished 10 Stamina and 10 Magic Points after the fight.")

    def display_stats(self):
        print("== Player Stats ==")
        print(f"HP: {self.player.hp}")
        print(f"MP: {self.player.magic_points}")
        print(f"Stamina: {self.player.stamina}")
        print(f"Level: {self.player.level}")
        print(f"Strength: {self.player.stats.strength}")
        print(f"Defense: {self.player.stats.defense}")
        print(f"Magic Defense: {self.player.stats.magic_defense}")
        print(f"Speed: {self.player.stats.speed}")
        print(f"Magic Power: {self.player.stats.magic_power}")
        print(f"Stamina: {self.player.stats.stamina}")
        print(f"Magic Cost: {self.player.stats.magic_cost}")
        input("Press Enter to return to combat...")

    def collect_loot(self):
        loot_chance = random.random()
        if loot_chance < 0.1:
            print("You have found a rare item!")
        elif loot_chance < 0.9:
            num_potions = random.choices([1, 2, 3], weights=[0.6, 0.3, 0.1])[0]
            for _ in range(num_potions):
                potion = random.choice(['Health Potion', 'Stamina Potion', 'Magic Elixir'])
                self.player.inventory['potions'].append(potion)
                print(f"Found {potion}!")
        else:
            ring_type = random.choice(['Attack Ring', 'Magic Ring'])
            self.player.inventory['rings'].append(ring_type)
            print(f"Found {ring_type}!")

    def dungeonmonster(self, floor):
        if random.random() < 0.1:
            monster = random.choice([m for m in self.monsters if m['name'] == 'Dragon']).copy()
        else:
            monster = random.choice([m for m in self.monsters if m['name'] != 'Dragon']).copy()
        monster['hp'] = int(monster['hp'] * (1 + 0.05 * floor))
        monster['attack'] = int(monster['attack'] * (1 + 0.05 * floor))
        return monster

    def clear_floor(self, floor):
        self.player.score += 5
        input(f"You cleared floor {floor}. Press Enter to continue traversing the dungeon.")
        self.player.gain_experience(100)

    def dungeonconquered(self):
        print("Congratulations! You have conquered the dungeon!")
        print(f"Your final score is: {self.player.score}")
        # Implement additional reward logic here

    def dungeonpuzzle(self):
        print("== You have encountered a puzzle room! ==")
        print("Solve the puzzle to earn a reward.")
        number_to_guess = random.randint(1, 10)
        attempts = 3
        while attempts > 0:
            user_input = input(f"Guess the number (1-10), {attempts} attempts remaining: ")
            guess = int(user_input)
            if 1 <= guess <= 10:
                if guess == number_to_guess:
                    print("Correct! You have solved the puzzle.")
                    self.grant_reward()
                    return
                else:
                    print("Incorrect guess.")
                attempts -= 1
        print("You failed to solve the puzzle. No reward this time.")

    def grant_reward(self):
        rewards = [
            {"name": "Fire Magic Book", "effect": self.learn_fire_magic},
            {"name": "Water Magic Book", "effect": self.learn_water_magic},
            {"name": "Ice Magic Book", "effect": self.learn_ice_magic},
            {"name": "Excalir Sword", "effect": self.player.obtain_excalir}
        ]
        reward = random.choice(rewards)
        print(f"You have received a {reward['name']}!")
        reward['effect']()

    def learn_fire_magic(self):
        self.player.fireball_damage += 10
        self.player.burn_damage += 5
        print("Your fireball damage has increased by 10 and burn damage by 5!")

    def learn_water_magic(self):
        self.player.spells['water_nebula'] = True
        print("You have learned the Water Nebula spell! It can affect dragons and has a chance to drown enemies.")

    def learn_ice_magic(self):
        self.player.spells['frostbite'] = True
        print("You have learned the Frostbite spell! It deals 20 damage and can freeze monsters. It's super effective against dragons.")

    def play_game(self):
        for floor in range(1, 51):
            print(f"\n== Floor {floor} ==")
            if floor % 5 == 0:
                self.dungeonpuzzle()
            else:
                encounter_prob = 0.3 + 0.1 * (floor % 10)  # Increase encounter probability with each floor in the set of 10
                while random.random() < encounter_prob:  # Probability to encounter a monster, can stack
                    monster = self.dungeonmonster(floor)
                    if not self.dungeoncombat(monster, floor):
                        print("Game Over!")
                        return
            self.clear_floor(floor)

        self.leviant_boss()
        self.dungeonconquered()

    def mother_dragon_boss(self):
        print("== You have reached the final floor and encountered the Mother Dragon! ==")
        mother_dragon = {
            'name': 'Mother Dragon',
            'hp': 240,
            'attack': 30,
            'burn_duration': 0,
            'burn_damage': 0,
            'immune_to_fire': True,
            'egg_minions': 0
        }
        while self.player.hp > 0 and mother_dragon['hp'] > 0:
            self.turn += 1
            print(f"\nTurn {self.turn}:")
            print(f"Player HP: {self.player.hp} | Mother Dragon HP: {mother_dragon['hp']}")
            print(f"Player MP: {self.player.magic_points} | Player Stamina: {self.player.stamina}")

            # Player's turn
            if self.player.excalir:
                player_action = input("Choose action (1: Attack with Excalir, 2: Attack with Magic): ")
            else:
                player_action = input("Choose action (1: Attack with Weapon, 2: Attack with Magic): ")

            if player_action == '1' and self.player.stamina >= 5:
                # Attack with Weapon or Excalir
                self.player.stamina -= 5
                if self.player.excalir:
                    if self.player.hp <= 25:
                        damage = self.player.base_attack * 1.5  # True form of Excalir
                    else:
                        damage = self.player.base_attack * (1 + (100 - self.player.hp) // 25 * 0.05)
                else:
                    damage = self.player.base_attack
                mother_dragon['hp'] -= max(0, damage)
                print(f"Player attacks Mother Dragon with weapon for {damage} damage.")
            elif player_action == '2' and self.player.magic_points >= 5 and self.player.stamina >= 5:
                # Attack with Magic
                self.player.stamina -= 5
                self.player.magic_points -= 5
                available_spells = self.get_available_spells()
                if available_spells:
                    magic_action = input(f"Choose magic {available_spells}: ")
                    self.cast_spell(magic_action, mother_dragon)
                else:
                    print("You have no spells available.")
            else:
                print("Invalid action or not enough magic points/stamina.")

            # Apply burn damage to Mother Dragon
            if mother_dragon['burn_duration'] > 0:
                burn_damage = 5 + self.player.stats.magic_power
                mother_dragon['hp'] -= burn_damage
                mother_dragon['burn_duration'] -= 1
                print(f"Mother Dragon takes {burn_damage} burn damage.")

            if mother_dragon['hp'] <= 0:
                print("Mother Dragon is defeated!")
                self.player.score += 2
                return

            # Mother Dragon's turn
            if 'frozen' in mother_dragon and mother_dragon['frozen']:
                print("Mother Dragon is frozen and cannot move this turn.")
                mother_dragon['frozen'] = False  # Reset frozen status
            elif 'drowned' in mother_dragon and mother_dragon['drowned']:
                print("Mother Dragon is drowned and cannot move this turn.")
                mother_dragon['drowned'] = False  # Reset drowned status
            else:
                mother_dragon_action = random.choice(['attack', 'lay_egg'])
                if mother_dragon_action == 'attack':
                    self.player.hp -= max(0, mother_dragon['attack'])
                    print(f"Mother Dragon attacks Player for {mother_dragon['attack']} damage.")
                elif mother_dragon_action == 'lay_egg' and mother_dragon['egg_minions'] < 2:
                    mother_dragon['egg_minions'] += 1
                    print("Mother Dragon lays an egg. A baby dragon will hatch in 3 turns.")
                    egg_turns = 3

            if self.player.hp <= 0:
                print("Player is defeated!")
                return False

        return True

    def leviant_boss(self):
        print("== You have reached floor 50 and encountered Leviant, the powerful plant creature! ==")
        leviant = {
            'name': 'Leviant',
            'hp': 200,
            'attack': 25,
            'burn_duration': 0,
            'burn_damage': 0,
            'regenerate': 0,
            'poisoned': 0
        }
        while self.player.hp > 0 and leviant['hp'] > 0:
            self.turn += 1
            print(f"\nTurn {self.turn}:")
            print(f"Player HP: {self.player.hp} | Leviant HP: {leviant['hp']}")
            print(f"Player MP: {self.player.magic_points} | Player Stamina: {self.player.stamina}")

            # Player's turn
            if self.player.excalir:
                player_action = input("Choose action (1: Attack with Excalir, 2: Attack with Magic): ")
            else:
                player_action = input("Choose action (1: Attack with Weapon, 2: Attack with Magic): ")

            if player_action == '1' and self.player.stamina >= 5:
                # Attack with Weapon or Excalir
                self.player.stamina -= 5
                damage = self.player.base_attack * (1 + self.player.stats.strength / 100)
                if self.player.excalir:
                    if self.player.hp <= 25:
                        damage *= 1.5  # True form of Excalir
                    else:
                        damage *= 1 + (100 - self.player.hp) // 25 * 0.05
                leviant['hp'] -= max(0, damage)
                print(f"Player attacks Leviant with weapon for {damage} damage.")
            elif player_action == '2' and self.player.magic_points >= 5 and self.player.stamina >= 5:
                # Attack with Magic
                self.player.stamina -= 5
                self.player.magic_points -= 5
                available_spells = self.get_available_spells()
                if available_spells:
                    magic_action = input(f"Choose magic {available_spells}: ")
                    self.cast_spell(magic_action, leviant)
                else:
                    print("You have no spells available.")
            else:
                print("Invalid action or not enough magic points/stamina.")

            # Apply burn damage to Leviant
            if leviant['burn_duration'] > 0:
                burn_damage = 5 + self.player.stats.magic_power
                leviant['hp'] -= burn_damage
                leviant['burn_duration'] -= 1
                print(f"Leviant takes {burn_damage} burn damage.")

            if leviant['hp'] <= 0:
                print(f"Leviant is defeated!")
                self.player.score += 2
                self.player.gain_experience(200)
                self.replenish_resources()
                return

            # Leviant's turn
            leviant_action = random.choice(['attack', 'regenerate', 'poison'])
            if leviant_action == 'attack':
                self.player.hp -= max(0, leviant['attack'])
                print(f"Leviant attacks Player for {leviant['attack']} damage.")
            elif leviant_action == 'regenerate' and leviant['regenerate'] == 0:
                leviant['hp'] += 50
                leviant['regenerate'] = 5  # Regen lasts for 5 turns
                print("Leviant regenerates 50 HP.")
            elif leviant_action == 'poison' and leviant['poisoned'] == 0:
                self.player.hp -= 5
                leviant['poisoned'] = 5  # Poison lasts for 5 turns
                print("Leviant poisons Player, dealing 5 damage per turn.")

            # Apply poison damage to player
            if leviant['poisoned'] > 0:
                self.player.hp -= 5
                leviant['poisoned'] -= 1
                print(f"Player takes 5 poison damage.")

            if self.player.hp <= 0:
                print("Player is defeated!")
                return False

        return True

# Example of running the game
dungeon = Dungeon()
dungeon.play_game()
