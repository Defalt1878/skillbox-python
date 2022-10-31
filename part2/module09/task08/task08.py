import re

print('Задача 8. Частотный анализ')


def get_analysis_results(text: str):
    letters = re.findall('[a-zA-Z]', text.lower())
    full_count = len(letters)
    letters_set = set(letters)
    results = [
        (letter, round(letters.count(letter) / full_count, 3))
        for letter in letters_set
    ]
    results.sort(key=lambda tpl: (-tpl[1], tpl[0]))
    return results


text_file = open('text.txt', 'r')
data = text_file.read()
text_file.close()

print('\nСодержимое файла text.txt:')
print(data)

analysis_results = get_analysis_results(data)
analysis_results = '\n'.join([f'{result[0]} {result[1]}' for result in analysis_results])

analysis_file = open('analysis.txt', 'w')
analysis_file.write(analysis_results)
analysis_file.close()

print('\nСодержимое файла analysis.txt:')
print(analysis_results)
