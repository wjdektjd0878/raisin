# story.py
import random

# Chapter 1 스토리 시작
def chapter1(player):
    print(f'Chapter 1: {player.name} escapes.')
    for i in range(4):
        choice = input('Choice (3, 2, or 1 points): ')
        if choice not in ['3', '2', '1']:
            print('Invalid choice. Please enter 3, 2, or 1.')
            continue
        else:
            player.points += int(choice)
            success_probability = 70 if choice == '3' else 80 if choice == '2' else 90
            if random.randint(1, 100) > success_probability:
                print('Fail.')
                player.points = 0
            else:
                print('Success!')
    if player.points >= 10:
        chapter2(player)
    else:
        print('Game over.')

# Chapter 2 스토리 시작
def chapter2(player):
    print(f'Chapter 2: {player.name} moves on.')
    for i in range(5):
        choice = input('Choice (3, 2, or 1 points): ')
        if choice not in ['3', '2', '1']:
            print('Invalid choice. Please enter 3, 2, or 1.')
            continue
        else:
            player.points += int(choice)
            success_probability = 70 if choice == '3' else 80 if choice == '2' else 90
            if random.randint(1, 100) > success_probability:
                print('Fail.')
                player.points -= 1
            else:
                print('Success!')
    if player.points >= 11:
        chapter3(player)
    else:
        print('Game over.')

# Chapter 3 스토리 시작
def chapter3(player):
    print(f'Chapter 3: {player.name} continues.')
    # Chapter 3 로직...

# 스토리 진행 시작
def progress_story(player):
    chapter1(player)
