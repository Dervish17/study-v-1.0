import json


def main():
    # Задание 1
    s = 0
    c = 0
    with open('Задание 1.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for key in data:
            if data[key]['city'] == 'Москва':
                s += data[key]['age']
                c += 1
                print(data[key]['name'])
        print(s / c)

    # Задание 2
    info_dict = {
        'student1': {
            'last_name': 'Калинин',
            'first_name': 'Николай',
            'second_name': 'Сергеевич',
            'phone': '+79619553302',
            'year_of_birth': '1986',
            'place_of_birth': 'Тамбовка',
            'place_of_study': 'БГПУ'
        }
    }
    with open('Задание 2.json', 'w', encoding='utf-8') as info_file:
        json.dump(info_dict, info_file, ensure_ascii=False, indent='\t')

    # Задание 3
    with open('Задание 2.json', 'r', encoding='utf-8') as info_file:
        changed_key = input('Введите, какое значение вы хотите изменить: ')
        changed_value = input('Введите новую информацию: ')
        changed_dict = json.load(info_file)
        if changed_key == 'Фамилия':
            changed_dict['student1']['last_name'] = changed_value
        elif changed_key == 'Имя':
            changed_dict['student1']['first_name'] = changed_value
        elif changed_key == 'Отчество':
            changed_dict['student1']['second_name'] = changed_value
        elif changed_key == 'Телефон':
            changed_dict['student1']['phone'] = changed_value
        elif changed_key == 'Год рождения':
            changed_dict['student1']['year_of_birth'] = changed_value
        elif changed_key == 'Город рождения':
            changed_dict['student1']['place_of_birth'] = changed_value
        elif changed_key == 'Место учебы':
            changed_dict['student1']['place_of_study'] = changed_value
    with open('Задание 2.json', 'w', encoding='utf-8') as info_file:
        json.dump(changed_dict, info_file, ensure_ascii=False, indent='\t')

    # Задание 4
    with open('test — копия.json', 'r', encoding='utf-8') as info_file:
        geo_test = json.load(info_file)
        print('Метка находится в стране:', geo_test['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
              ['metaDataProperty']['GeocoderMetaData']['Address']['Components'][0]['name'])
        print('Координаты:', geo_test['response']['GeoObjectCollection']
              ['featureMember'][0]['GeoObject']['Point']['pos'])

    # Задание 5
    with open('test — копия.json', 'r', encoding='utf-8') as info_file:
        geo_test = json.load(info_file)
        geo_test['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty'][
            'GeocoderMetaData']['Address']['country_code'] = 'Rus'
        geo_test['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty'][
            'GeocoderMetaData']['Address']['postal_code'] = '675004'
        geo_test['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty'][
            'GeocoderMetaData']['Address']['formatted'] = 'г. Благовещенск, ул. Ленина, 104'
    with open('test — копия.json', 'w', encoding='utf-8') as info_file:
        json.dump(geo_test, info_file, ensure_ascii=False, indent='\t')


if __name__ == '__main__':
    main()
