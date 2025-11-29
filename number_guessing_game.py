import random

def play_round():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    close_range = 5  # Distance for "very close"
    
    print("Guess a number between 1 and 100 (max 10 attempts)!")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: "))
            attempts += 1
            
            if guess == secret_number:
                print(f"Correct! You won in {attempts}/{max_attempts} attempts.")
                return True
            elif abs(guess - secret_number) <= close_range:
                print("Very close! Try a bit higher or lower.")
            elif guess < secret_number:
                print("Too low!")
            else:
                print("Too high!")
                
        except ValueError:
            print("Enter a valid number.")
            continue
    
    print(f"Game over! The number was {secret_number}.")
    return False

def main():
    while True:
        play_round()
        replay = input("\nPlay again? (y/n): ").lower().strip()
        if replay != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
