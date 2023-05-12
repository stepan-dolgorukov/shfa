# Задача «архиватор [Shannon–Fano](https://en.wikipedia.org/wiki/Shannon–Fano_coding)»

Ученики: [Юрий Машуков](https://github.com/mrKakushonok), [Степан Долгоруков](https://github.com/stepan-dolgorukov)

Преподаватель: [Елизавета Кокорина](https://github.com/jmbloodycon)

## Аргументы запуска

+ --file, -f &mdash; файл, из которого считывается информация
+ --action, -a &mdash; действие над файлом
    + encode, enc, e &mdash; кодирование
    + decode, dec, d &mdash; декодирование
+ --output, -o &mdash; файл, в которой выводится информация
+ --help, -h &mdash; показать справочное сообщение

## Примеры использования

### Кодировка

```
./shfa.py --action encode --file example.png --output compressed
```

### Декодировка

```
./shfa.py --action d --output decompr --file compressed.txt
```

## Файловый состав

+ shfa.py &mdash; файл входа в программму
+ argparser.py &mdash; разбор аргументов запуска
+ argchecker.py &mdash; проверка аргументов на корректность
+ decoder.py &mdash; декодировка (расжатие) информации
+ reader.py &mdash; считывание закодированной информаци
+ encoder.py &mdash; кодировка (сжатие) информации
+ writer.py &mdash; запись закодированной информациии
+ probability.py &mdash; подсчёт вероятности встречи символа
+ symbol_code.py &mdash; отображение &laquo;символ→код&raquo;

## Зависимости

Зависимости указываются в файле requirements.txt

## Тестирование

Для запуска тестов и формирования отчёта по покрытию используется скрипт
test.sh