def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print('--------------------')
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input('guess a, b, or c: ').lower()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guesses, guesses)

def check_answer(answer, guess):
    if answer == guess:
        print('right')
        return 1
    else:
        print('wrong')
        return 0
    
def display_score(correct_guesses, guesses):
    print('--------------------')
    print('results')
    print('-----------------')
    print('Answers: ', end='')
    for i in questions:
        print(questions.get(i), end=' ')
    print()

    print('Guesses: ', end=' ')
    for i in guesses:
        print(i, end=' ')
    print()

    score = int(correct_guesses/len(questions)*100)
    print('Your score is: ' + str(score))



def play_again():
    response = input('do you want to play again: type yes or no').upper()

    if response == 'YES':
        return True
    else:
        return False

questions = {
    'who created pyhton?': 'a',
    'what year was python created?': 'b',
    'python is tributed to what comedy group?': 'c',
    'is the earth round?': 'a'
}

options = [['a. guido', 'b. elon', 'c. bill'], ['a.1990', 'b. 1999', 'c. 2000'], ['a. one', 'b. two', 'c. monty python'], ['a. true', 'b. false']]

new_game()

while play_again():
    new_game()