# main.py
import random
import os
import story
import logging

logging.basicConfig(filename='./app.log', filemode='w', level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

def example_function(param):
    logging.info('Starting example_function')
    try:
        # Function logic goes here...
        logging.debug('This is a debug message')
    except Exception as e:
        logging.error('An error occurred: ' + str(e))
    finally:
        logging.info('Finished example_function')

# Somewhere else in your code...
example_function("test parameter")

# Player의 Character 생성
class Character:
    def __init__(self, name):
        self.name = name
        self.points = 0

def main():
    name = input('플레이어의 이름을 입력하세요: ')
    player = Character(name)
    print(story.get_main_story1(name))
    story.progress_story(player)

if __name__ == "__main__":
    main()

