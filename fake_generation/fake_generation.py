import file_operations
from faker import Faker
import random
import os


def replace_letter(latters_mapping, word_list):
    '''Функция заменяет буквы в списке слов согласно словарю'''
    skills_runnic_list = []
    for skill in word_list:
        skill_runnic = ''
        for word in skill:
            word = word.replace(word, latters_mapping[word])
            skill_runnic += word
        skills_runnic_list.append(skill_runnic)
    return skills_runnic_list


def make_dir():
    save_path = input("Введите полный путь к директории, где сохранить папку с карточками:")+r"\charts"
    if os.path.isdir(save_path):
        print("Папка уже существует, файлы в ней перезаписаны")
    else:
        os.makedirs(save_path)
        print("Папка успешно создана")
    return save_path


def main():
    fake = Faker("ru_RU")
    skills_list = [
        'Стремительный прыжок', 'Электрический выстрел', 'Ледяной удар',
        'Стремительный удар', 'Кислотный взгляд', 'Тайный побег',
        'Ледяной выстрел', 'Огненный заряд'
        ]
    word_mapping = {
        'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
        'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
        'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
        'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
        'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
        'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
        'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
        'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
        'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
        'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
        'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
        'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
        'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
        'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
        'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
        'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
        'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
        'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
        'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
        'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
        'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
        'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
        ' ': ' '
    }
    charsheet_input_path = input("Введите путь к файлу с шаблоном карточки: ")
    charsheet_output_path = make_dir() + r"\result-{}.svg"

    for x in range(10):
        random_skills_list = random.sample(replace_letter(word_mapping, skills_list), 3)
        context = {
          "first_name": fake.first_name(),
          "last_name": fake.last_name(),
          "job": fake.job(),
          "town": fake.city(),
          "strength": random.randint(3, 18),
          "agility": random.randint(3, 18),
          "endurance": random.randint(3, 18),
          "intelligence": random.randint(3, 18),
          "luck": random.randint(3, 18),
          "skill_1": random_skills_list[0],
          "skill_2": random_skills_list[1],
          "skill_3": random_skills_list[2]
        }
        file_operations.render_template(charsheet_input_path, charsheet_output_path.format(x+1), context)


if __name__ == "__main__":
    main()
