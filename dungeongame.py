import random

class Stats:
    """
    A class to represent the player's stats.

    Attributes:
    -----------
    strength : int
        The player's strength stat.
    defense : int
        The player's defense stat.
    magic_defense : int
        The player's magic defense stat.
    speed : int
        The player's speed stat.
    magic_power : int
        The player's magic power stat.
    stamina : int
        The player's stamina stat.
    magic_cost : int
        The player's magic cost stat.
    hp : int
        Additional stat for increasing the player's max HP.
    endurance : int
        Additional stat for increasing the player's max stamina.
    magic_amount : int
        Additional stat for increasing the player's max magic points.
    stat_points : int
        Points available for allocation to the player's stats.
    skill_points : int
        Points available for allocation to the player's skills.

    Methods:
    --------
    allocate_stat_points():
        Allows the player to allocate their stat points.
    """

    def __init__(self):
        """Initialize the stats with default values."""
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
        """
        Allows the player to allocate their available stat points to various attributes.
        """
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
    """
    A class to represent the player.

    Attributes:
    -----------
    name : str
        The name of the player.
    level : int
        The level of the player.
    base_max_hp : int
        The base maximum HP of the player.
    base_max_stamina : int
        The base maximum stamina of the player.
    base_max_magic_points : int
        The base maximum magic points of the player.
    hp : int
        The current HP of the player.
    max_hp : int
        The maximum HP of the player.
    base_attack : int
        The base attack value of the player.
    magic : int
        The magic power of the player.
    weapon : int
        The weapon power of the player.
    magic_points : int
        The current magic points of the player.
    max_magic_points : int
        The maximum magic points of the player.
    stamina : int
        The current stamina of the player.
    max_stamina : int
        The maximum stamina of the player.
    burn_duration : int
        The duration of burn status on the player.
    burn_damage : int
        The damage taken each turn due to burn.
    score : int
        The player's score.
    experience : int
        The experience points of the player.
    stats : Stats
        The stats object containing player's attributes.
    inventory : dict
        The inventory of the player, including potions, elixirs, rings, and weapons.
    spells : dict
        A dictionary tracking available spells for the player.
    spell_cooldowns : dict
        A dictionary tracking cooldowns for each spell.
    equipped_rings : dict
        A dictionary tracking the number of combat and magic rings equipped.
    equipped_weapon : str
        The name of the currently equipped weapon.
    excalir : bool
        A flag indicating if the player has obtained the Excalir sword.
    is_shielded : bool
        A flag indicating if the player is shielded.
    shield_turns : int
        The number of turns the shield is active.
    gold : int
        The amount of gold the player has.

    Methods:
    --------
    level_up():
        Handles the player's level up process.
    experience_to_next_level() -> int:
        Calculates the experience points required for the next level.
    gain_experience(amount: int):
        Adds experience points to the player and handles level up if needed.
    update_max_values():
        Updates the player's maximum HP, stamina, and magic points based on stats.
    block() -> float:
        Returns the block value based on the player's defense.
    parry() -> float:
        Returns the parry damage based on the player's strength.
    update_spell_cooldowns():
        Updates the cooldowns for all spells.
    """

    def __init__(self):
        """Initialize the player with default values and stats."""
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
        """
        Handles the player's level-up process, awarding stat points and skill points as appropriate.
        """
        self.level += 1
        self.stats.stat_points += 5
        self.experience -= self.experience_to_next_level()
        if self.level % 5 == 0:
            self.stats.skill_points += 1
        print(f"You leveled up to level {self.level}! You have {self.stats.stat_points} stat points to allocate.")
        self.stats.allocate_stat_points()
        self.update_max_values()

    def experience_to_next_level(self) -> int:
        """
        Calculates the experience points required for the next level.

        Returns:
        --------
        int: The amount of experience needed for the next level.
        """
        return 100 * (1.1 ** (self.level - 1))

    def gain_experience(self, amount: int):
        """
        Adds experience points to the player and handles level up if needed.

        Parameters:
        -----------
        amount : int
            The amount of experience points to add.
        """


        self.experience += amount
        while self.experience >= self.experience_to_next_level():
            self.level_up()

    def update_max_values(self):
        """
        Updates the player's maximum HP, stamina, and magic points based on stats.
        """
        self.max_hp = self.base_max_hp + round(self.stats.hp)
        self.max_stamina = self.base_max_stamina + round(self.stats.endurance)
        self.max_magic_points = self.base_max_magic_points + round(self.stats.magic_amount)
        self.hp = min(self.hp, self.max_hp)
        self.stamina = min(self.stamina, self.max_stamina)
        self.magic_points = min(self.magic_points, self.max_magic_points)

    def block(self) -> float:
        """
        Calculates the block value based on the player's defense.

        Returns:
        --------
        float: The value by which incoming damage is reduced.
        """
        block_value = self.stats.defense * 0.5
        return block_value

    def parry(self) -> float:
        """
        Calculates the parry damage based on the player's strength.

        Returns:
        --------
        float: The damage dealt by a parry.
        """
        parry_damage = self.stats.strength * 0.5
        return parry_damage

    def update_spell_cooldowns(self):
        """
        Reduces the cooldowns for all spells by 1 if they are on cooldown.
        """
        for spell in self.spell_cooldowns:
            if self.spell_cooldowns[spell] > 0:
                self.spell_cooldowns[spell] -= 1

class SpecialAbility:
    """
    A class to represent a special ability.

    Attributes:
    -----------
    name : str
        The name of the special ability.
    effect : function
        The function that defines the effect of the ability.
    cooldown : int, optional
        The number of turns required before the ability can be used again (default is 2).
    current_cooldown : int
        The current number of turns remaining on the cooldown.

    Methods:
    --------
    use(user, target):
        Executes the ability's effect on the target.
    reduce_cooldown():
        Reduces the cooldown of the ability by 1 turn.
    """

    def __init__(self, name, effect, cooldown=2):
        """Initialize the special ability with a name, effect, and cooldown."""
        self.name = name
        self.effect = effect
        self.cooldown = cooldown
        self.current_cooldown = 0

    def use(self, user, target):
        """
        Executes the ability's effect on the target.

        Parameters:
        -----------
        user : object
            The entity using the ability.
        target : object
            The entity being targeted by the ability.
        """
        print(f"{user.name} uses {self.name}!")
        self.effect(user, target)
        self.current_cooldown = self.cooldown

    def reduce_cooldown(self):
        """Reduces the cooldown of the ability by 1 turn."""
        if self.current_cooldown > 0:
            self.current_cooldown -= 1

def fire_breath(user, target):
    """
    A special ability that deals fire damage to the target and applies a burn effect.

    Parameters:
    -----------
    user : object
        The entity using the ability.
    target : object
        The entity being targeted by the ability.
    """
    damage = 20 + user.level * 2
    target.hp -= damage
    target.is_burning = True
    target.burn_duration = 6
    print(f"{target.name} takes {damage} fire damage and is burning!")

def stronger_fire_breath(user, target):
    """
    A stronger version of the fire breath ability, dealing more damage and applying a burn effect.

    Parameters:
    -----------
    user : object
        The entity using the ability.
    target : object
        The entity being targeted by the ability.
    """
    damage = 30 + user.level * 3
    target.hp -= damage
    target.is_burning = True
    target.burn_duration = 6
    print(f"{target.name} takes {damage} fire damage and is burning!")

def ice_shield(user, target):
    """
    A special ability that shields the user from all damage for 2 turns.

    Parameters:
    -----------
    user : object
        The entity using the ability.
    target : object
        The entity being targeted by the ability.
    """
    user.is_shielded = True
    user.shield_turns = 2
    print(f"{user.name} uses Ice Shield and is protected from all damage for 2 turns!")

def ice_lance(user, target):
    """
    A special ability that deals ice damage to the target and applies a freeze effect.

    Parameters:
    -----------
    user : object
        The entity using the ability.
    target : object
        The entity being targeted by the ability.
    """
    damage = 15 + user.level * 1.5
    target.hp -= damage
    target.is_frozen = True
    target.frozen_duration = 3
    print(f"{target.name} takes {damage} ice damage and is frozen for 3 turns!")

def water_heal(user):
    """
    A special ability that heals the user.

    Parameters:
    -----------
    user : object
        The entity using the ability.
    """
    heal_amount = 20 + user.level * 2
    user.hp += heal_amount
    print(f"{user.name} heals for {heal_amount} HP!")

def smash(user, target):
    """
    A basic attack ability that deals physical damage to the target.

    Parameters:
    -----------
    user : object
        The entity using the ability.
    target : object
        The entity being targeted by the ability.
    """
    damage = 10 + user.level * 2
    target.hp -= damage
    print(f"{user.name} smashes {target.name} for {damage} damage!")

def water_nebula(user, target):
    """
    A special ability that deals water damage to the target with a chance to drown them.

    Parameters:
    -----------
    user : object
        The entity using the ability.
    target : object
        The entity being targeted by the ability.
    """
    base_damage = user.level * 2 + 10
    if isinstance(user, Player):
        magic_power = user.stats.magic_power
    else:
        magic_power = user.magic_power
    damage = base_damage + base_damage * 0.05 * magic_power
    target.hp -= max(0, damage)
    print(f"{user.name} casts Water Nebula on {target.name} for {damage} damage.")
    if random.random() < 0.3:
        target.is_drowned = True  # 30% chance to drown
        target.drowned_duration = 3  # Drown lasts for 3 turns
        print(f"{target.name} is drowned and unable to move for one turn!")

class Monster:
    """
    A class to represent a monster in the dungeon.

    Attributes:
    -----------
    name : str
        The name of the monster.
    level : int
        The level of the monster.
    hp : int
        The current HP of the monster.
    attack : int
        The attack value of the monster.
    magic_power : int
        The magic power of the monster.
    abilities : list
        A list of special abilities the monster can use.
    is_frozen : bool
        A flag indicating if the monster is frozen.
    frozen_duration : int
        The number of turns the monster remains frozen.
    is_burning : bool
        A flag indicating if the monster is burning.
    burn_duration : int
        The number of turns the monster remains burning.
    is_poisoned : bool
        A flag indicating if the monster is poisoned.
    poison_duration : int
        The number of turns the monster remains poisoned.
    is_shielded : bool
        A flag indicating if the monster is shielded.
    shield_turns : int
        The number of turns the shield is active.
    is_drowned : bool
        A flag indicating if the monster is drowned.
    drowned_duration : int
        The number of turns the monster remains drowned.
    immune_to_fire : bool
        A flag indicating if the monster is immune to fire.
    experience : int
        The amount of experience points the monster gives when defeated.
    gold : int
        The amount of gold the monster drops when defeated.

    Methods:
    --------
    take_turn(player):
        Handles the monster's turn in combat.
    reduce_abilities_cooldown():
        Reduces the cooldowns of the monster's abilities.
    """

    def __init__(self, name, level, base_hp, base_attack, abilities=None, immune_to_fire=False, gold=0):
        """Initialize the monster with its name, level, base stats, abilities, and resistances."""
        self.name = name
        self.level = level
        self.hp = base_hp + random.randint(-10, 10)  # Randomize HP within a range
        self.attack = base_attack + random.randint(-2, 2)  # Randomize attack within a range
        self.magic_power = level * 2  # Simplified magic power based on level
        self.abilities = abilities if abilities else []
        self.is_frozen = False
        self.frozen_duration = 0
        self.is_burning = False
        self.burn_duration = 0
        self.is_poisoned = False
        self.poison_duration = 0
        self

        self.is_shielded = False
        self.shield_turns = 0
        self.is_drowned = False
        self.drowned_duration = 0
        self.immune_to_fire = immune_to_fire
        self.experience = self.level * 20  # Experience proportional to monster level
        self.gold = gold  # Gold dropped by the monster

    def take_turn(self, player):
        """
        Handles the monster's turn in combat, including attack, special abilities, and status effects.

        Parameters:
        -----------
        player : Player
            The player object representing the hero.
        """
        if self.is_frozen:
            print(f"{self.name} is frozen and cannot move this turn.")
            self.frozen_duration -= 1
            if self.frozen_duration <= 0:
                self.is_frozen = False
            return

        if self.shield_turns > 0:
            print(f"{self.name} is shielded and cannot attack this turn.")
            self.shield_turns -= 1
            if self.shield_turns <= 0:
                self.is_shielded = False
            return

        if self.is_drowned:
            print(f"{self.name} is drowned and cannot move this turn.")
            self.drowned_duration -= 1
            if self.drowned_duration <= 0:
                self.is_drowned = False
            return

        action = random.choice(['attack', 'special'])
        if action == 'attack':
            damage = self.attack * (1 + self.level * 0.02)
            if player.is_shielded:
                print(f"{player.name} is shielded and takes no damage.")
            else:
                player.hp -= damage
                print(f"{self.name} attacks {player.name} for {damage} damage.")
        elif action == 'special' and self.abilities:
            available_abilities = [ability for ability in self.abilities if ability.current_cooldown == 0]
            if available_abilities:
                ability = random.choice(available_abilities)
                ability.use(self, player)

        if self.is_burning:
            burn_damage = 5 + self.level
            self.hp -= burn_damage
            self.burn_duration -= 1
            print(f"{self.name} takes {burn_damage} burn damage.")
            if self.burn_duration <= 0:
                self.is_burning = False

        if self.is_poisoned:
            poison_damage = 3 + self.level
            self.hp -= poison_damage
            self.poison_duration -= 1
            print(f"{self.name} takes {poison_damage} poison damage.")
            if self.poison_duration <= 0:
                self.is_poisoned = False

        if self.hp <= 0:
            print(f"{self.name} is defeated!")

    def reduce_abilities_cooldown(self):
        """Reduces the cooldowns of the monster's abilities by 1 turn."""
        for ability in self.abilities:
            ability.reduce_cooldown()

class Dungeon:
    """
    A class to represent the dungeon and manage the game flow.

    Attributes:
    -----------
    player : Player
        The player object representing the hero.
    turn : int
        The current turn number in the dungeon.

    Methods:
    --------
    dungeoncombat(monster: Monster, floor: int) -> bool:
        Manages the combat between the player and a monster.
    reset_cooldowns():
        Resets all spell cooldowns for the player.
    flee() -> bool:
        Determines whether the player successfully flees from combat.
    get_available_spells() -> list:
        Returns a list of available spells the player can cast.
    cast_spell(spell_name: str, monster: Monster):
        Casts a spell against the target monster.
    use_inventory():
        Handles the player's interaction with their inventory.
    apply_potion_effect(potion: str):
        Applies the effect of a potion to the player.
    replenish_resources():
        Replenishes a portion of the player's stamina and magic points after combat.
    display_stats():
        Displays the player's current stats.
    collect_loot():
        Handles the loot collection process after defeating a monster.
    generate_rare_loot():
        Generates and awards a rare loot item to the player.
    check_inventory_limit():
        Checks if the player's inventory exceeds the limit and prompts to replace an item if necessary.
    replace_item_prompt():
        Prompts the player to replace an item in their inventory when the limit is exceeded.
    dungeonmonster(floor: int) -> Monster:
        Generates a monster based on the current dungeon floor.
    clear_floor(floor: int):
        Handles actions after clearing a floor, including experience and loot rewards.
    add_potion_to_inventory(potion: str):
        Adds a potion to the player's inventory.
    dungeonconquered():
        Displays a message when the player conquers the dungeon.
    dungeonpuzzle():
        Handles a puzzle room encounter in the dungeon.
    grant_reward():
        Grants a reward to the player after solving a puzzle.
    learn_fire_magic():
        Teaches the player the Fireball spell.
    learn_water_magic():
        Teaches the player the Water Nebula spell.
    learn_ice_magic():
        Teaches the player the Frostbite and Ice Lance spells.
    play_game():
        Manages the main game loop, including floor progression and encounters.
    mother_dragon_boss() -> bool:
        Handles the encounter with the Mother Dragon boss.
    summon_baby_dragon(mother_dragon: Monster):
        Summons a Baby Dragon to assist the Mother Dragon boss.
    leviant_boss() -> bool:
        Handles the encounter with the Leviant boss on the final floor.
    merida_shop():
        Manages the interaction with Merida's shop where the player can buy items.
    """

    ACTIONS = {
        'regular': [
            '1: Attack with Weapon',
            '2: Attack with Magic',
            '3: Inventory',
            '4: Stats',
            '5: Flee',
            '6: Block',
            '7: Parry'
        ],
        'with_excalir': [
            '1: Attack with Excalir',
            '2: Esmera Slash',
            '3: Attack with Magic',
            '4: Inventory',
            '5: Stats',
            '6: Flee',
            '7: Block',
            '8: Parry'
        ]
    }

    def __init__(self):
        """Initialize the dungeon with a player and starting turn count."""
        self.player = Player()
        self.turn = 0

    def dungeoncombat(self, monster: Monster, floor: int) -> bool:
        """
        Manages the combat between the player and a monster.

        Parameters:
        -----------
        monster : Monster
            The monster the player is fighting.
        floor : int
            The current floor number in the dungeon.

        Returns:
        --------
        bool: True if the player wins the combat, False if the player is defeated or flees.
        """
        print(f"==Combat with {monster.name}==")
        while self.player.hp > 0 and monster.hp > 0:
            self.turn += 1
            self.player.update_spell_cooldowns()
            print(f"\nTurn {self.turn}:")
            print(f"Player HP: {round(self.player.hp, 2)}/{self.player.max_hp} | Monster HP: {monster.hp}")
            print(f"Player MP: {round(self.player.magic_points, 2)}/{self.player.max_magic_points} | Player Stamina: {self.player.stamina}/{self.player.max_stamina}")

            # player's turn
            actions = self.ACTIONS['with_excalir'] if self.player.excalir else self.ACTIONS['regular']
            for action in actions:
                print(action)
            player_action = input("Choose action: ")

            if player_action == '1' and self.player.stamina >= 5:
                # Attack with Weapon or Excalir
                self.player.stamina -= 5
                if self.player.excalir:
                    damage = 80 * (1 + self.player.stats.strength / 100)
                    if self.player.hp <= 25:
                        damage *= 1.5  # True form of Excalir
                    else:
                        damage *= 1 + (100 - self.player.hp) // 25 * 0.05
                else:
                    damage = self.player.base_attack
                monster.hp -= max(0, damage)
                print(f"Player attacks {monster.name} with weapon for {damage} damage.")
            elif player_action == '2' and self.player.excalir:
                if self.player.spell_cooldowns['esmera_slash'] == 0:
                    # Esmera Slash
                    damage = 80 * (1 + self.player.stats.strength / 100) * 2
                    monster.hp -= max(0, damage)
                    print(f"Player uses Esmera Slash on {monster.name} for {damage} damage.")
                    self.player.spell_cooldowns['esmera_slash'] = 4
                else:
                    print("Esmera Slash is on cooldown.")
            elif (player_action == '2' and not self.player.excalir) or (player_action == '3' and self.player.excalir):
                if self.player.magic_points >= 5 and self.player.stamina >= 5:
                    # Attack with Magic
                    self.player.stamina -= 5
                    magic_cost = 5 - 0.5 * self.player.equipped_rings['magic']
                    if self.player.magic_points >= magic_cost:
                        self.player.magic_points -= magic_cost
                        available_spells = self.get_available_spells()
                        if available_spells:
                            print(f"Available spells: {','.join([f'{i+1}: {spell}' for i, spell in enumerate(available_spells)])}")
                            try:
                                spell_choice = int(input("Choose a spell: ")) - 1
                                if 0 <= spell_choice < len(available_spells):
                                    spell_name = available_spells[spell_choice]
                                    self.cast_spell(spell_name, monster)
                                else:
                                    print("Invalid spell choice.")
                            except ValueError:
                                print("Invalid input. Please enter a valid number.")
                        else:
                            print("You have no spells available.")
                    else:
                        print("Not enough magic points.")
                else:
                    print("Not enough stamina to attack with magic.")
            elif (player_action == '3' and not self.player.excalir) or (player_action == '4' and self.player.excalir):
                # Inventory
                self.use_inventory()
            elif (player_action == '4' and not self.player.excalir) or (player_action == '5' and self.player.excalir):
                # Stats breakdown
                self.display_stats()
            elif (player_action == '5' and not self.player.excalir) or (player_action == '6' and self.player.excalir):
                # Flee
                if self.flee():
                    print("You successfully fled the combat.")
                    return False
                else:
                    print("Failed to flee.")
            elif (player_action == '6' and not self.player.excalir) or (player_action == '7' and self.player.excalir):
                # Block
                block_value = self.player.block()
                print(f"Player blocks, reducing incoming damage by {block_value}.")
            elif (player_action == '7' and not self.player.excalir) or (player_action == '8' and self.player.excalir):
                # Parry
                if self.player.stamina >= 5:
                    self.player.stamina -= 5
                    parry_damage = self.player.parry()
                    monster.hp -= max(0, parry_damage)
                    print(f"Player parries and counters with {parry_damage} damage.")
                else:
                    print("Not enough stamina to parry.")
            else:
                print("Invalid action or not enough magic points/stamina.")

            # Monster takes its turn after player's action, unless combat ends
            if monster.hp > 0:
                monster.take_turn(self.player)
                monster.reduce_abilities_cooldown()

            if self.player.hp <= 0:
                print("Player is defeated!")
                return False

        if monster.hp <= 0:
            self.player.gain_experience(monster.experience)
            self.player.gold += monster.gold
            print(f"Player gains {monster.experience} experience points and {monster.gold} gold!")
            self.replenish_resources()
            self.reset_cooldowns()
            return True

    def reset_cooldowns(self):
        """Resets all spell cooldowns for the player."""
        for spell in self.player.spell_cooldowns:
            self.player.spell_cooldowns[spell] = 0

    def flee(self) -> bool:
        """
        Determines whether the player successfully flees from combat.

        Returns:
        --------
        bool: True if the player successfully flees, False otherwise.
        """
        flee_chance = 0.5  # 50% chance to flee
        return random.random() < flee_chance

    def get_available_spells(self) -> list:
        """
        Returns a list of available spells the player can cast.

        Returns:
        --------
        list: A list of spell names available for casting.
        """
        return [spell for spell, available in self.player.spells.items() if available and self.player.spell_cooldowns[spell] == 0]

    def cast_spell(self, spell_name: str, monster: Monster):
        """
        Casts a spell against the target monster.

        Parameters:
        -----------
        spell_name : str
            The name of the spell to cast.
        monster : Monster
            The target monster.
        """
        if spell_name == 'fireball':
            if monster.immune_to_fire:
                print(f"Player casts Fireball on {monster.name} but it is immune to fire!")
            else:
                base_damage = self.player.magic * (1 + self.player.stats.magic_power / 100)
                damage = base_damage + base_damage * 0.05 * self.player.equipped_rings['magic']
                monster.hp -= max(0, damage)
                print(f"Player casts Fireball on {monster.name} for {damage} damage.")
                # 30% chance to cause burn damage
                if random.random() < 0.3:
                    monster.is_burning = True
                    monster.burn_duration = 6  # Burn lasts for 6 turns
                    monster.burn_damage = 5 + self.player.stats.magic_power  # Burn does additional damage per turn
                    print(f"{monster.name} is now burning!")
                else:
                    print("The Fireball did not cause a burn effect.")
        elif spell_name == 'water_nebula':
            water_nebula(self.player, monster)
        elif spell_name == 'frostbite':
            base_damage = 20
            damage = base_damage + base_damage * 0.05 * self.player.equipped_rings['magic']
            if 'Dragon' in monster.name:
                damage *= 2  # Double damage to dragons
            monster.hp -= max(0, damage)
            print(f"Player casts Frostbite on {monster.name} for {damage} damage.")
            # Apply freeze effect
            monster.is_frozen = True
            monster.frozen_duration = 3
            print(f"{monster.name} is frozen and cannot move for the next turn.")
        elif spell_name == 'ice_lance':
            ice_lance(self.player, monster)

        # Set cooldown for the used spell
        self.player.spell_cooldowns[spell_name] = 2  # Spell cannot be used for 1 turn

    def use_inventory(self):
        """Handles the player's interaction with their inventory."""
        print("== Inventory ==")
        print("1: Equip Ring")
        print("2: Equip Weapon")
        for i, (item, count) in enumerate(self.player.inventory['potions'].items()):
            print(f"{i + 3}: {item} x{count}")

        try:
            choice = int(input("Choose an inventory option: ")) - 1
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        if choice == 0:
            self.player.equip_ring()
        elif choice == 1:
            self.player.equip_weapon()
        elif 2 <= choice < 2 + len(self.player.inventory['potions']):
            potion = list(self.player.inventory['potions'].keys())[choice - 2]
            self.apply_potion_effect(potion)
        else:
            print("Invalid choice.")

    def apply_potion_effect(self, potion: str):
        """
        Applies the effect of a potion to the player.

        Parameters:
        -----------
        potion : str
            The name of the potion being used.
        """
        if potion == 'Health Potion':
            self.player.hp = min(self.player.hp + 50, self.player.max_hp)
            print("You used a Health Potion and restored 50 HP.")
        elif potion == 'Stamina Potion':
            self.player.stamina = min(self.player.stamina + 50, self.player.max_stamina)
            print("You used a Stamina Potion and restored 50 Stamina.")
        elif potion == 'Magic Elixir':
            self.player.magic_points = min(self.player.magic_points + 40, self.player.max_magic_points)
            print("You used a Magic Elixir and restored 40 Magic Points.")
        elif potion == 'Status Nullifying Potion':
            self.player.burn_duration = 0
            self.player.is_burning = False
            self.player.frozen_duration = 0
            self.player.is_frozen = False
            print("You used a Status Nullifying Potion and nullified all status effects.")
        elif potion == 'Strength Potion':
            self.player.stats.strength += 10
            print("You used a Strength Potion and increased your strength by 10.")

        # Remove one potion from inventory
        self.player.inventory['potions'][potion] -= 1
        if self.player.inventory['potions'][potion] == 0:
            del self.player.inventory['potions'][potion]

    def replenish_resources(self):
        """Replenishes a portion of the player's stamina and magic points after combat."""
        self.player.stamina = min(self.player.stamina + 10, self.player.max_stamina)
        self.player.magic_points = min(self.player.magic_points + 10, self.player.max_magic_points)
        print(f"You have replenished 10 Stamina and 10 Magic Points after the fight. Current Stamina: {self.player.stamina}/{self.player.max_stamina}, Current Magic Points: {self.player.magic_points}/{self.player.max_magic_points}")

    def display_stats(self):
        """Displays the player's current stats."""
        print("== Player Stats ==")
        print(f"HP: {self.player.hp}/{self.player.max_hp}")
        print(f"MP: {self.player.magic_points}/{self.player.max_magic_points}")
        print(f"Stamina: {self.player.stamina}/{self.player.max_stamina}")
        print(f"Level: {self.player.level}")
        print(f"Strength: {self.player.stats.strength}")
        print(f"Defense: {self.player.stats.defense}")
        print(f"Magic Defense: {self.player.stats.magic_defense}")
        print(f"Speed: {self.player.stats.speed}")
        print(f"Magic Power: {self.player.stats.magic_power}")
        print(f"Stamina: {self.player.stats.stamina}")
        print(f"Magic Cost: {self.player.stats.magic_cost}")
        print(f"HP: {self.player.stats.hp}")
        print(f"Endurance: {self.player.stats.endurance}")
        print(f"Magic Amount: {self.player.stats.magic_amount}")
        print(f"Combat Rings Equipped: {self.player.equipped_rings['combat']}")
        print(f"Magic Rings Equipped: {self.player.equipped_rings['magic']}")
        print(f"Gold: {self.player.gold}")
        input("Press Enter to return to combat...")

    def collect_loot(self):
        """Handles the loot collection process after defeating a monster."""
        loot_chance = random.random()
        if loot_chance < 0.1:
            print("You have found a rare item!")
            self.generate_rare_loot()
        elif loot_chance < 0.9:
            num_potions = random.choices([1, 2, 3], weights=[0.6, 0.3, 0.1])[0]
            for _ in range(num_potions):
                potion = random.choice(['Health Potion', 'Stamina Potion', 'Magic Elixir', 'Strength Potion', 'Status Nullifying Potion'])
                if potion in self.player.inventory['potions']:
                    self.player.inventory['potions'][potion] += 1
                else:
                    self.player.inventory['potions'][potion] = 1
                print(f"Found {potion}!")
        else:
            ring_type = random.choice(['Combat Ring', 'Magic Ring'])
            self.player.inventory['rings'].append(ring_type)
            print(f"Found {ring_type}!")

        self.check_inventory_limit()

    def generate_rare_loot(self):
        """Generates and awards a rare loot item to the player."""
        rare_loots = [
            {"name": "Sword of Flames", "effect": "Adds fire damage to attacks"},
            {"name": "Shield of Aegis", "effect": "Increases defense by 10"},
            {"name": "Potion of Strength", "effect": "Temporarily increases strength by 5"},
            {"name": "Cloak of Invisibility", "effect": "Grants a chance to evade attacks"},
            {"name": "Ring of Regeneration", "effect": "Restores 5 HP per turn"}
        ]
        rare_loot = random.choice(rare_loots)
        print(f"Found rare item: {rare_loot['name']} - {rare_loot['effect']}")
        # Add logic to add rare item to player's inventory

    def check_inventory_limit(self):
        """Checks if the player's inventory exceeds the limit and prompts to replace an item if necessary."""
        total_items = sum(self.player.inventory['potions'].values()) + len(self.player.inventory['rings']) + len(self.player.inventory['weapons'])
        if total_items > 10:
            print("Your inventory is full. You must replace an item.")
            self.replace_item_prompt()

    def replace_item_prompt(self):
        """Prompts the player to replace an item in their inventory when the limit is exceeded."""
        print("Choose an item to replace:")
        inventory_items = list(self.player.inventory['potions'].items()) + \
                          [(f"Ring: {item}", 1) for item in self.player.inventory['rings']] + \
                          [(f"Weapon: {item}", 1) for item in self.player.inventory['weapons']]
        for i, (item, count) in enumerate(inventory_items):
            print(f"{i + 1}: {item} x{count}")

        try:
            choice = int(input("Choose an item to replace: ")) - 1
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        if 0 <= choice < len(inventory_items):
            item_name, count = inventory_items[choice]
            if "Potion" in item_name:
                potion_type = item_name.split(": ")[1]
                del self.player.inventory['potions'][potion_type]
            elif "Ring" in item_name:
                ring_type = item_name.split(": ")[1]
                self.player.inventory['rings'].remove(ring_type)
            elif "Weapon" in item_name:
                weapon_type = item_name.split(": ")[1]
                self.player.inventory['weapons'].remove(weapon_type)
            print(f"Replaced {item_name}.")
        else:
            print("Invalid choice.")

    def dungeonmonster(self, floor: int) -> Monster:
        """
        Generates a monster based on the current dungeon floor.

        Parameters:
        -----------
        floor : int
            The current floor number in the dungeon.

        Returns:
        --------
        Monster: A monster object with attributes adjusted for the floor level.
        """
        if random.random() < 0.1:
            monster = Monster("Dragon", floor, 80, 10, abilities=[SpecialAbility("Fire Breath", fire_breath)], immune_to_fire=True, gold=400)
        elif random.random() < 0.1:
            monster = Monster("Ice Wraith", floor, 60, 8, abilities=[SpecialAbility("Ice Shield", ice_shield), SpecialAbility("Ice Lance", ice_lance)], gold=100)
        elif random.random() < 0.1:
            monster = Monster("Water Nymph", floor, 70, 9, abilities=[SpecialAbility("Water Nebula", water_nebula), SpecialAbility("Water Heal", lambda user, target: water_heal(user))], gold=100)
        else:
            monsters = [
                Monster("Goblin", floor, 30, 5, abilities=[SpecialAbility("Slash", smash)], gold=50),
                Monster("Orc", floor, 50, 7, abilities=[SpecialAbility("Smash", smash)], gold=40)
            ]
            monster = random.choice(monsters)
        monster.hp = int(monster.hp * (1 + 0.02 * floor))
        monster.attack = int(monster.attack * (1 + 0.02 * floor))
        return monster

    def clear_floor(self, floor: int):
        
        """
        Handles actions after clearing a floor, including experience and loot rewards.

        Parameters:
        -----------
        floor : int
            The current floor number in the dungeon.
        """
        
        self.player.score += 1
        input(f"You cleared floor {floor}. Press Enter to continue traversing the dungeon.")
        self.player.gain_experience(100)
        self.player.gold += 100
        print("You received 100 gold for clearing the floor.")
        self.add_potion_to_inventory('Health Potion')
        self.add_potion_to_inventory('Magic Elixir')
        print("You received a Health Potion and a Magic Elixir for clearing the floor.")

    def add_potion_to_inventory(self, potion: str):
        """
        Adds a potion to the player's inventory.

        Parameters:
        -----------
        potion : str
            The name of the potion to add.
        """
        if potion in self.player.inventory['potions']:
            self.player.inventory['potions'][potion] += 1
        else:
            self.player.inventory['potions'][potion] = 1

    def dungeonconquered(self):
        """Displays a message when the player conquers the dungeon."""
        print("Congratulations! You have conquered the dungeon!")
        print(f"Your final score is: {self.player.score}")
        # Implement additional reward logic here

    def dungeonpuzzle(self):
        """Handles a puzzle room encounter in the dungeon."""
        print("== You have encountered a puzzle room! ==")
        print("Solve the puzzle to earn a reward.")
        number_to_guess = random.randint(1, 10)
        attempts = 3
        while attempts > 0:
            try:
                guess = int(input(f"Guess the number (1-10), {attempts} attempts remaining: "))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 10.")
                continue

            if 1 <= guess <= 10:
                if guess == number_to_guess:
                    print("Correct! You have solved the puzzle.")
                    self.grant_reward()
                    return
                else:
                    print("Incorrect guess.")
                attempts -= 1
            else:
                print("Invalid input. Please enter a number between 1 and 10.")
        print("You failed to solve the puzzle. No reward this time.")

    def grant_reward(self):
        """Grants a reward to the player after solving a puzzle."""
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
        """Teaches the player the Fireball spell."""
        self.player.spells['fireball'] = True
        self.player.spell_cooldowns['fireball'] = 0
        print("You have learned the Fireball spell!")

    def learn_water_magic(self):
        """Teaches the player the Water Nebula spell."""
        self.player.spells['water_nebula'] = True
        self.player.spell_cooldowns['water_nebula'] = 0
        print("You have learned the Water Nebula spell!")

    def learn_ice_magic(self):
        """Teaches the player the Frostbite and Ice Lance spells."""
        self.player.spells['frostbite'] = True
        self.player.spell_cooldowns['frostbite'] = 0
        self.player.spells['ice_lance'] = True
        self.player.spell_cooldowns['ice_lance'] = 0
        print("You have learned the Frostbite and Ice Lance spells!")

    def play_game(self):
        """Manages the main game loop, including floor progression and encounters."""
        for floor in range(1, 51):
            print(f"\n== Floor {floor} ==")
            if floor % 10 == 0:
                self.dungeonpuzzle()
            elif floor % 13 == 0:
                self.merida_shop()
            elif floor % 22 == 0:
                self.mother_dragon_boss()
            else:
                encounter_prob = 0.3 + 0.1 * (floor % 10)  # Increase encounter probability with each floor in the set of 10
                encounters = 0
                while random.random() < encounter_prob and encounters < 3:  # Limit encounters to 3 per floor
                    encounters += 1
                    monster = self.dungeonmonster(floor)
                    if not self.dungeoncombat(monster, floor):
                        print("Game Over!")
                        return
            self.clear_floor(floor)

        self.leviant_boss()
        self.dungeonconquered()

    def mother_dragon_boss(self) -> bool:
        
        """
        Handles the encounter with the Mother Dragon boss.

        Returns:
        --------
        bool: True if the player wins the combat, False if the player is defeated.
        """
        
        print("== You have encountered a Mother Dragon! ==")
        mother_dragon = Monster("Mother Dragon", 50, 300, 35, abilities=[SpecialAbility("Stronger Fire Breath", stronger_fire_breath), SpecialAbility("Summon Baby Dragon", lambda user, target: self.summon_baby_dragon(user))], immune_to_fire=True, gold=1000)
        while self.player.hp > 0 and mother_dragon.hp > 0:
            self.turn += 1
            print(f"\nTurn {self.turn}:")
            print(f"Player HP: {self.player.hp} | Mother Dragon HP: {mother_dragon.hp}")
            print(f"Player MP: {self.player.magic_points} | Player Stamina: {self.player.stamina}")

            actions = self.ACTIONS['with_excalir'] if self.player.excalir else self.ACTIONS['regular']
            for action in actions:
                print(action)
            player_action = input("Choose action: ")

            if player_action == '1' and self.player.stamina >= 5:
                # Attack with Weapon or Excalir
                self.player.stamina -= 5
                damage = self.player.base_attack * (1 + self.player.stats.strength / 100)
                if self.player.excalir:
                    damage = 80 * (1 + self.player.stats.strength / 100)
                    if self.player.hp <= 25:
                        damage *= 1.5  # True form of Excalir
                    else:
                        damage *= 1 + (100 - self.player.hp) // 25 * 0.05
                mother_dragon.hp -= max(0, damage)
                print(f"Player attacks Mother Dragon with weapon for {damage} damage.")
            elif player_action == '2' and self.player.excalir:
                if self.player.spell_cooldowns['esmera_slash'] == 0:
                    # Esmera Slash
                    damage = 80 * (1 + self.player.stats.strength / 100) * 2
                    mother_dragon.hp -= max(0, damage)
                    print(f"Player uses Esmera Slash on {mother_dragon.name} for {damage} damage.")
                    self.player.spell_cooldowns['esmera_slash'] = 4
                else:
                    print("Esmera Slash is on cooldown.")
            elif (player_action == '2' and not self.player.excalir) or (player_action == '3' and self.player.excalir):
                if self.player.magic_points >= 5 and self.player.stamina >= 5:
                    # Attack with Magic
                    self.player.stamina -= 5
                    magic_cost = 5 - 0.5 * self.player.equipped_rings['magic']
                    if self.player.magic_points >= magic_cost:
                        self.player.magic_points -= magic_cost
                        available_spells = self.get_available_spells()
                        if available_spells:
                            print(f"Available spells: {', '.join([f'{i+1}: {spell}' for i, spell in enumerate(available_spells)])}")
                            spell_choice = int(input("Choose a spell: ")) - 1
                            if 0 <= spell_choice < len(available_spells):
                                spell_name = available_spells[spell_choice]
                                self.cast_spell(spell_name, mother_dragon)
                            else:
                                print("Invalid spell choice.")
                        else:
                            print("You have no spells available.")
                    else:
                        print("Not enough magic points.")
                else:
                    print("Not enough stamina to attack with magic.")
            elif (player_action == '3' and not self.player.excalir) or (player_action == '4' and self.player.excalir):
                # Inventory
                self.use_inventory()
            elif (player_action == '4' and not self.player.excalir) or (player_action == '5' and self.player.excalir):
                # Stats breakdown
                self.display_stats()
            elif (player_action == '5' and not self.player.excalir) or (player_action == '6' and self.player.excalir):
                # Flee
                if self.flee():
                    print("You successfully fled the combat.")
                    return False
                else:
                    print("Failed to flee.")
            elif (player_action == '6' and not self.player.excalir) or (player_action == '7' and self.player.excalir):
                # Block
                block_value = self.player.block()
                print(f"Player blocks, reducing incoming damage by {block_value}.")
            elif (player_action == '7' and not self.player.excalir) or (player_action == '8' and self.player.excalir):
                # Parry
                if self.player.stamina >= 5:
                    self.player.stamina -= 5
                    parry_damage = self.player.parry()
                    mother_dragon.hp -= max(0, parry_damage)
                    print(f"Player parries and counters with {parry_damage} damage.")
                else:
                    print("Not enough stamina to parry.")
            else:
                print("Invalid action or not enough magic points/stamina.")

            mother_dragon.take_turn(self.player)
            mother_dragon.reduce_abilities_cooldown()

            if self.player.hp <= 0:
                print("Player is defeated!")
                return False

        return True

    def summon_baby_dragon(self, mother_dragon: Monster):
        
        """
        Summons a Baby Dragon to assist the Mother Dragon boss.

        Parameters:
        -----------
        mother_dragon : Monster
            The Mother Dragon boss monster.
        """
        
        baby_dragon = Monster("Baby Dragon", mother_dragon.level, 100, 15, abilities=[SpecialAbility("Fire Breath", fire_breath)], immune_to_fire=True, gold=0)
        baby_dragon.take_turn(self.player)

    def leviant_boss(self) -> bool:
        
        """
        Handles the encounter with the Leviant boss on the final floor.

        Returns:
        --------
        bool: True if the player wins the combat, False if the player is defeated.
        """
        
        print("== You have reached floor 50 and encountered Leviant, the powerful plant creature! ==")
        leviant = Monster("Leviant", 50, 200, 25, abilities=[SpecialAbility("Poison Spit", smash), SpecialAbility("Regenerate", lambda user, target: water_heal(user))], gold=800)
        while self.player.hp > 0 and leviant.hp > 0:
            self.turn += 1
            print(f"\nTurn {self.turn}:")
            print(f"Player HP: {self.player.hp} | Leviant HP: {leviant.hp}")
            print(f"Player MP: {self.player.magic_points} | Player Stamina: {self.player.stamina}")

            actions = self.ACTIONS['with_excalir'] if self.player.excalir else self.ACTIONS['regular']
            for action in actions:
                print(action)
            player_action = input("Choose action: ")

            if player_action == '1' and self.player.stamina >= 5:
                # Attack with Weapon or Excalir
                self.player.stamina -= 5
                damage = self.player.base_attack * (1 + self.player.stats.strength / 100)
                if self.player.excalir:
                    damage = 80 * (1 + self.player.stats.strength / 100)
                    if self.player.hp <= 25:
                        damage *= 1.5  # True form of Excalir
                    else:
                        damage *= 1 + (100 - self.player.hp) // 25 * 0.05
                leviant.hp -= max(0, damage)
                print(f"Player attacks Leviant with weapon for {damage} damage.")
            elif player_action == '2' and self.player.excalir:
                if self.player.spell_cooldowns['esmera_slash'] == 0:
                    # Esmera Slash
                    damage = 80 * (1 + self.player.stats.strength / 100) * 2
                    leviant.hp -= max(0, damage)
                    print(f"Player uses Esmera Slash on {leviant.name} for {damage} damage.")
                    self.player.spell_cooldowns['esmera_slash'] = 4
                else:
                    print("Esmera Slash is on cooldown.")
            elif (player_action == '2' and not self.player.excalir) or (player_action == '3' and self.player.excalir):
                if self.player.magic_points >= 5 and self.player.stamina >= 5:
                    # Attack with Magic
                    self.player.stamina -= 5
                    magic_cost = 5 - 0.5 * self.player.equipped_rings['magic']
                    if self.player.magic_points >= magic_cost:
                        self.player.magic_points -= magic_cost
                        available_spells = self.get_available_spells()
                        if available_spells:
                            print(f"Available spells: {', '.join([f'{i+1}: {spell}' for i, spell in enumerate(available_spells)])}")
                            spell_choice = int(input("Choose a spell: ")) - 1
                            if 0 <= spell_choice < len(available_spells):
                                spell_name = available_spells[spell_choice]
                                self.cast_spell(spell_name, leviant)
                            else:
                                print("Invalid spell choice.")
                        else:
                            print("You have no spells available.")
                    else:
                        print("Not enough magic points.")
                else:
                    print("Not enough stamina to attack with magic.")
            elif (player_action == '3' and not self.player.excalir) or (player_action == '4' and self.player.excalir):
                # Inventory
                self.use_inventory()
            elif (player_action == '4' and not self.player.excalir) or (player_action == '5' and self.player.excalir):
                # Stats breakdown
                self.display_stats()
            elif (player_action == '5' and not self.player.excalir) or (player_action == '6' and self.player.excalir):
                # Flee
                if self.flee():
                    print("You successfully fled the combat.")
                    return False
                else:
                    print("Failed to flee.")
            elif (player_action == '6' and not self.player.excalir) or (player_action == '7' and self.player.excalir):
                # Block
                block_value = self.player.block()
                print(f"Player blocks, reducing incoming damage by {block_value}.")
            elif (player_action == '7' and not self.player.excalir) or (player_action == '8' and self.player.excalir):
                # Parry
                if self.player.stamina >= 5:
                    self.player.stamina -= 5
                    parry_damage = self.player.parry()
                    leviant.hp -= max(0, parry_damage)
                    print(f"Player parries and counters with {parry_damage} damage.")
                else:
                    print("Not enough stamina to parry.")
            else:
                print("Invalid action or not enough magic points/stamina.")

            leviant.take_turn(self.player)
            leviant.reduce_abilities_cooldown()

            if self.player.hp <= 0:
                print("Player is defeated!")
                return False

            if leviant.hp <= 0:
                self.player.gain_experience(leviant.experience)
                self.player.gold += leviant.gold
                print(f"Player gains {leviant.experience} experience points and {leviant.gold} gold!")
                self.replenish_resources()
                self.reset_cooldowns()
                return True

        return True

    def merida_shop(self):
        """Manages the interaction with Merida's shop where the player can buy items."""
        
        print("Welcome to Merida's Dungeon Shop! Here you can buy items to aid you in your journey.")
        print("1. Buy Health Potion (50 gold)")
        print("2. Buy Stamina Potion (50 gold)")
        print("3. Buy Magic Elixir (50 gold)")
        print("4. Buy Strength Potion (100 gold)")
        print("5. Buy Status Nullifying Potion (100 gold)")
        print("6. Buy Iron Sword (200 gold)")
        print("7. Buy Steel Sword (400 gold)")
        print("8. Buy Adventurer's Armor (300 gold)")
        print("9. Buy Steel Armor (600 gold)")
        print("10. Buy Scepter's Eye (500 gold)")
        print("11. Buy Magic Book (Reflect Spell) (700 gold)")
        print(f"You have {self.player.gold} gold.")

        choice = int(input("Choose an item to buy: "))

        if choice == 1 and self.player.gold >= 50:
            self.add_potion_to_inventory('Health Potion')
            self.player.gold -= 50
            print("You bought a Health Potion.")
        elif choice == 2 and self.player.gold >= 50:
            self.add_potion_to_inventory('Stamina Potion')
            self.player.gold -= 50
            print("You bought a Stamina Potion.")
        elif choice == 3 and self.player.gold >= 50:
            self.add_potion_to_inventory('Magic Elixir')
            self.player.gold -= 50
            print("You bought a Magic Elixir.")
        elif choice == 4 and self.player.gold >= 100:
            self.add_potion_to_inventory('Strength Potion')
            self.player.gold -= 100
            print("You bought a Strength Potion.")
        elif choice == 5 and self.player.gold >= 100:
            self.add_potion_to_inventory('Status Nullifying Potion')
            self.player.gold -= 100
            print("You bought a Status Nullifying Potion.")
        elif choice == 6 and self.player.gold >= 200:
            self.player.inventory['weapons'].append('Iron Sword')
            self.player.gold -= 200
            print("You bought an Iron Sword.")
        elif choice == 7 and self.player.gold >= 400:
            self.player.inventory['weapons'].append('Steel Sword')
            self.player.gold -= 400
            print("You bought a Steel Sword.")
        elif choice == 8 and self.player.gold >= 300:
            self.player.inventory['armor'] = 'Adventurer\'s Armor'
            self.player.gold -= 300
            print("You bought Adventurer's Armor.")
        elif choice == 9 and self.player.gold >= 600:
            self.player.inventory['armor'] = 'Steel Armor'
            self.player.gold -= 600
            print("You bought Steel Armor.")
        elif choice == 10 and self.player.gold >= 500:
            self.player.inventory['magic_items'] = 'Scepter\'s Eye'
            self.player.gold -= 500
            print("You bought Scepter's Eye.")
        elif choice == 11 and self.player.gold >= 700:
            self.player.spells['reflect'] = True
            self.player.spell_cooldowns['reflect'] = 0
            self.player.gold -= 700
            print("You bought the Reflect Spell.")
        else:
            print("You don't have enough gold or invalid choice.")

# running the game
dungeon = Dungeon()
dungeon.play_game()
