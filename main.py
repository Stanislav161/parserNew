import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Создаем объект Translator
translator = Translator()

# Создаем функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        # Создаем объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_word = soup.find("div", id="random_word").text.strip()
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        # Чтобы программа возвращала словарь
        return {
            "english_word": english_word,
            "word_definition": word_definition
        }
    # Функция, которая сообщит об ошибке, но не остановит программу
    except:
        print("Произошла ошибка")
        return None

# Создаем функцию для перевода слова и определения
def translate_to_russian(word, definition):
    try:
        translated_word = translator.translate(word, src='en', dest='ru').text
        translated_definition = translator.translate(definition, src='en', dest='ru').text
        return translated_word, translated_definition
    except Exception as e:
        print(f"Ошибка перевода: {e}")
        return word, definition

# Создаем функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    while True:
        # Создаем функцию, чтобы использовать результат функции-словаря
        word_dict = get_english_words()
        if not word_dict:
            continue

        english_word = word_dict.get("english_word")
        word_definition = word_dict.get("word_definition")

        # Переводим слово и определение на русский язык
        russian_word, russian_definition = translate_to_russian(english_word, word_definition)

        # Начинаем игру
        print(f"Значение слова - {russian_definition}")
        user = input("Что это за слово? ").strip().lower()
        if user == russian_word.lower():
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {russian_word}")

        # Создаем возможность закончить игру
        play_again = input("Хотите сыграть еще раз? y/n").strip().lower()
        if play_again != "y":
            print("Спасибо за игру!")
            break

word_game()