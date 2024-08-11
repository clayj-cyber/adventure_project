import random
from player.abilities import SpecialAbility, fire_breath, smash

class Monster:
    def __init__(self, name, level, base_hp, base_attack, abilities=None, immune_to_fire=False, gold=0):
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
        self.is_shielded = False
        self.shield_turns = 0
        self.is_drowned = False
        self.drowned_duration = 0
        self.immune_to_fire = immune_to_fire
        self.experience = self.level * 20  # Experience proportional to monster level
        self.gold = gold  # Gold dropped by the monster

    def take_turn(self, player):
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
        for ability in self.abilities:
            ability.reduce_cooldown()

