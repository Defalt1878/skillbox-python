import regex  # Не re, потому что он не позволяет повторения в просмотре назад
import requests

print('Задача 6. Web scraping')


def search_content_in_tags(page: str, tag: str):
    return regex.findall(rf'(?<=<{tag}.+>\s*)\b.+\b(?=\s*</{tag}>)', page)


page = requests.get('http://www.columbia.edu/~fdc/sample.html').text
print(search_content_in_tags(page, 'h3'))
