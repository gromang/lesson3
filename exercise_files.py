new_content = ''
with open('referat.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    word_count = content.replace('\n', ' ').split(' ')
    new_content = content.replace('.', '!')

    print(f'Длина строки: {len(content)} символов')
    print(f'Колличество слов в реферате: {len(word_count)}')

with open('referat2.txt', 'w', encoding='utf-8') as new_file:
    new_file.write(new_content)
