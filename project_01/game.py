
import random
import winsound
import pygame
import time



def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    print("I have picked a number between 1 and 100.")
    print("You have only 7 attempts to guess it.\n")

    target = random.randint(1, 100)
    max_attempts = 7
    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess (1-100): "))
            
            if guess < 1 or guess > 100:
                print("❗ Please choose a number between 1 and 100.\n")
                continue

            attempts += 1

            if guess > target:
                print("🔻 Your number is greater than mine. Try a smaller number.\n")
            elif guess < target:
                print("🔺 Your number is smaller than mine. Try a bigger number.\n")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempt(s).")
                 # Initialize mixer
                pygame.mixer.init()

                # Load the sound
                pygame.mixer.Sound("project_01/firecracker.wav").play()

                # Wait for sound to finish (adjust depending on sound length)
                time.sleep(10)

                return  # End game if guessed correctly

        except ValueError:
            print("⚠️ Invalid input. Please enter a valid number.\n")

    # After all attempts are used
    print(f"❌ Game over! You've used all {max_attempts} attempts.")
    print(f"The correct number was: {target}")

# Run the game
number_guessing_game()








  
    
             