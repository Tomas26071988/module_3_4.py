# root_words.py

def single_root_words(root_word, *other_words):
    # Создаем пустой список для подходящих слов
    same_words = []

    # Приводим корневое слово к нижнему регистру для сравнения
    root_word_lower = root_word.lower()

    # Перебираем остальные слова
    for word in other_words:
        # Приводим слово к нижнему регистру для сравнения
        word_lower = word.lower()

        # Условие для добавления слова в список same_words
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)

    # Возвращаем список подходящих слов
    return same_words


# Примеры вызова функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Выводим результаты
print(result1)
print(result2)