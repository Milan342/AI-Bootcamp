class Cat:
    def sound(self):
        print("Meow")


class Cow:
    def sound(self):
        print("Moo")


def make_sound(animal):
    animal.sound()


make_sound(Cat())
make_sound(Cow())