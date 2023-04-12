# # OOP
# class BigObject: # Class or blueprint
#     pass
#
#
# obj1 = BigObject() # instantiate of class
# obj2 = BigObject() # instantiate of class
# obj3 = BigObject() # instantiate of class
#
# print(type(obj1))
# # CLASS is a blueprint that you make instances of over and over
#
# # -------------

# class PlayerCharacter:  # self refers back to the class
#     membership = True  # class object attribute
#
#     def __init__(self, name='', age=0, attack=5):
#         # constructor method or init method
#         if self.membership:
#             self.name = name  # self hasnt refers to what hasnt been created yet
#             self.age = age  # attributes | properties
#             self.attack = attack
#
#     def run(self):
#         print('run')
#         return "done"
#
#
# player1 = PlayerCharacter('Cindy', attack=50)
# player2 = PlayerCharacter('Tom', age=75)
# player3 = PlayerCharacter('Rick')
#
# print(player1.attack)
# print(player2.age)

# # -------------------

# class PlayerCharacter:
#     membership = True
#
#     def __init__(self, name='', age=0, attack=5):
#         if self.membership:
#             self.name = name
#             self.age = age
#             self.attack = attack
#
#     def shout(self):
#         print(f'my name is {self.name}')
#
#     @classmethod  # cls is the classmethod version of self
#     def adding_things(cls, num1, num2):
#         return cls('Teddy', num1 + num2)
#
#     @staticmethod  # does not have access to the cls
#     def adding_things2(num1, num2):
#         return num1 + num2
#
#
# player1 = PlayerCharacter('Cindy', age=50)
# player2 = PlayerCharacter.adding_things(2, 3)
#
# print(player1.age, player1.name)
# print(player1.adding_things(4, 6))
#
# # Four Pillars of OOP
# # 1. encapsulation - wrap and make reusable
#
# # 2. Abstraction - getting access to the wanted data and hiding the rest
# # _attribute means that its private
#
# # 3. Inheritance - allowing new objects to take on the properties of existing objects
# # class Wizard(User):
# # isinstance(instance, Class)
# print(isinstance(player2, object))
#
#
# # 4. Polymorphism - object classes can share the same method name. the names react differently debending on the
# # object that calls them
# class User(object):
#     def sign_in(self):
#         print('hello')
#
#
# class Wizard(User):
#     def __init__(self, name, power):
#         self.power = power
#         self.name = name
#
#     def attack(self):
#         print(f'attacking with the power of {self.power}')
#
#
# class Archer(User):
#     def __init__(self, name, arrows):
#         self.arrows = arrows
#         self.name = name
#
#         print(f'attacking with arrows: arrows left - {self.arrows}')
#
#
# wizard1 = Wizard('arch', power=20)
# archer1 = Archer('wiz', arrows=40)
#
# #
# # def player_attack(char):
# #     char.attack()
# #
# #
# # player_attack(wizard1)
# # player_attack(archer1)
#
# # for char in [wizard1, archer1]:
# #     char.attack()

# # ---------------

class User(object):
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('hello')


class Wizard(User):
    def __init__(self, name, power, email):
        # User.__init__(self, email)
        super().__init__(email)  # new in Python
        self.power = power
        self.name = name

    def attack(self):
        # User.attack(self)
        print(f'attacking with the power of {self.power}')


wizard1 = Wizard('arch', 20, 'merlin@gmail.com')
print(wizard1.email)

# introspection :
print(dir(wizard1))
