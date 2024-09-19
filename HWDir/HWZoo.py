from os import remove


class Animal:

    def __init__(self, name, age, spec):
        self._name = name
        self._age = age
        self._spec = spec

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def get_spec(self):
        return self._spec

    def set_spec(self, spec):
        self._spec = spec

    def make_sound(self):
        raise NotImplementedError("")




class Mammal(Animal):

    def __init__(self, name, age):
        super().__init__(name, age, spec="Mammal")
        self._skin_type = "fur"

    def get_skin_type(self):
        return self._skin_type
    def make_sound(self):
        return f'{self.get_name()} рычит.'


class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, spec="Bird")
        self._skin_type = "feather"

    def get_skin_type(self):
        return self._skin_type

    def make_sound(self):
        return f"{self.get_name()} чирикает."


class Reptile(Animal):

    def __init__(self, name, age):
        super().__init__(name, age, spec="Рептилия")
        self._skin_type = "Scale"

    def get_skin_type(self):
        return self._skin_type

    def make_sound(self):
        return f"{self.get_name()} шипит."


class Zoo:

    def __init__(self):
        self._animals = []

    def add_animal(self, animal):
        self._animals.append(animal)

    def remove_animal(self, name):
        for animal in self._animals:
            if animal.get_name() == name:
                self._animals.remove(animal)
                print(f"{name} удален из зоопарка.")
                return
        print(f"Животное с именем {name} не найдено.")

    def show_all_animals(self):
        if not self._animals:
            print("В зоопарке пока нет животных.")
        else:
            print("Животные в зоопарке:")
            for animal in self._animals:
                print(f"Имя: {animal.get_name()}, Возраст: {animal.get_age()}, Вид: {animal.get_spec()}, Покрытие кожи: {animal.get_skin_type()}")

    def make_all_sounds(self):
        for animal in self._animals:
            print(animal.make_sound())



myZoo = Zoo()

lion = Mammal('Лев', 3)
sparrow = Bird("Воробей", 2)
snake = Reptile("Змея", 3)



myZoo.add_animal(lion)
myZoo.add_animal(sparrow)
myZoo.add_animal(snake)


myZoo.show_all_animals()


myZoo.make_all_sounds()

# myZoo.remove_animal('Воробей')

