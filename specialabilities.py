class SpecialAbility:
    def __init__(self, name, effect, cooldown=2):
        self.name = name
        self.effect = effect
        self.cooldown = cooldown
        self.current_cooldown = 0

    def use(self, user, target):
        print(f"{user.name} uses {self.name}!")
        self.effect(user, target)
        self.current_cooldown = self.cooldown

    def reduce_cooldown(self):
        if self.current_cooldown > 0:
            self.current_cooldown -= 1

def fire_breath(user, target):
    damage = 20 + user.level * 2
    target.hp -= damage
    target.is_burning = True
    target.burn_duration = 6
    print(f"{target.name} takes {damage} fire damage and is burning!")

def stronger_fire_breath(user, target):
    damage = 30 + user.level * 3
    target.hp -= damage
    target.is_burning = True
    target.burn_duration = 6
    print(f"{target.name} takes {damage} fire damage and is burning!")

def ice_shield(user, target):
    user.is_shielded = True
    user.shield_turns = 2
    print(f"{user.name} uses Ice Shield and is protected from all damage for 2 turns!")

def ice_lance(user, target):
    damage = 15 + user.level * 1.5
    target.hp -= damage
    target.is_frozen = True
    target.frozen_duration = 3
    print(f"{target.name} takes {damage} ice damage and is frozen for 3 turns!")

def water_heal(user):
    heal_amount = 20 + user.level * 2
    user.hp += heal_amount
    print(f"{user.name} heals for {heal_amount} HP!")

def smash(user, target):
    damage = 10 + user.level * 2
    target.hp -= damage
    print(f"{user.name} smashes {target.name} for {damage} damage!")

def water_nebula(user, target):
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


