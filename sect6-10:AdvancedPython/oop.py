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

class PlayerCharacter:  # self refers back to the class
    membership = True  # class object attribute

    def __init__(self, name='', age=0, attack=5):
        # constructor method or init method
        if self.membership:
            self.name = name  # self hasnt refers to what hasnt been created yet
            self.age = age  # attributes | properties
            self.attack = attack

    def run(self):
        print('run')
        return "done"


player1 = PlayerCharacter('Cindy', attack=50)
player2 = PlayerCharacter('Tom', age=75)
player3 = PlayerCharacter('Rick')

print(player1.attack)
print(player2.age)
