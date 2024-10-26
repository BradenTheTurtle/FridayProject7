import random  # Import the random module

# Greeting message
print("Welcome to the PowerBall Lottery Number Generator!")

# Generate five random white ball numbers (1-69)
white_ball_1 = random.randint(1, 69)
white_ball_2 = random.randint(1, 69)
white_ball_3 = random.randint(1, 69)
white_ball_4 = random.randint(1, 69)
white_ball_5 = random.randint(1, 69)

# Generate one random red ball number (1-26)
red_ball = random.randint(1, 26)

# Print the lottery numbers with specified formatting
print(f"{white_ball_1} {white_ball_2} {white_ball_3} {white_ball_4} {white_ball_5}   {red_ball}")

# Farewell message
print("Good luck with your PowerBall ticket!")
