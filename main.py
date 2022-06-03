import random

acceptable = ('R','r','P','p','S','s')

print('''Winning Rules of the Rock paper scissor game as follows: \n
                Rock vs paper == paper wins \n
                Rock vs scissor == Rock wins \n
                paper vs scissor == scissor wins \n''')

while True:
    print('''Pick an option >>>
        R for Rock
        P for Paper
        S for Scissors''')
    user_choice = input('Your turn: ')

    while user_choice not in (acceptable):
        user_choice = input('Enter a valid input: ')
    
    if user_choice in ('R','r'):
        choice_name = 'Rock'
    elif user_choice in ('P','p'):
        choice_name = 'Paper'
    elif user_choice in ('S','s'):
        choice_name = 'Scissors'

    print(f'Your choice is: {choice_name}')
    print('\nNow my turn.......')

    ai_choice = random.randint(1, 3)

    if ai_choice == 1:
        ai_choice_name = 'Rock'
    elif ai_choice == 2:
        ai_choice_name = 'Paper'
    elif ai_choice == 3:
        ai_choice_name = 'Scissors'

    print(f'I choose: {ai_choice_name}')
    print(f'\n{choice_name} vs {ai_choice_name}')

    if choice_name == 'Rock' and ai_choice_name == 'Paper':
        print('Paper Wins vs Rock\n')
        print('==I win this round==')
    elif choice_name == 'Paper' and ai_choice_name == 'Rock':
        print('Paper Wins vs Rock\n')
        print('==You win this round==')
    elif choice_name == 'Rock' and ai_choice_name == 'Rock':
        print('==It is a tie==')

    elif choice_name == 'Rock' and ai_choice_name == 'Scissors':
        print('Rock Wins vs Scissors\n')
        print('==You win this round==')
    elif choice_name == 'Scissors' and ai_choice_name == 'Rock':
        print('Rock Wins vs Scissors\n')
        print('==I win this round==')
    elif choice_name == 'Scissors' and ai_choice_name == 'Scissors':
        print('==It is a tie==')

    elif choice_name == 'Paper' and ai_choice_name == 'Scissors':
        print('Scissors Wins vs Paper\n')
        print('==I win this round==')
    elif choice_name == 'Scissors' and ai_choice_name == 'Paper':
        print('Scissors Wins vs Paper\n')
        print('==You win this round==')
    elif choice_name == 'Scissors' and ai_choice_name == 'Scissors':
        print('==It is a tie==')


    query = input('Do you want to play again? (Y/N):  ')
    if query in ('y','Y'):
        continue
    elif query in ('n','N'):
        print('Thanks For playing')
        break