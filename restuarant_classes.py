
class Restaurant():

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.served = 0

    def describe_restaurant(self):
        """Returns a short description of the restaruant"""
        print "{} serves food of the {} cuisuine. How delicious!".format(self.name.title(), self.cuisine.title())

    def open_restaurant(self):
        """Indicates that the restaurant is now open"""

        print "{} is now Open!".format(self.name.title())

    def number_served(self):
        """prints the number of customers served"""

        print "{} has served {} customers!".format(self.name.title(), self.served)

    def set_number_served(self, num_served):
        """increments the number served value"""

        self.served += num_served



chapeau = Restaurant("chapeau", "french") 
chiptole = Restaurant("chiptole", "mexican")
seniores = Restaurant("seniores", "italian")

chapeau.describe_restaurant()





