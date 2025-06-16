import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Test for the class Anonymous Survey

    Args:
        unittest (module): unittest testcase
    """

    def setUp(self) -> None:
        """Create a survey and a set of responses for used in all test methods.
        """
        question = "What programming language did you first learn to code?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Python', 'C++', 'Javascript']

    def test_store_single_response(self):
        """Test that a signle response is stored properly.
        """
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_response(self):
        """Test if three response store properly.
        """

        for response in self.responses:
            self.my_survey.store_response(response)
        
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == "__main__":
    unittest.main()