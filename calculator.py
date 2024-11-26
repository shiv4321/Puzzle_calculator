import random

def generate_puzzle(answer):
    # Create a simple puzzle by scrambling the digits of the answer
    answer_str = str(answer)
    puzzle = ''.join(random.sample(answer_str, len(answer_str)))
    return puzzle

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def get_operation_input():
    while True:
        operation = input("Enter the operation (+, -, *, /): ")
        if operation in ['+', '-', '*', '/']:
            return operation
        else:
            print("Invalid operation! Please enter one of +, -, *, /.")

def calculator():
    while True:
        print("Welcome to the Puzzle Calculator!")

        # Taking input from the user
        num1 = get_float_input("Enter the first number: ")
        operation = get_operation_input()
        num2 = get_float_input("Enter the second number: ")

        # Performing the calculation
        if operation == '+':
            answer = num1 + num2
        elif operation == '-':
            answer = num1 - num2
        elif operation == '*':
            answer = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Cannot divide by zero! Please try again.")
                continue
            answer = num1 / num2

        # Generating a new puzzle for each iteration
        puzzle = generate_puzzle(answer)
        print(f"Puzzle: {puzzle}")
        
        # Asking the user to guess the answer
        for attempt in range(2):
            guess = get_float_input(f"Attempt {attempt + 1}: Guess the answer: ")
            if guess == answer:
                print(f"Congratulations! You guessed it right! The answer is: {answer}")
                break
            else:
                print("Wrong guess! Try again.")
        
        else:
            # Display the real answer if both attempts fail
            print(f"Sorry! The correct answer was: {answer}")

        # Asking if the user wants to know the meaning of the puzzle
        meaning_choice = input("Do you want to know the meaning of the puzzle? (yes/no): ").strip().lower()
        if meaning_choice == 'yes':
            print(f"The puzzle was a scrambled version of the answer: {answer}")

        # Asking user if they want to play again
        while True:
            choice = input("Do you want to play again (yes/no)? ").strip().lower()
            if choice in ['yes', 'no']:
                break
            else:
                print("Please enter 'yes' or 'no'.")

        if choice == 'no':
            break

# Run the calculator
calculator()
