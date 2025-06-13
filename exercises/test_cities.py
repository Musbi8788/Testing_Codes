import unittest
from city_function import city_country


class TestCityCountryName(unittest.TestCase):
    """A simple program to test city country name format"""

    def test_city_country(self):
        """Do Banjul Gambia work? """

        formatted_name = city_country('banjul', 'gambia')
        self.assertEqual(formatted_name, 'Banjul, Gambia')

    def test_city_country_population(self):
        formatted_name = city_country('banjul', 'gambia' ' - ' '555')
        self.assertEqual(formatted_name, 'Banjul, Gambia - 555')


if __name__ == "__main__":
    unittest.main()
