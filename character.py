class Attribute:

    def __init__(self, val: int):
        self.val = val

    def __int__(self):
        return self.val

    def modifier(self):
        return int(self.val / 2) - 5


class Character:

    def __init__(self, name: str):
        self.name = name
        self.intelligence = Attribute(10)
        self.charisma = Attribute(10)
        self.constitution = Attribute(11)
        self.strength = Attribute(10)
        self.dexterity = Attribute(12)
        self.perception = Attribute(10)
        self.wisdom = Attribute(10)

        self.max_hp = self.calc_max_hp()
        self.hp = self.max_hp

        self.ac = self.calc_ac()

    def calc_max_hp(self):
        return 10 + self.constitution.modifier()

    def calc_ac(self):
        return 10 + self.dexterity.modifier()

    def __str__(self):
        retval = f"Character: {self.name}\n"
        retval += f"- Int: {int(self.intelligence)}\n"
        retval += f"HP: {self.hp}\n"
        retval += f"AC: {self.ac}\n"

        return retval
