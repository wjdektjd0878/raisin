def get_main_story(character_name):
    with open('text_file/mainstory', 'r', encoding='utf-8') as file:
        story = file.read()
    return story.replace('{name}', character_name)


def get_sub_story():
    return "메인 스토리 내용"