##Пакет для разбора таблиц со ставками с сайта https://1xstavka.ru/

*При изменении структуры сайта может стать не актуальным** 
*Данные сохраняются в html, затем парсятся в json* 
***
##Пример использования

    from xstavka_parse_package.parse import parse_list
    if __name__ == '__main__':
        url_list = [
            r'https://1xstavka.ru/line/Volleyball/',
            r'https://1xstavka.ru/line/Football/',
            r'https://1xstavka.ru/line/Tennis/',
            r'https://1xstavka.ru/line/Ice-Hockey/',
        ]
        parse_list(url_list)

***
##Установка

    pip install xstavka_parse_package

## Лицензия 
Лицензия MIT