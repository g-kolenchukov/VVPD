'''
Markdown – это достаточно простой язык разметки, созданный для
обозначения форматирования в обычном тексте. Путем вставки в текст
специальных символов можно сформировать блоки выделенного текста.
Например, две звёздочки (**) в начале и конце выражения делают его
выделенным полужирным начертанием, а одна звёздочка (*) до и после –
наклонным курсивом.
Необходимо написать две функции:
- первая будет преобразовывать обрамлённое в звёздочки выражение в
теги <em> и </em>;
- вторая будет преобразовывать обрамлённое в двойные звёздочки
выражение в теги <strong> и </strong>.
9.2 Входные данные
На вход обеим функциям подаётся строка S, которая может быть
обрамлена звёздочками, а может и не быть (тогда нужно вернуть исходную
строку).
9.3 Сигнатуры функций и примеры
Функции обязательно должны соответствовать определённым сигнатурам,
представленным на листингах 9.1-9.2.
Листинг 9.1 – Сигнатура первой функции
def bold (s: str) -> str:
Листинг 9.2 – Сигнатура второй функции
def itallic (s: str) -> str:
Пример: получив на вход строку «**bold text**», функция bold возвращает
строку «<strong>bold text</strong>».
'''


def itallic(line: str) -> str:
    '''Функция, преобразующая выражение к курсивному виду.'''
    if len(line) > 2:
        if line[0] == '*' and line[-1] == '*':
            line = line[1:-1]
            return f'<strong>{line}</strong>'
        else:
            return 'Строка не содержит необходимое количество звёздочек'
    else:
        return 'В строке отсутствует необходимое количество символов'


def bold(line: str) -> str:
    '''Функция, преобразующая выражение к полужирному виду.'''
    if len(line) > 4:
        if line[0] == '*' and line[1] == '*' and line[-2] == '*' and line[-1] == '*':
            line = line[2:-2]
            return f'<strong>{line}</strong>'
        else:
            return 'Строка не содержит необходимое количество звёздочек'
    else:
        return 'В строке отсутствует необходимое количество символов'


def main():
    line = input('Введите строку для каких-либо преобразований: ')
    menu = 'Меню программы:\n' \
           '1 - для того чтобы сделать строку жирной\n' \
           '2 - для того чтобы сделать строку курсивом\n' \
           '3 - для изменения исходной строки\n' \
           '0 - для выхода из программы.'
    print(menu)
    set_type = input('Введите выбранный тип: ')
    while set_type != '0':
        if set_type == '1':
            print(bold(line))
        elif set_type == '2':
            print(itallic(line))
        elif set_type == '3':
            line = input('Введите строку для каких-либо преобразований: ')
        else:
            print('Некорректно, повторите попытку')
        print(menu)
        set_type = input('Введите выбранный тип: ')


if __name__ == '__main__':
    main()
