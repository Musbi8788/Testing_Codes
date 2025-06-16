import unittest
from employee import Employee


class TestEmployeeSalary(unittest.TestCase):
    """Test if Employee class will work properly

    Args:
        unittest (str): test case
    """

    def setUp(self, ) -> None:
        """Test for both annual and raise salaries
        """
        self.annual_salary = 3000
        self.my_salary = Employee('musbi', 'jawo', self.annual_salary)

    def test_give_defualt_raise(self):
        """does raise salary work
        """
        self.my_salary.give_raise()
        self.assertEqual(8000, self.my_salary.annual_salary)

    def test_give_custom_raise(self):
        """test add custom raise
        """
        custom_raise = 3000
        self.my_salary.give_raise(custom_raise)
        self.assertEqual(6000, self.my_salary.annual_salary)


if __name__ == "__main__":
    unittest.main()
