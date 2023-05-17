import importlib
import random
import sys
from main_story import get_main_story
from sub_stories import sub_story1


# 캐릭터의 이름과 배경 설명을 저장하는 클래스
class Character:
    def __init__(self):
        self.name = ""
        self.background = ""

# 배경 설명을 입력하고 출력하는 함수
def describe_background(character):
    with open('text_file/background', 'r', encoding='utf-8') as file:
        character.background = file.read()
    print(character.background)

# Press Any Button 메시지를 출력하고 이름을 입력받는 함수
def press_any_button(character):
    input("Press Any Button to continue...")
    character.name = input("이름을 작성해 주세요: ")

# 선택지를 출력하고 사용자의 선택을 입력받는 함수
def make_choice(choices):
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")
    user_choice = int(input("번호를 선택하세요: "))
    return user_choice

# 메인 함수
def main():
    # 캐릭터 객체 생성
    character = Character()

    # 배경 설명 함수 호출
    describe_background(character)

    # Press Any Button 함수 호출
    press_any_button(character)

    # 메인 스토리와 서브 스토리 모듈 import
    sys.path.append("./")
    main_story_module = importlib.import_module('main_story')
    sub_stories_module = importlib.import_module('sub_stories')

    # 메인 스토리 출력
    print(main_story_module.get_main_story(character.name))

    # 메인 스토리 선택지 출력
    choices = main_story_module.get_choices()
    make_choice(choices)

    # 서브 스토리 출력
    sub_stories = [sub_stories_module.sub_story1, sub_stories_module.sub_story2, sub_stories_module.sub_story3, sub_stories_module.sub_story4]
    for sub_story in random.sample(sub_stories, k=random.randint(2, 4)):
        story, choices = sub_story(character.name)
        print(story)
        make_choice(choices)

    # 마지막 메인 스토리 출력
    print(main_story_module.get_story(character.name))

    # 마지막 메인 스토리 선택지 출력
    choices = main_story_module.get_choices()
    make_choice(choices)

# 메인 함수 실행
if __name__ == "__main__":
    main()
