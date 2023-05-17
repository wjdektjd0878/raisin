# sub_stories.py
def sub_story1(character_name):
    # Return the contents of the first substory
    with open('text_file/sub_story1.txt', 'r', encoding='utf-8') as file:
        story = file.read().replace('{name}', character_name)
    choices = ['Choice 1', 'Choice 2', 'Choice 3']
    return story, choices

def sub_story2(character_name):
    # Return the contents of the second substory
    with open('text_file/sub_story2.txt', 'r', encoding='utf-8') as file:
        story = file.read().replace('{name}', character_name)
    choices = ['Choice 1', 'Choice 2']
    return story, choices

def sub_story3(character_name):
    # Return the contents of the third substory
    with open('text_file/sub_story3.txt', 'r', encoding='utf-8') as file:
        story = file.read().replace('{name}', character_name)
    choices = ['Choice 1', 'Choice 2', 'Choice 3']
    return story, choices

def sub_story4(character_name):
    # Return the contents of the fourth substory
    with open('text_file/sub_story4.txt', 'r', encoding='utf-8') as file:
        story = file.read().replace('{name}', character_name)
    choices = ['Choice 1', 'Choice 2']
    return story, choices
# 나머지 서브스토리도 이런 방식으로 정의하면 됩니다.
