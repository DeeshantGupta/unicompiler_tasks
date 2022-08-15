import random
from re import L


class Game:
    def __init__(self, lower, higher):
        self.l = lower
        self.h = higher
        self.name = ""
        self.score = 0
        self.guess = 0
        self.wrong = (higher - lower)//9
        self.max_score = higher - lower
        self.hints = []
        self.number = random.randint(lower, higher)

    def rules(self):
        print("#################################################")
        print("#                 Rules                         #")
        print("# After every wrong answer, you willget a hint  #")
        print("#                  And                          #")
        print("#   For every hint, you will lose 09points      #")
        print("#  So in total you will able to get {} hints    #".format(self.wrong))
        print("#################################################")

    def start(self):
        print("@@@@@@@@@@@@@@@@@@@@@")
        print("@Welcome to the game@")
        print("@@@@@@@@@@@@@@@@@@@@@")
        print("\n")
        self.rules()

        self.name = input("Enter your name ------>")
        # print(self.number)

        print("\n\n")

        print(
            "Range is ------> {low} - {high}".format(low=self.l, high=self.h))

        p = input("Do your first guess: ")

        while not self.check(p):
            print("\n##############################")
            print("\tHint\t")
            print("###############################")
            for i in self.hints:
                print("\r"+i)
            if (self.score == -(self.max_score)):
                self.lose()
            p = input("Wrong Guess. Do your next guess: ")

    def check(self, number):
        if not number.isdigit():
            print("\nError: Invalid Input. No point detected")
            return False

        elif int(number) == 0:
            print("\nError: Invalid Input. Out of bound.")
            return False

        else:
            number = int(number)
            if (number == self.number):
                self.win()
                return True
            else:
                self.hint(number)
                return False

    def hint(self, number):
        if self.number % number == 0:
            self.hints.append(
                "Number is a multiple of {}.".format(number))
        elif number % self.number == 0:
            self.hints.append(
                "{} is a multiple of answer.".format(number))
        elif number < self.number:
            self.hints.append(
                "Number is greater than {}.".format(number))
        elif number > self.number:
            self.hints.append(
                "Number is smaller than {}.".format(number))

        self.score -= self.wrong
        self.guess += 1

    def win(self):
        print("\n-----------------------------------------------------------------")
        print("Congratulations, you guess it correct.\n\nThe correct number is {}".format(
            self.number))

        print("Number of guesses you do: {}".format(self.guess))
        print("Your score: {}".format(self.score+self.max_score))
        print("Max Score: {}".format(self.max_score))
        print("-----------------------------------------------------------------")

    def lose(self):
        print("\nSorry, you lose.\nYou reach max number of hints.")


    # win function for showing score and no. of choices you make
a = Game(1, 100)
a.start()
