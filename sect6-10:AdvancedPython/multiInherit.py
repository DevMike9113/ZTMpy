class User(object):
    def sign_in(self):
        print('hello')


class Wizard(User):
    def __init__(self, name, power):
        # User.__init__(self, email)
        # super().__init__(email)  # new in Python
        self.name = name
        self.power = power

    def attack(self):
        # User.attack(self)
        print(f'attacking with the power of {self.power}')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f'{self.arrows} remaining')

    def run(self):
        print('ran really fast')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


hb1 = HybridBorg('borgie', 100, 20)

# wizard1 = Wizard('arch', 20)

print(hb1.run())
print(hb1.check_arrows())
print(hb1.attack())
print(hb1.sign_in())
