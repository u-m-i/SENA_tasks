""" Triangle figure and all the ecuations
"""

class Triangle:

    
    def __init__(self) -> None:

        self.shape = ""
        self.sides = {
            "base": 0,
            "side_a": 0,
            "side_b" : 0,
            "height" : 0,
        }

    
    def bh_area(self):

        """ The traditional area of a triangule
        """

        self.bh_area = (self.sides["height"] * self.sides["base"] / 2)

        return self.bh_area


    def heron_area(self):

        """ Aply the heron's method, only if we have two sides of the triangle
        """

        self.heron_area = ((1/2 *self.sides["height"]) * self.sides["base"])

        return self.heron_area
    

    def get_sides(self):

        self.shape = input("¿Cuál es la forma del triángulo? ")

        try:
            for item in self.sides.keys():

                user_attr = int(input(f"Define {item} del triángulo: "))
                self.sides[item] = user_attr
        except ValueError:
            print("Dont be a dumbass and put up a number")

        return self.sides, self.shape

 

  
    