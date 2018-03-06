
class Restaurant():

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        """Returns a short description of the restaruant"""
        print "{} serves food of the {} cuisuine. How delicious!".format(self.name.title(), self.cuisine.title())

    def open_restaurant(self):
        """Indicates that the restaurant is now open"""

        print "{} is now Open!".format(self.name.title())


chapeau = Restaurant("chapeau", "french") 
chiptole = Restaurant("chiptole", "mexican")
seniores = Restaurant("seniores", "italian")

chapeau.describe_restaurant()





