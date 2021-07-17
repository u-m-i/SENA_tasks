# From poligons
from triangle import Triangle

# Unittest
import unittest


class TestPoligon(unittest.TestCase):

    def setUp(self):
        """
        """

        self.poligon = Triangle()
        self.poligon.get_sides()

        

    def test_object(self):

        self.assertIsInstance(self.poligon, Triangle)

        x_shape = input("Escribe una forma de un triángulo: ").strip(" ")

        self.poligon.shape = x_shape

        self.assertTrue(self.poligon.shape == x_shape)


    def test_area(self):

        
        self.poligon_height = self.poligon.sides["height"]
        self.poligon_base = self.poligon.sides["base"]

        self.poligon_area = self.poligon.bh_area()
        
        self.assertTrue(self.poligon_area == (self.poligon_base*self.poligon_height / 2))

        print(f"The poligon area is: {self.poligon_area}")


    def test_heron_area(self):
        
        
        self.poligon_height = self.poligon.sides["height"]
        self.poligon_base = self.poligon.sides["base"]

        self.poligon_heron_area = (1/2 * self.poligon_height * self.poligon_base)

        print(f"The poligon area is: {self.poligon_hereon_area}")

        self.assertTrue(self.poligon_heron_area == (1/2 * self.poligon_height * self.poligon_base) )

    
    def test_perimter(self):

        perimeter = self.poligon.perimeter()

        self.assertTrue(perimeter == (self.poligon.sides["side_a"] + self.poligon.sides["side_b"] + self.poligon.sides["base"]) )

        print(f"The triangle´s perimeter is: {perimeter}")

    


    def tearDown(self):
        print("El objeto fue probado")




if __name__ == "__main__":

    unittest.main(verbosity=2)