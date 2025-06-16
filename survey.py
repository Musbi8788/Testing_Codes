class AnonymousSurvey:
    """
    Collect anonymous answer to a survey question.
    """
    def __init__(self, question):
        """Store a question and prepare to store a responses.

        Args:
            question (str): survey question 
        """
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question.
        """
        print(self.question)

    def store_response(self, new_response):
        """
        Store a single response to the store
        """
        self.responses.append(new_response)

    def show_results(self):
        """Show all the result that have been given.
        """
        print("Survey Result:")
        for response in self.responses:
            print("- {}".format(response))
        
        

