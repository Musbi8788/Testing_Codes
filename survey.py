class AnonymousSurvey():
    """Collect anonymous answer to a survey question.    
    """

    def __init__(self,question):
        """Store a questions, and prepare to store responses.

        Args:
            question (str): generate questions to ask user
        """
        self.question = question
        self.responses = []

    def show_question(self,):
        """Show the survey question
        """
        print(self.question)

    def store_response(self, new_response):
        """Store a signle response

        Args:
            new_response (str): store single response from the user.
        """
        self.responses.append(new_response)

    def show_results(self,):
        """Show all the response that have been given.
        """
        print("Survey Results:")
        for response in self.responses:
            print(f"- {response}")