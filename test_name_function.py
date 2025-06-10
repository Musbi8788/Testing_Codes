import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """_summary_
    Tests for name_function.py
    Args:
        unittest (_type_): testing name function
    """

    def test_first_last_name(self) -> None:
        """_summary_
        Do name like 'musbi jawo' work?
        """
        formatted_name = get_formatted_name('musbi', 'jawo')
        self.assertEqual(formatted_name, 'Musbi Jawo')


if __name__ == "__main__":
    unittest.main
