class Stats:
    def __init__(self):
        # initialize stat attributes
        pass
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
        pass
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
pass

