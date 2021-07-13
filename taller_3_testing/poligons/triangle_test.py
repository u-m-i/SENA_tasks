# From poligons
from triangle import Triangle

# Unittest
import unittest


class TestPoligon(unittest.TestCase):

    def setUp(self):
        """
        """
        self.poligon = Triangle()
        

    def test_object(self):

        self.assertIsInstance(self.poligon, Triangle)

        x_shape = input("Escribe una forma de un triángulo: ").strip(" ")

        self.poligon.shape = x_shape

        self.assertTrue(self.poligon.shape == x_shape)


    def test_area(self):


        self.poligon.get_sides()
        self.poligon_height = self.poligon.sides["height"]
        self.poligon_base = self.poligon.sides["base"]

        self.poligon_area = self.poligon.bh_area()
        
        self.assertTrue(self.poligon_area == (self.poligon_base*self.poligon_height / 2))

        print(f"The poligon area is: {self.poligon_area}")


    def test_heron_area(self):

        
        self.poligon.get_sides()
        self.poligon_height = self.poligon.sides["height"]
        self.poligon_base = self.poligon.sides["base"]

        self.poligon_heron_area = (1/2 * self.poligon_height * self.poligon_base)

        print(self.poligon_heron_area)

        self.assertTrue(self.poligon_heron_area == (1/2 * self.poligon_height * self.poligon_base) )


    def tearDown(self):
        print("El objeto fue probado")




if __name__ == "__main__":

    unittest.main(verbosity=2)