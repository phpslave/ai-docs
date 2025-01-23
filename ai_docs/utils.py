def save_to_file(content, path):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)