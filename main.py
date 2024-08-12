import random

class Stats:
    def __init__(self):
        # initialize stat attributes
        self.strength = 5
        self.defense = 5
        self.magic_defense = 5
        self.speed = 5
        self.magic_power = 5
        self.stamina = 5
        self.magic_cost = 5
        self.hp = 0  # additional stat for increasing max HP
        self.endurance = 0  # additional stat for increasing max stamina
        self.magic_amount = 0  # additional stat for increasing max magic points
        self.stat_points = 0
        self.skill_points = 0

    def allocate_stat_points(self):
        # logic to allocate stat points
        while self.stat_points > 0:
            print("\nAllocate your stat points:")
            print(f"1. Strength: {self.strength}")
            print(f"2. Defense: {self.defense}")
            print(f"3. Magic Defense: {self.magic_defense}")
            print(f"4. Speed: {self.speed}")
            print(f"5. Magic Power: {self.magic_power}")
            print(f"6. Stamina: {self.stamina}")
            print(f"7. Magic Cost: {self.magic_cost}")
            print(f"8. HP: {self.hp}")
            print(f"9. Endurance: {self.endurance}")
            print(f"10. Magic Amount: {self.magic_amount}")
            print(f"Stat points available: {self.stat_points}")
            try:
                choice = int(input("Choose a stat to increase (1-10): "))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 10.")
                continue
            if choice in range(1, 11):
                try:
                    points = int(input("Enter the number of points to allocate: "))
                except ValueError:
                    print("Invalid input. Please enter a valid number of points.")
                    continue
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
                    elif choice == 8:
                        self.hp += points
                    elif choice == 9:
                        self.endurance += points
                    elif choice == 10:
                        self.magic_amount += points
                    self.stat_points -= points
                else:
                    print("Not enough stat points.")
            else:
                print("Invalid choice.")
        print("Stat points allocated successfully.")

class Player:
    def __init__(self):
        # initialize player attributes, stats, inventory, etc.
        self.name = 'Hero'
        self.level = 1
        self.base_max_hp = 100
        self.base_max_stamina = 50
        self.base_max_magic_points = 40
        self.hp = self.base_max_hp
        self.max_hp = self.base_max_hp
        self.base_attack = 25
        self.magic = 25
        self.weapon = 25
        self.magic_points = self.base_max_magic_points
        self.max_magic_points = self.base_max_magic_points
        self.stamina = self.base_max_stamina
        self.max_stamina = self.base_max_stamina
        self.burn_duration = 0
        self.burn_damage = 0
        self.score = 0
        self.experience = 0
        self.stats = Stats()
        self.inventory = {
            'potions': {},
            'elixirs': {},
            'rings': [],
            'weapons': []
        }
        self.spells = {
            'fireball': True,
            'water_nebula': False,
            'frostbite': False,
            'ice_lance': False
        }
        self.spell_cooldowns = {
            'fireball': 0,
            'water_nebula': 0,
            'frostbite': 0,
            'ice_lance': 0,
            'esmera_slash': 0
        }
        self.equipped_rings = {
            'combat': 0,
            'magic': 0
        }
        self.equipped_weapon = 'Basic Weapon'
        self.excalir = False
        self.is_shielded = False
        self.shield_turns = 0
        self.gold = 0

    def level_up(self):
        # logic for leveling up the player
        self.level += 1
        self.stats.stat_points += 5
        self.experience -= self.experience_to_next_level()
        if self.level % 5 == 0:
            self.stats.skill_points += 1
        print(f"You leveled up to level {self.level}! You have {self.stats.stat_points} stat points to allocate.")
        self.stats.allocate_stat_points()
        self.update_max_values()

    def experience_to_next_level(self):
        # calculate experience needed for the next level
        return 100 * (1.1 ** (self.level - 1))

    def gain_experience(self, amount):
        # Gain experience and potentially level up
        self.experience += amount
        while self.experience >= self.experience_to_next_level():
            self.level_up()

    def update_max_values(self):
        # update max values for HP, stamina, and magic points
        self.max_hp = self.base_max_hp + round(self.stats.hp)
        self.max_stamina = self.base_max_stamina + round(self.stats.endurance)
        self.max_magic_points = self.base_max_magic_points + round(self.stats.magic_amount)
        self.hp = min(self.hp, self.max_hp)
        self.stamina = min(self.stamina, self.max_stamina)
        self.magic_points = min(self.magic_points, self.max_magic_points)

    def equip_ring(self):
        # Equip a ring from the inventory
        if not self.inventory['rings']:
            print("You have no rings to equip.")
            return

        if sum(self.equipped_rings.values()) >= 10:
            print("You cannot equip more than 10 rings.")
            return

        print("Available rings:")
        for i, ring in enumerate(self.inventory['rings']):
            print(f"{i + 1}: {ring}")

        try:
            choice = int(input("Choose a ring to equip: ")) - 1
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        if 0 <= choice < len(self.inventory['rings']):
            ring = self.inventory['rings'].pop(choice)
            if ring == 'Combat Ring':
                self.equipped_rings['combat'] += 1
            elif ring == 'Magic Ring':
                self.equipped_rings['magic'] += 1
            print(f"You have equipped the {ring}.")
        else:
            print("Invalid choice.")

    def equip_weapon(self):
        # Equip a weapon from the inventory
        if not self.inventory['weapons']:
            print("You have no weapons to equip.")
            return

        print("Available weapons:")
        for i, weapon in enumerate(self.inventory['weapons']):
            print(f"{i + 1}: {weapon}")

        try:
            choice = int(input("Choose a weapon to equip: ")) - 1
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        if 0 <= choice < len(self.inventory['weapons']):
            self.equipped_weapon = self.inventory['weapons'][choice]
            print(f"You have equipped the {self.equipped_weapon}.")
        else:
            print("Invalid choice.")

class SpecialAbility:
    def __init__(self, name, effect, cooldown=2):
        # Initialize special ability attributes
        self.name = name
        self.effect = effect
        self.cooldown = cooldown
        self.current_cooldown = 0

    def use(self, user, target):
        # Logic to use a special ability
        print(f"{user.name} uses {self.name}!")
        self.effect(user, target)
        self.current_cooldown = self.cooldown

    def reduce_cooldown(self):
        # Reduce the cooldown of the ability
        if self.current_cooldown > 0:
            self.current_cooldown -= 1


# define special ability functions
def fire_breath(user, target):
    # logic for fire breath attack
    damage = 20 + user.level * 2
    target.hp -= damage
    target.is_burning = True
    target.burn_duration = 6
    print(f"{target.name} takes {damage} fire damage and is burning!")

def water_heal(user):
    # logic for water healing ability
    heal_amount = 20 + user.level * 2
    user.hp += heal_amount
    print(f"{user.name} heals for {heal_amount} HP!")

def smash(user, target):
    # logic for smash attack
    damage = 10 + user.level * 2
    target.hp -= damage
    print(f"{user.name} smashes {target.name} for {damage} damage!")

def water_nebula(user, target):
    # logic for water nebula attack
    base_damage = user.level * 2 + 10
    if isinstance(user, Player):
import random

class Stats:
    def __init__(self):
        # initialize stat attributes
        self.strength = 5
        self.defense = 5
        self.magic_defense = 5
        self.speed = 5
        self.magic_power = 5
        self.stamina = 5
        self.magic_cost = 5
        self.hp = 0  # additional stat for increasing max HP
        self.endurance = 0  # additional stat for increasing max stamina
        self.magic_amount = 0  # additional stat for increasing max magic points
        self.stat_points = 0
        self.skill_points = 0

    def allocate_stat_points(self):
        # logic to allocate stat points
        while self.stat_points > 0:
            print("\nAllocate your stat points:")
            print(f"1. Strength: {self.strength}")
            print(f"2. Defense: {self.defense}")
            print(f"3. Magic Defense: {self.magic_defense}")
            print(f"4. Speed: {self.speed}")
            print(f"5. Magic Power: {self.magic_power}")
            print(f"6. Stamina: {self.stamina}")
            print(f"7. Magic Cost: {self.magic_cost}")
            print(f"8. HP: {self.hp}")
            print(f"9. Endurance: {self.endurance}")
            print(f"10. Magic Amount: {self.magic_amount}")
            print(f"Stat points available: {self.stat_points}")
            try:
                choice = int(input("Choose a stat to increase (1-10): "))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 10.")
                continue
            if choice in range(1, 11):
                try:
                    points = int(input("Enter the number of points to allocate: "))
                except ValueError:
                    print("Invalid input. Please enter a valid number of points.")
                    continue
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
                    elif choice == 8:
                        self.hp += points
                    elif choice == 9:
                        self.endurance += points
                    elif choice == 10:
                        self.magic_amount += points
                    self.stat_points -= points
                else:
                    print("Not enough stat points.")
            else:
                print("Invalid choice.")
        print("Stat points allocated successfully.")

class Player:
    def __init__(self):
        # initialize player attributes, stats, inventory, etc.
        self.name = 'Hero'
        self.level = 1
        self.base_max_hp = 100
        self.base_max_stamina = 50
        self.base_max_magic_points = 40
        self.hp = self.base_max_hp
        self.max_hp = self.base_max_hp
        self.base_attack = 25
        self.magic = 25
        self.weapon = 25
        self.magic_points = self.base_max_magic_points
        self.max_magic_points = self.base_max_magic_points
        self.stamina = self.base_max_stamina
        self.max_stamina = self.base_max_stamina
        self.burn_duration = 0
        self.burn_damage = 0
        self.score = 0
        self.experience = 0
        self.stats = Stats()
        self.inventory = {
            'potions': {},
            'elixirs': {},
            'rings': [],
            'weapons': []
        }
        self.spells = {
            'fireball': True,
            'water_nebula': False,
            'frostbite': False,
            'ice_lance': False
        }
        self.spell_cooldowns = {
            'fireball': 0,
            'water_nebula': 0,
            'frostbite': 0,
            'ice_lance': 0,
            'esmera_slash': 0
        }
        self.equipped_rings = {
            'combat': 0,
            'magic': 0
        }
        self.equipped_weapon = 'Basic Weapon'
        self.excalir = False
        self.is_shielded = False
        self.shield_turns = 0
        self.gold = 0

    def level_up(self):
        # logic for leveling up the player
        self.level += 1
        self.stats.stat_points += 5
        self.experience -= self.experience_to_next_level()
        if self.level % 5 == 0:
            self.stats.skill_points += 1
        print(f"You leveled up to level {self.level}! You have {self.stats.stat_points} stat points to allocate.")
        self.stats.allocate_stat_points()
        self.update_max_values()

    def experience_to_next_level(self):
        # calculate experience needed for the next level
        return 100 * (1.1 ** (self.level - 1))

    def gain_experience(self, amount):
        # Gain experience and potentially level up
        self.experience += amount
        while self.experience >= self.experience_to_next_level():
            self.level_up()

    def update_max_values(self):
        # update max values for HP, stamina, and magic points
        self.max_hp = self.base_max_hp + round(self.stats.hp)
        self.max_stamina = self.base_max_stamina + round(self.stats.endurance)
        self.max_magic_points = self.base_max_magic_points + round(self.stats.magic_amount)
        self.hp = min(self.hp, self.max_hp)
        self.stamina = min(self.stamina, self.max_stamina)
        self.magic_points = min(self.magic_points, self.max_magic_points)

    def equip_ring(self):
        # Equip a ring from the inventory
        if not self.inventory['rings']:
            print("You have no rings to equip.")
            return

        if sum(self.equipped_rings.values()) >= 10:
            print("You cannot equip more than 10 rings.")
            return

        print("Available rings:")
        for i, ring in enumerate(self.inventory['rings']):
            print(f"{i + 1}: {ring}")

        try:
            choice = int(input("Choose a ring to equip: ")) - 1
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        if 0 <= choice < len(self.inventory['rings']):
            ring = self.inventory['rings'].pop(choice)
            if ring == 'Combat Ring':
                self.equipped_rings['combat'] += 1
            elif ring == 'Magic Ring':
                self.equipped_rings['magic'] += 1
            print(f"You have equipped the {ring}.")
        else:
            print("Invalid choice.")

    def equip_weapon(self):
        # Equip a weapon from the inventory
        if not self.inventory['weapons']:
            print("You have no weapons to equip.")
            return

        print("Available weapons:")
        for i, weapon in enumerate(self.inventory['weapons']):
            print(f"{i + 1}: {weapon}")

        try:
            choice = int(input("Choose a weapon to equip: ")) - 1
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        if 0 <= choice < len(self.inventory['weapons']):
            self.equipped_weapon = self.inventory['weapons'][choice]
            print(f"You have equipped the {self.equipped_weapon}.")
        else:
            print("Invalid choice.")

    def block(self):
        # logic for blocking an attack
        block_value = self.stats.defense * 0.5
        return block_value

    def parry(self):
        # logic for parrying an attack
        parry_damage = self.stats.strength * 0.5
        return parry_damage

    def update_spell_cooldowns(self):
        # update spell cooldowns at the end of each turn
        for spell in self.spell_cooldowns:
            if self.spell_cooldowns[spell] > 0:
                self.spell_cooldowns[spell] -= 1


class SpecialAbility:
    def __init__(self, name, effect, cooldown=2):
        # Initialize special ability attributes
        self.name = name
        self.effect = effect
        self.cooldown = cooldown
        self.current_cooldown = 0

    def use(self, user, target):
        # Logic to use a special ability
        print(f"{user.name} uses {self.name}!")
        self.effect(user, target)
        self.current_cooldown = self.cooldown

    def reduce_cooldown(self):
        # Reduce the cooldown of the ability
        if self.current_cooldown > 0:
            self.current_cooldown -= 1


# define special ability functions
def fire_breath(user, target):
    # logic for fire breath attack
    damage = 20 + user.level * 2
    target.hp -= damage
    target.is_burning = True
    target.burn_duration = 6
    print(f"{target.name} takes {damage} fire damage and is burning!")

def water_heal(user):
    # logic for water healing ability
    heal_amount = 20

