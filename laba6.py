countries_dict = {"Австрия": "Вена", "Бельгия": "Брюссель", "Великобритания": "Лондон", "Германия": "Берлин", "Ирландия": "Дублин", "Лихтенштейн": "Вадуц", "Нидерладны": "Амстердам",
                 "Франция": "Париж", "Белоруссия": "Минск", "Болгария": "София", "Польша": "Варшава", "Чехия": "Прага", "Албания": "Тирана", "Босния и Герцеговина": "Сараево",
                 "Северная Македония": "Скопье", "Сербия": "Белград"}
print(countries_dict)
print(countries_dict['Германия'])
for i in sorted(countries_dict):
    print(i, " - ", countries_dict[i])

def zadacha1():
    alph = {
        "а": 1,
        "б": 3,
        "в": 1,
        "г": 3,
        "д": 2,
        "е": 1,
        "ё": 3,
        "ж": 5,
        "з": 5,
        "и": 1,
        "й": 4,
        "к": 2,
        "л": 2,
        "м": 2,
        "н": 1,
        "о": 1,
        "п": 2,
        "р": 1,
        "с": 1,
        "т": 1,
        "у": 2,
        "ф": 10,
        "х": 5,
        "ц": 5,
        "ч": 5,
        "ш": 8,
        "щ": 10,
        "ъ": 10,
        "ы": 4,
        "ь": 3,
        "э": 8,
        "ю": 8,
        "я": 3
    }

    vvod = input("Введите слово: ")
    k = 0
    for i in vvod:
        k += alph[i.lower()]
    print("Ваша сумма: ", k)

def zadacha3():
    students = {"Москвитина - японский, английский, турецкий", "Корнильцева - русский, французский, китайский"}
    languages = set()
    print("Фамилии тех, кто знает китайский язык: ")
    for student in students:
        language = student.split(' - ')[1].split(', ')
        for i in language:
            if i == 'китайский':
                print(student.split(' - ')[0])
        languages = languages.union(set(language))
    print('Языки: ', *sorted(list(languages)))
    print('Количество языков: ', len(list(languages)))


zadacha3()







