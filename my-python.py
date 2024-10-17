class Hero:
    def __init__(self, name, health, attack_power, armor_number):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.armor_number = armor_number

    # Anda telah diserang
    def diserang(self, lawan, attack_power_lawan):
        attack_diterima = attack_power_lawan - self.armor_number if attack_power_lawan > self.armor_number else 0
        print(f"Damage yang diterima: { str(attack_diterima) } Phsycal Damage")
        
        if attack_diterima < self.health:
            self.health -= attack_diterima
        else:
            self.health = 0

        return self.health

    # Anda menyerang
    def serang(self, lawan):
        print(f"{ self.name } Menyerang { lawan.name }")
        print(f"Anda telah mengalahkan {self.name}") if lawan.diserang(self, self.attack_power) == 0 else print(f"HP {lawan.name} bersisa {lawan.health}. Ayo serang lagi!")

fattahillah = Hero("Hiu", 2000, 1500, 550)
susan = Hero("Kucing", 100000, 1990, 12000)

susan.serang(fattahillah)
print("")
susan.serang(fattahillah)