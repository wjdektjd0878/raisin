# story.py
import os
import random


# 주인공 이름 입력 받는 함수
def read_and_replace(file_path, player):
    with open(file_path, 'r', encoding='utf-8') as file:
        story = file.read()
        print(story.replace('{name}', player.name))


# 초기 스토리 진행
def get_main_story1(player):
    print(f'Chapter 1: 대피')
    read_and_replace(f'main_story.txt', player)
    chapter1(player)


# Chapter 1 스토리 시작
def chapter1(player):

    point_list = [2,1,4]

    for i in range(1):
        choice = input('번호 선택 :  ')
        if choice not in ['3', '2', '1']:
            print('Invalid choice. Please enter 3, 2, or 1.')
            continue
        else:
            for ii in range(3):
                if choice == ii:
                    read_and_replace('./chapter1_main_stories/main{}_choice_story.txt'.format(ii), player)
                    player.points = point_list[i]
                    print(player.points)

    if player.points == 2:
        chapter1_sub_1(player)
    elif player.points == 1:
        chapter1_sub_2(player)
    else:
        chapter1_sub_3(player)



def chapter1_sub_1(player):
    # 스토리 폴더에 있는 모든 텍스트 파일을 나열합니다
    available_stories = os.listdir('chapter1_sub_stories1')
    
    for i in range(4):
        # 무작위로 스토리 파일을 선택하고 목록에서 제거합니다
        story_file = random.choice(available_stories)
        available_stories.remove(story_file)
        
        # 스토리를 읽고 출력합니다

        read_and_replace(f'./chapter1_sub_stories1/{story_file}', player)
        
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


def chapter1_sub_2(player):
    # 스토리 폴더에 있는 모든 텍스트 파일을 나열합니다
    available_stories = os.listdir('chapter1_sub_stories2')
    
    for i in range(4):
        # 무작위로 스토리 파일을 선택하고 목록에서 제거합니다
        story_file = random.choice(available_stories)
        available_stories.remove(story_file)
        
        # 스토리를 읽고 출력합니다

        read_and_replace(f'./chapter1_sub_stories2/{story_file}', player)
        
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


def chapter1_sub_3(player):
    # 스토리 폴더에 있는 모든 텍스트 파일을 나열합니다
    available_stories = os.listdir('chapter1_sub_stories3')
    
    for i in range(4):
        # 무작위로 스토리 파일을 선택하고 목록에서 제거합니다
        story_file = random.choice(available_stories)
        available_stories.remove(story_file)
        
        # 스토리를 읽고 출력합니다

        read_and_replace(f'./chapter1_sub_stories3/{story_file}', player)
        
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
    get_main_story1(player)
