import os
import json

input_words = input("Введите ключевое слово или слова: ")
words = input_words.split()
result_books_list = []
books_list_len = len(result_books_list)
folder_books = 'books'
books = os.listdir(folder_books)
error_book = str()

for book_name in books:
    try:
        folder_book = os.path.join(folder_books, book_name)
        with open(folder_book, 'r', encoding='windows-1251') as f:
            content = f.read()
            for word in words:
                if word.lower() in content.lower():
                    word_exist = True
                else:
                    word_exist = False
                    break
            if word_exist:
                result_books_list += [book_name]
    except:
        error_book = book_name
        pass
res_in_column = '\n'.join(result_books_list)
print(res_in_column)

print(f'''
Книга {error_book} не является книгой''')

# функция создания файла JSON
def writer(result):
    if len(result) <= 0:
        print('Книг с данной комбинацией слов не найдено')
    else:
        with open('books list.json', 'w') as write_file:
            json.dump(result_books_list, write_file)
            return print('\nСписок книг был записан в файл books list')


writer(result_books_list)
