import copy

print('Задача 6. Глубокое копирование')

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам {} недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на {}',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}


def get_site_for(phone):
    new_site = copy.deepcopy(site)
    new_site['html']['head']['title'] = new_site['html']['head']['title'].format(phone)
    new_site['html']['body']['h2'] = new_site['html']['body']['h2'].format(phone)
    return new_site


count = int(input('Сколько сайтов: '))
sites = {}

for _ in range(count):
    phone_name = input('Введите название продукта для нового сайта: ')
    sites[phone_name] = get_site_for(phone_name)
    for phone_name, site in sites.items():
        print(f'Сайт для {phone_name}:')
        print(site)
        print()
