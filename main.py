import random


# Function:
#     Guess the number that's generated from random



# **************************** Functions *************************

def game():
    print('Select the range')
    first = int(input('enter the first number: '))
    second = int(input('enter the second number: '))
    print()

    answer = random.randint(first, second)

    guess = int(input(f'Guess the number in the range {first}, {second}: '))
    hint = 0
    closeCall = []

    while True:

        # **************************** Give up *************************

        # closeCall.append(abs(answer-guess))
        # closestGuess = min(closeCall)
        # if guess == 'Give UP':
        #     print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        #
        #     print(f'the closest guess is {closestGuess}')

        # **************************** Hint *************************

        if hint %5 == 0:
            print('**********************************', '\n')
            print('__________ HINT _____________', '\n')
            print(f'the number is {abs(answer - guess)} digits away from {guess}', '\n')
            print('**********************************')

        # **************************** check *************************
        if guess == answer:
            print('You got it!!!', '\n')
            print(f'the answer is {answer} ', '\n')
            print(f'total number number of tries: {hint + 1}', '\n')

            # *************************** Play Again *************************
            playAgain = int(input('Wanna Guess again: (**** 1 for yes and 0 to Quit *****): '))

            if playAgain == 1:
                game()
            break

        else:
            print('Wrong Guess, Guess again :(', '\n')
            guess = int(input(f'Guess the number in the range {first}, {second}: '))

            # **************************** for hint *************************
        hint += 1


if __name__ == '__main__':

    try:
        game()
    except ValueError:
        print("-------------------------------------------------")
        print(f'please enter a number')
        print("-------------------------------------------------")
        game()





