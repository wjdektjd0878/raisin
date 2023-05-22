# story.py
import os
import random

def get_main_story1(player_name, choice=None):
    print(f'Chapter 1: 대피')
    story_path = 'main_story.txt'

    with open(f'{story_path}', 'r', encoding='utf-8') as file:
        story = file.read()

    return story.replace('{name}', player_name)

# Chapter 1 스토리 시작
def chapter1(player):
    story_path = ''
    for i in range(1):
        choice = input('번호 선택 :  ')
        if choice not in ['3', '2', '1']:
            print('Invalid choice. Please enter 3, 2, or 1.')
            continue
        else:
            if choice == '3' :
                with open('story.txt', 'r', encoding='utf-8') as file:
                    print(file.read())
                player.points = 3
                print(player.points)
            elif choice == '2' :
                with open('story.txt', 'r', encoding='utf-8') as file:
                    print(file.read())
                player.points = 3
                print(player.points)
            else:
                print('Success!')
                player.points += int(choice)
                print(player.points)

    if player.points == 3:
        chapter1_sub(player)
    elif player.points == 2:
        chapter1_sub(player)
    else:
        chapter1_sub(player)



def chapter1_sub(player):
    # 스토리 폴더에 있는 모든 텍스트 파일을 나열합니다
    available_stories = os.listdir('chapter1_sub_stories')
    
    for i in range(4):
        # 무작위로 스토리 파일을 선택하고 목록에서 제거합니다
        story_file = random.choice(available_stories)
        available_stories.remove(story_file)
        
        # 스토리를 읽고 출력합니다
        with open(f'chapter1_sub_stories/{story_file}', 'r', encoding='utf-8') as file:
            print(file.read())
        
        choice = input('Choice (3, 2, or 1 points): ')
        if choice not in ['3', '2', '1']:
            print('Invalid choice. Please enter 3, 2, or 1.')
            continue
        else:
            player.points += int(choice)
            success_probability = 70 if choice == '3' else 80 if choice == '2' else 90
            if random.randint(1, 100) > success_probability:
                print('Fail.')
                player.points = max(player.points - 1, 0)  # 가능하면 점수를 하나 뺍니다
                print(player.points)
            else:
                print('Success!')
                print(player.points)

        if not available_stories:
            print(player.points)
            print('실패하였습니다.')
            break

    if player.points >= 10:
        chapter2(player)
    else:
        print('실패하였습니다.')

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

# Chapter 3 스토리 시작
def chapter3(player):
    print(f'Chapter 3: {player.name} continues.')
    # Chapter 3 로직...

# 스토리 진행 시작
def progress_story(player):
    chapter1(player)
