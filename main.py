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
