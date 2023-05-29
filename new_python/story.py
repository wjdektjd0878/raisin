# story.py
import os
import random

start_story = './main_stories'
chapter1_story = './chapter1_stories'

# 주인공 이름 입력 받는 함수
def read_and_replace(file_path, player):
    with open(file_path, 'r', encoding='utf-8') as file:
        story = file.read()
        print(story.replace('{name}', player.name))

# 번호를 입력받는 
def choice_select(choices,number):
    for i in range(number):
        choice = input('번호 선택 :  ')
        if choice not in choices:
            print('올바르지 않은 선택입니다.')
            continue
        else:
            print(choice + '번을 선택하셨습니다.\n')
            return choice

        

# 초기 스토리 진행
def get_main_story1(player):
    print(f'Chapter 1: 대피')
    read_and_replace(start_story + '/main_story.txt', player)
    select = choice_select(['1','2','3'], 1)
    chapter1(player,select)
        

# Chapter_1 분기 스토리 시작
def chapter1(player, select):
    read_and_replace(start_story + '/main_choice{}_story.txt'.format(select), player)
    select_c1 = choice_select(['1','2','3'], 1)
    chapter1_choice_1(player,select_c1)



# 분기 스토리 진행
def chapter1_choice_1(player):
    print(f'Chapter 1: 대피')
    read_and_replace(f'./main_stories/main_story_choice_1.txt', player)
    chapter1_sub_1(player)


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
        chapter(player)
    else:
        print('실패하였습니다.')


# 스토리 진행 시작
def progress_story(player):
    get_main_story1(player)
