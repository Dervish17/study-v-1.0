class Weapon:
    def __init__(self, name):
        self.name = name


class CivilianWeapon(Weapon):
    def __init__(self, name, damage):
        super().__init__(name)
        self._damage = damage


class SportWeapon(CivilianWeapon):
    def __init__(self, name, damage, clip):
        super().__init__(name, damage)
        self.clip = clip


class HuntWeapon(CivilianWeapon):
    def __init__(self, name, damage, clip):
        super().__init__(name, damage)
        self.clip = clip


class ServiceWeapon(Weapon):
    def __init__(self, name, damage):
        super().__init__(name)
        self._damage = damage


class PoliceWeapon(ServiceWeapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self.lethal = False


class CombatWeapon(Weapon):
    def __init__(self, name, damage):
        super().__init__(name)
        self._damage = damage


class Rifle(CombatWeapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)
