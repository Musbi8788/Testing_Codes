import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Test for the Anonymous class

    Args:
        unittest (test): _description_
    """

    def setUp(self):
        """Create a survey and a set of response for use in all test methods.
        """
        question = input("What language did you first learn to speak? ")
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Arabic', 'French']


    def test_store_single_response(self):
        """
        Test that a single response is store properly.
        """
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    
    
    def test_store_three_response(self):
        """Test that three individual response are stored properly.
        """
        for response in self.responses:
            self.my_survey.store_response(response)
        
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)




if __name__ == "__main__":
    unittest.main()