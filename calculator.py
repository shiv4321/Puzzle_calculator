import streamlit as st
import random

def generate_puzzle(answer):
    """
    Create a simple puzzle by scrambling the digits of the answer.
    """
    answer_str = str(answer)
    puzzle = ''.join(random.sample(answer_str, len(answer_str)))
    return puzzle

def get_float_input(prompt, key=None):
    """
    Get a float input from the user, with error handling.
    """
    while True:
        try:
            value = float(st.text_input(prompt, key=key))
            return value
        except ValueError:
            st.warning("Invalid input! Please enter a numeric value.")

def get_operation_input():
    """
    Get the operation input from the user.
    """
    operation = st.selectbox("Enter the operation (+, -, *, /)", ['+', '-', '*', '/'])
    return operation

def calculator():
    """
    The main calculator function.
    """
    st.title("Puzzle Calculator")

    # Taking input from the user
    num1 = get_float_input("Enter the first number:", key="num1_input")
    operation = get_operation_input()
    num2 = get_float_input("Enter the second number:", key="num2_input")

    # Performing the calculation
    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        answer = num1 - num2
    elif operation == '*':
        answer = num1 * num2
    elif operation == '/':
        if num2 == 0:
            st.warning("Cannot divide by zero! Please try again.")
            return
        answer = num1 / num2

    # Generating a new puzzle for each iteration
    puzzle = generate_puzzle(answer)
    st.write(f"Puzzle: {puzzle}")

    # Asking the user to guess the answer
    for attempt in range(2):
        guess = get_float_input(f"Attempt {attempt + 1}: Guess the answer:", key=f"guess_{attempt}")
        if guess == answer:
            st.success(f"Congratulations! You guessed it right! The answer is: {answer}")
            break
        else:
            st.error("Wrong guess! Try again.")
    else:
        # Display the real answer if both attempts fail
        st.error(f"Sorry! The correct answer was: {answer}")

    # Asking if the user wants to know the meaning of the puzzle
    meaning_choice = st.radio("Do you want to know the meaning of the puzzle?", ['Yes', 'No'], key="meaning_choice")
    if meaning_choice == 'Yes':
        st.write(f"The puzzle was a scrambled version of the answer: {answer}")

    # Asking user if they want to play again
    play_again = st.button("Play Again", key="play_again")
    if not play_again:
        st.stop()


# Run the calculator
calculator()



st.write()
