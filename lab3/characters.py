class Weapon:

    def __init__(self, name, damage):

        self.name = name
        self.damage = damage


    def attack_description(self):
        return f"attacks with {self.name} for {self.damage} damage"



class Character:

    def __init__(self, name, special_power):

        self.name = name

        self.special_power = special_power

        self.weapon = None


    def __str__(self):

        return f"I am {self.name}, a {self.__class__.__name__}"


    def equip_weapon(self, weapon):

        self.weapon = weapon


    def attack(self):

        if self.weapon:

            return f"{self.name} {self.weapon.attack_description()}!"

        return f"{self.name} attacks with bare hands for 5 damage!"


    def get_status(self):

        weapon_info = self.weapon.name if self.weapon else "unarmed"

        return f"{self.name} the {self.__class__.__name__} - Weapon: {weapon_info}"


def summon_power(self):

        raise NotImplementedError("Subclasses must implement summon_power()")



class Warrior(Character):

    def __init__(self, name):

        super().__init__(name, "Berserker Rage")


    def summon_power(self):

        return f"{self.name} unleashes {self.special_power}! Attack power doubled!"



class Mage(Character):

    def __init__(self, name):

        super().__init__(name, "Arcane Blast")


    def summon_power(self):

        return f"{self.name} channels {self.special_power}! Enemies are stunned!"



class Archer(Character):
    def __init__(self, name):
        super().__init__(name, "triple shot")

    def summon_power(self):

        return f"{self.name} uses {self.special_power}! They can now shoot three arrows at once!"



bow = Weapon("bow","30hp")
staff = Weapon("staff","75hp")
sword = Weapon("sword","50hp")


army = [

Warrior("Thorin"),
Mage("Gandalf"),
Archer("Legolas")
]


for Character in army:
    Character.equip_weapon(sword)
    print(Character)
    print(Character.get_status())
    print(Character.summon_power())

army[0].equip_weapon(sword)
print(army[0].summon_power())
army[1].equip_weapon(sword)
print(army[1].summon_power())

