import unittest 
from employee import Employee

class TestEmployeeRaiseSalary(unittest.TestCase):
    """Test the Employee raise salary class

    Args:
        unittest (module): _description_. Testcase
    """

    def setUp(self) -> None:
        """Set an instand for all method
        """
        first_name = 'musbi'
        last_name = 'jawo'
        annual_salary = 3000
        self.my_salary = Employee(first_name, last_name, annual_salary)

    def test_give_default_raise(self):
        """Test default raise is correctcly added to salary.
        """
        self.my_salary.give_raise()  # add default raise to annual salary
        self.assertEqual(8000, self.my_salary.annual_salary)
    
    def test_give_custom_raise(self):
        """Test custom raise is correctly added to salary.
        """
        self.my_salary.give_raise(
            10000)  # add raise salary to annual salary 
        self.assertEqual(13000, self.my_salary.annual_salary)

if __name__ == "__main__":
    unittest.main()