# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("Bob", 2)
cat2 = Cat("Larry", 9)
cat3 = Cat("Ant", 27)


# all_cats = [cat1.name, cat2.name, cat3.name]
# all_cats = {(cat1.name, cat1.age), (cat2.name, cat2.age), (cat3.name, cat3.age)}


# 2 Create a function that finds the oldest cat
def oldest(*args):
    # print(cat3.name, cat3.age)
    return max(args)


print(oldest)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"The oldest cat is {oldest(cat1.age, cat2.age, cat3.age)} years old.")
