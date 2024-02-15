# import pandas as pd
import os


# установка параметров обработки первичных данных
# отбор данных по известному расширению файлов
known_extensions = ['.EXE', '.SYS', '.COM', '.CMD']
# отбор данных по категориям вхождения в каталоги
known_category = ['C:\\WINDOWS', 'C:\\PROGRAM FILES']


# проверка расширения файла на соответствие заданному перечню расширений
def test_file_ext(test_str: str, file_ext: list):
    filename, file_extension = os.path.splitext(test_str)
    if file_extension in file_ext:
        return True
    else:
        return False

# подсчет количества директорий в пути файла
def test_file_jump(test_str: str):
    return test_str.count('\\')

# проверка пути файла на вхождение в категорию поиска
def test_file_category(test_str: str, file_cat: list):
    rezult = 0
    for i in file_cat:
        if i in test_str:
            rezult = file_cat.index(i) + 1
            break
    return rezult

#
def read_write_data(inp_file: str, outp_file: str, flag_train: bool):
    # порядковый номер
    string_number = 0
    # список с данными для записи в файл
    data_for_file = []

    with open(inp_file, 'r', encoding='ansi', errors='ignore') as file:
        text_lines = file.readlines()

    if flag_train:
        data_for_file.append(
            'FileId' + ',' + 'WarningFlag' + ',' + 'FileName' + ',' + 'DirectoryCount' + ',' + 'FileCategory' + '\n')
        for item in text_lines:
            #разбор пути файла
            test_string = item.strip().upper()
            # флаг попадания файла в выборку
            warn_flag = 0

            if test_file_ext(test_string, known_extensions):
                file_count_dir = test_file_jump(test_string)
                file_category = test_file_category(test_string, known_category)
                if 3 > file_count_dir or file_count_dir > 5:
                    warn_flag = 1
                string_for_csv = str(string_number) + ',' + str(warn_flag) + ',' + os.path.basename(
                    test_string) + ',' + str(file_count_dir) + ',' + str(file_category) + '\n'
                data_for_file.append(string_for_csv)
                string_number += 1

        with open('train_' + outp_file, 'w', encoding='utf-8', errors='ignore') as file:
            file.writelines(data_for_file)
    else:
        data_for_file.append('FileId' + ',' + 'FileName' + ',' + 'DirectoryCount' + ',' + 'FileCategory' + '\n')
        for item in text_lines:
            test_string = item.strip().upper()

            if test_file_ext(test_string, known_extensions):
                file_count_dir = test_file_jump(test_string)
                file_category = test_file_category(test_string, known_category)
                string_for_csv = str(string_number) + ',' + os.path.basename(test_string) + ',' + str(
                    file_count_dir) + ',' + str(file_category) + '\n'
                data_for_file.append(string_for_csv)
                string_number += 1

        with open('test_' + outp_file, 'w', encoding='utf-8', errors='ignore') as file:
            file.writelines(data_for_file)



def main():
    read_write_data('c_all.txt', 'data_model.csv', True)
    read_write_data('d_all.txt', 'data_model.csv', False)
