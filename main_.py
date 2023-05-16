import random
import importlib
import sys
from main_story import get_main_story
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

def get_story(module, character_name):
    try:
        story = module.get_sub_story().replace('{name}', character_name)
    except Exception:
        story = "스토리를 불러오는데 실패했습니다."
    return story


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

# Define the story parts
story_parts = {
    'part1': {
        'story': 'You are at a fork in the road.',
        'choices': ['Go left', 'Go right', 'Go straight', 'Turn back']
    },
    'part2': {
        'story': 'You encounter a mysterious stranger.',
        'choices': ['Talk to the stranger', 'Ignore the stranger', 'Run away']
    },
    # Add more story parts and choices as needed...
}

def tell_story(part, character_name):
    story = story_parts[part]['story'].replace('{name}', character_name)
    print(story)
    make_choice(story_parts[part]['choices'])

# main function
def main():
    # Create character object
    character = Character()

    # Call background description function
    describe_background(character)

    # Call the Press Any Button function
    press_any_button(character)

    # Proceed to each part of the story
    for part in story_parts:
        tell_story(part, character.name)

        # Proceed to sub-stories
        for i in range(random.randint(2, 4)):
            sub_story = get_story(sub_story_modules[i], character.name)
            print(sub_story)

            choices = [f"choice {i}" for i in range(1, random.randint(2, 5))]
            make_choice(choices)

    # Print the character's name at the end
    print("Your character's name is " + character.name)

# Execute main function
if __name__ == "__main__":
    main()
