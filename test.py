# class Furniture:
# 	color = ""
# 	material = ""

# table = Furniture()
# table.color = "brown"
# table.material = "wood"

# couch = Furniture()
# couch.color = "red"
# couch.material = "leather"

# def describe_furniture(piece):
# 	return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))

# print(describe_furniture(table)) 
# # Should be "This piece of furniture is made of brown wood"
# print(describe_furniture(couch)) 
# # Should be "This piece of furniture is made of red leather"

# Class and composition
class Animal:
    name = ""
    category = ""
    
    def __init__(self, name):
        self.name = name
    
    def set_category(self, category):
        self.category = category

class Turtle(Animal):
    category = "reptile"

print(Turtle.category)

class Snake(Animal):
    category = "reptile"

class Zoo:
    def __init__(self):
        self.current_animals = {}
    
    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.category
    
    def total_of_category(self, category):
        result = 0
        for animal in self.current_animals.values():
            if animal == category:
                result += 1
        return result

zoo = Zoo()

turtle = Turtle("Turtle") #create an instance of the Turtle class
snake = Snake("Snake") #create an instance of the Snake class

zoo.add_animal(turtle)
zoo.add_animal(snake)

print(zoo.total_of_category("reptile")) #how many zoo animal types in the reptile category