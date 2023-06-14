class Quadruped:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight  # in pounds
        self.height = height  # in inches
        self.daily_calories = 0
        self.foods_eaten = []

    def growl(self):
        print("GRRRRR")

    def consume(self, treat):
        self.daily_calories += treat.calories
        self.foods_eaten.append(treat)


class Treat:
    def __init__(self, name, weight, calories):
        self.name = name
        self.weight = weight  # in pounds
        self.calories = calories  # in inches


class Dog(Quadruped):
    def __init__(self, name, weight, height):
        super().__init__(name, weight, height)

    def bark(self):
        print("WOOF!")


class Cat(Quadruped):
    def __init__(self, name, weight, height):
        super().__init__(name, weight, height)

    def meow(self):
        print("Meow!")


if __name__ == "__main__":
    print("\n\n=====CAT TIME=====")
    ramy = Cat("Ramy", 15, 12)
    ramy.meow()
    ramy.growl()
    my_treat = Treat("kibble", 1, 15)
    my_treat2 = Treat("kibble", 1, 15)
    print("===Ramy calories before===")
    print(ramy.daily_calories)
    print("===Ramy calories after===")
    ramy.consume(my_treat)
    print(ramy.daily_calories)
    ramy.consume(my_treat2)
    for treat in ramy.foods_eaten:
        print(treat.name)
    print(ramy.daily_calories)
    


	ramys_foods_eaten = []
    franks_food_eaten = []
    
	pets = []
	for name in ["frank", "ramy", "max"]:
        pets.append(Dogs(name, 0, 0))

	for pet in pets:
		print(pet.name)