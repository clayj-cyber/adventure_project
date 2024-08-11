from player.stats import Stats

class Player:
    def __init__(self):
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
        self.level += 1
        self.stats.stat_points += 5
        self.experience -= self.experience_to_next_level()
        if self.level % 5 == 0:
            self.stats.skill_points += 1
        print(f"You leveled up to level {self.level}! You have {self.stats.stat_points} stat points to allocate.")
        self.stats.allocate_stat_points()
        self.update_max_values()

    def experience_to_next_level(self):
        return 100 * (1.1 ** (self.level - 1))

    def gain_experience(self, amount):
        self.experience += amount
        while self.experience >= self.experience_to_next_level():
            self.level_up()

    def update_max_values(self):
        self.max_hp = self.base_max_hp + round(self.stats.hp)
        self.max_stamina = self.base_max_stamina + round(self.stats.endurance)
        self.max_magic_points = self.base_max_magic_points + round(self.stats.magic_amount)
        self.hp = min(self.hp, self.max_hp)
        self.stamina = min(self.stamina, self.max_stamina)
        self.magic_points = min(self.magic_points, self.max_magic_points)

    def equip_ring(self):
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

    def obtain_excalir(self):
        self.excalir = True
        print("You have obtained the Excalir sword! It does 80 base damage and its damage increases as you lose HP.")

    def block(self):
        # Block reduces incoming damage based on defense stat
        block_value = self.stats.defense * 0.5
        return block_value

    def parry(self):
        # Parry does 50% less damage than regular attack but uses attack stat
        parry_damage = self.stats.strength * 0.5
        return parry_damage

    def update_spell_cooldowns(self):
        for spell in self.spell_cooldowns:
            if self.spell_cooldowns[spell] > 0:
                self.spell_cooldowns[spell] -= 1

