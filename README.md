# Move-day
Сразу говорю, что опыта у меня 1 месяц, скрипт кривой и почти все можно переделать и сделать лучше. Но вроде работает более-менее.

Инструкция:
1) EXTENSION_PATH = f'C:/Users/User/AppData/Local/Google/Chrome/User Data/Profile 1/Extensions/nkbihfbeogaeaoehlefnkodbefgpgknn/12.6.1_0.crx'
   Указываем путь к расширению ММ (файл приложил)

2) Указываем сидки, прокси и номер аккаунта в таком формате (прокси тут не надо, но я тестил, поэтому оставил, можете везде одну поставить)
wallets = [
    {
        "seed_phrase": ["word", "word", "word", "word", "word", "word", "word", "word", "word", "word", "word", "word"],
        "proxy": {
            'http': 'http://LOGIN:PASS@111.111.11.11:22222',
            'https': 'https://LOGIN:PASS@111.111.11.11:22222'
        },
        "name": "Account 1"
    },
    {
        "seed_phrase": ["word", "word", "word", "word", "word", "word", "word", "word", "word", "word", "word", "word"],
        "proxy": {
            'http': 'http://LOGIN:PASS@111.111.11.11:22222',
            'https': 'https://LOGIN:PASS@111.111.11.11:22222'
        },
        "name": "Account 2"
    },
]

3) После выполнения пары квестов будет написан такой текст, в скобочках список готовых аккаунтов.
  Квесты для Account 4 завершены.
  [4, 11, 48]
  Если вдруг скрипт вылетит с ошибкой, готовые аккаунты нужно просто закомментировать.

4) Скрипт работает достаточно долго, в том числе потому, что Галка глючная. Я просто запускаю на фоне и занимаюсь другими делами.
   
6) Ошибки сейчас вылетают редко, но иногда бывает, в том числе из-за глючной галки)
   
7) Все дейсвия сопровождаются комментариями:
  Страница Battle открыта
  Окно Метамаск появилось, подтверждено.
  Ждем логин.
  Логин есть.
  Задание ОК
  Кнопка квеста Battle нажата.
  Оплата подтверждена.
  Окно Метамаск появилось.
  Страница добавления сети
  Сеть добавлена
  Кнопка квеста Battle нажата.
  Оплата подтверждена.
  Окно Метамаск появилось.
  Транзакция подтверждена
  Проверка клейма
  Клейм квеста Battle выполнен.
  Открылся квест Daily Move
  Логин есть.
  Задание 1 ОК
  Задание 2 ОК
  Задание 3 ОК
  Задание 4 ОК
  Задание 5 ОК
  Кнопка квеста Daily Move нажата.
  Оплата подтверждена.
  Окно Метамаск появилось.
  Кнопка добавления сети не появилась.
  Страница подтверждения транзакции
  Проверка клейма
  Клейм квеста Daily Move выполнен.
  Квесты для Account 11 завершены.
  [11, 48]

7) Если квесты выполнены частично (например, задание выполнено, но скрипт вылетел в ошибку на клейме или задание выполнено, но Галка заглючила и этого не видит) я просто комментирую этот аккаунт и потом клеймлю его руками.

8) Сейчас в 99% проблемных случаев квест просто остановится с текстом в терминале (собственно, все написано в тексте):
  Сделай действие для продолжения: Если Метамаск появился - нажми Ентер, если НЕ появился - сделай действие для появления ММ и нажми Ентер
