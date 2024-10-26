# Define a dictionary with trivia questions and answers
trivia_questions = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "What year did the Titanic sink?": "1912",
    "Who wrote 'Romeo and Juliet'?": "Shakespeare",
    "What is the chemical symbol for water?": "H2O"
}

# Loop through each question in the dictionary
for question, answer in trivia_questions.items():
    print(question)  # Display the question
    user_answer = input("Your answer: ").strip()  # Prompt for the user's answer

    # Check if the user's answer matches the correct answer
    if user_answer.lower() == answer.lower():
        print("Correct! Well done!\n")  # Feedback for correct answer
    else:
        print(f"Incorrect. The correct answer is: {answer}\n")  # Feedback for incorrect answer

# Farewell message
print("Thank you for participating in the trivia quiz!")
