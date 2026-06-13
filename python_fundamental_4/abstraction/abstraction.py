from abc import ABC, abstractclassmethod #imported from abc module

class Animal(ABC): #abstract class 
    @abstractclassmethod
    def make_sound(self):  #abstract method
        pass # pass-nothing to do now

class Lion(Animal):
    def make_sound(self):
        print("Roar!")

class Cat(Animal):
    def make_sound(self):
        print("Meaw!")

cat=Cat()
cat.make_sound()

lion=Lion()
lion.make_sound()