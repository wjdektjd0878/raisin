# main.py
import random
import story

# Player의 Character 생성
class Character:
    def __init__(self, name):
        self.name = name
        self.points = 0

def main():
    name = input('플레이어의 이름을 입력하세요: ')
    player = Character(name)
    story.progress_story(player)

if __name__ == "__main__":
    main()
