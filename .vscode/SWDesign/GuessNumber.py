import random

# answer = random.randint(0, 100)
# print(answer)
# cnt = 0
# while True : 
#     guess = input("Please guess the number (between 0 - 100) :")
#     cnt += 1
#     try :
#         guess = int(guess)
#     except Exception:
#         print("Invalid number, please guess again.")
#         continue

#     if guess < answer :
#         print("Your guess was under")
#     elif guess > answer :
#         print("Your guess was over")
#     else :
#         break

# print("Congratulations!")

class GuessNumber :
    def __init__(self, number, min=0, max=100) :
        self.number = number
        self.min = min
        self.max = max
        self.guesses = 0
    
    def get_guess(self) :
        guess = input(f'Please guess a number ({self.min} - {self.max}):')

        if self.valid_number(guess) :
            return int(guess)
        else :
            print("Please enter a valid number.")
            return self.get_guess()

    def valid_number(self, str_number) :
        try :
            number = int(str_number)
        except Exception :
            return False
        
        return self.min <= number <= self.max

    def play(self) :
        while True :
            self.guesses += 1     

            guess = self.get_guess()

            if guess < self.number :
                print("Your guess was under.")
            elif guess > self.number :
                print("Your guess was over")
            else :
                break
        print(f"Congratulations! You guessed it in {self.guesses} guesses")
        print(f"Given number was {self.number}")

answer = random.randint(0, 100)
game = GuessNumber(answer, 0, 100)
game.play()