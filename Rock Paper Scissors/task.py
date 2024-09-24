import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices_images = [rock, paper, scissors]
continue_for_correct_answer = True
user_choice = None


while True:
    while continue_for_correct_answer:
        try:
            user_choice = int(input('What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
        except ValueError:
            print('Please type digit between 0 and 2.')
            continue


        if 0 <= user_choice <= 2:
            continue_for_correct_answer = False
            break
        print('Please type digit between 0 and 2.')
        continue

    continue_for_correct_answer = True
    computer_choice = random.randint(0, 2)

    print(choices_images[user_choice])
    print('Computer chose:')
    print(choices_images[computer_choice])

    if user_choice == 0 and computer_choice == 1:
        print('You lose!')
    elif user_choice == 0 and computer_choice == 2:
        print('You won!')

    elif user_choice == 1 and computer_choice == 0:
        print('You won!')
    elif user_choice == 1 and computer_choice == 2:
        print('You lose!')

    elif user_choice == 2 and computer_choice == 0:
        print('You lose!')
    elif user_choice == 2 and computer_choice == 1:
        print('You won!')

    else:
        print('Draw!')

    rematch = input('Do you want to try again? Type y for Yes or n for No.')

    if rematch.lower() == 'y':
        continue
    else:
        break
