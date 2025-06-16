from survey import AnonymousSurvey

# Define a question and make a survey
question = "What programming language do you first learn to code? "
my_survey = AnonymousSurvey(question) 

# Show the question, and store the responses to the question.
my_survey.show_question()
print("Enter 'q' at anytime to quit...\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the results
print("\nThanks you everyone who participated in the survey!")
my_survey.show_results()
