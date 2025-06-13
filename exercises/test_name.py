import unittest
from format_name import name_formatted


class TestFirstLastName(unittest.TestCase):
    """Test first and last name
    Args:
        unittest (_type_): Test Case
    """
    def test_format_name(self):
        """Do Musbi Jawo work?"""
        formatted_name = name_formatted('musbi', 'jawo')
        self.assertEqual(formatted_name, 'Musbi Jawo')


if __name__ == "__main__":
    unittest.main()