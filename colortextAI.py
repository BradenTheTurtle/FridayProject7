# Define functions for changing text color
def redText(text):
    return f"\033[91m{text}\033[0m"  # ANSI escape code for red text

def blueText(text):
    return f"\033[94m{text}\033[0m"  # ANSI escape code for blue text

def greenText(text):
    return f"\033[92m{text}\033[0m"  # ANSI escape code for green text

def yellowText(text):
    return f"\033[93m{text}\033[0m"  # ANSI escape code for yellow text

def brownText(text):
    return f"\033[38;5;94m{text}\033[0m"  # ANSI escape code for brown text

# Main program logic
if __name__ == "__main__":
    # Call each function and print the colored text
    print(redText("This text is red!"))
    print(blueText("This text is blue!"))
    print(greenText("This text is green!"))
    print(yellowText("This text is yellow!"))
    print(brownText("This text is brown!"))

    # User input for custom text color
    color_choice = input("Choose a color (red, blue, green, yellow, brown): ").strip().lower()
    user_text = input("Enter the text you want to display: ")

    # Display the user's text in the chosen color
    if color_choice == "red":
        print(redText(user_text))
    elif color_choice == "blue":
        print(blueText(user_text))
    elif color_choice == "green":
        print(greenText(user_text))
    elif color_choice == "yellow":
        print(yellowText(user_text))
    elif color_choice == "brown":
        print(brownText(user_text))
    else:
        print("Invalid color choice. Please choose from red, blue, green, yellow, or brown.")
