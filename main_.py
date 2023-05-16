import random
import importlib
import sys
sys.path.append("./Users/jungdasung/Desktop/unity/project/raisen_python/story")

# 캐릭터의 이름과 배경 설명을 저장하는 클래스
class Character:
    def __init__(self):
        self.name = ""
        self.background = ""

# 배경 설명을 파일에서 읽어오는 함수
def read_background_from_file():
    with open('./text_file/background', 'r', encoding='utf-8') as file:
        return file.read()

# 배경 설명을 입력하고 출력하는 함수
def describe_background(character):
    character.background = read_background_from_file()
    print(character.background)

# Press Any Button 메시지를 출력하고 이름을 입력받는 함수
def press_any_button(character):
    input("Press Any Button to continue...")
    character.name = input("이름을 작성해 주세요: ")

# 스토리 파일들을 로드합니다.
main_story_module = importlib.import_module('main_story')
sub_story_modules = [importlib.import_module(f'sub_story{i}') for i in range(1, 5)]

def get_story(module):
    return module.get_sub_story()

def roll_dice():
    return random.randint(1, 6)

def make_choice(choices):
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")

    choice_number = int(input("선택지를 고르세요: "))
    outcome = roll_dice()

    try:
        print(f"당신이 선택한 결과: {choices[choice_number - 1]}")
        assert outcome >= 4
    except AssertionError:
        print("실패했습니다.")

def main():
    # 캐릭터 객체 생성
    character = Character()

    # 배경 설명 함수 호출
    describe_background(character)

    # Press Any Button 함수 호출
    press_any_button(character)
햣
    print(get_story(main_story_module))

    for i in range(random.randint(2, 4)):
        print(get_story(sub_story_modules[i]))

        choices = [f"선택지 {i}" for i in range(1, random.randint(2, 5))]
        make_choice(choices)

    print(get_story(main_story_module))

if __name__ == "__main__":
    main()
