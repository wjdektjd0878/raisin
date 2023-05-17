# main_story.py

def get_main_story(character_name, choice=None):
    story_path = 'text_file/mainstory.txt'

    if choice:
        # If a choice has been made, update the story path
        story_path += f'_{choice}'

    with open(f'{story_path}', 'r', encoding='utf-8') as file:
        story = file.read()

    return story.replace('{name}', character_name)

def get_choices():
    return ['Option 1', 'Option 2', 'Option 3']
