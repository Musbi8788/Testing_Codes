class Employee():
    """Collect an employee details
    """

    def __init__(self, first_name, last_name, annual_salary):
        """Initial first, last name and annual salary and store each as an attribute

        Args:
            first_name (str): user first name
            last_name (str): user last name
            annual_salary (int): user annual salary
        """

        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_amount=5000):
        """give a raise amount and set 5,000 as defualt raise

        Args:
            raise_amount (int, optional): _description_. Defaults to 5000.
        """

        self.annual_salary += raise_amount
        
