# Проект: разработка автотестов
### Задача: Автоматизировать чек-лист "Создание наборов с продуктами Яндекс Прилавок"
#### Чек-лист:

| №  | Описание                                           | ОР:                                                       |
|----|----------------------------------------------------|----------------------------------------------------------|
| 1  | Допустимое количество символов (1):               | Код ответа — 201                                         |
|    | `kit_body = { "name": "a" }`                      | В ответе поле `name` совпадает с полем `name` в запросе  |
| 2  | Допустимое количество символов (511):             | Код ответа — 201                                         |
|    | `kit_body = { "name": "Тестовое значение для этой проверки будет ниже" }` | В ответе поле `name` совпадает с полем `name` в запросе  |
| 3  | Количество символов меньше допустимого (0):       | Код ответа — 400                                         |
|    | `kit_body = { "name": "" }`                       |                                                          |
| 4  | Количество символов больше допустимого (512):     | Код ответа — 400                                         |
|    | `kit_body = { "name": "Тестовое значение для этой проверки будет ниже" }` |                                                          |
| 5  | Разрешены английские буквы:                       | Код ответа — 201                                         |
|    | `kit_body = { "name": "QWErty" }`                 | В ответе поле `name` совпадает с полем `name` в запросе  |
| 6  | Разрешены русские буквы:                          | Код ответа — 201                                         |
|    | `kit_body = { "name": "Мария" }`                  | В ответе поле `name` совпадает с полем `name` в запросе  |
| 7  | Разрешены спецсимволы:                            | Код ответа — 201                                         |
|    | `kit_body = { "name": ""№%@"," }`                 | В ответе поле `name` совпадает с полем `name` в запросе  |
| 8  | Разрешены пробелы:                                | Код ответа — 201                                         |
|    | `kit_body = { "name": " Человек и КО " }`         | В ответе поле `name` совпадает с полем `name` в запросе  |
| 9  | Разрешены цифры:                                  | Код ответа — 201                                         |
|    | `kit_body = { "name": "123" }`                    | В ответе поле `name` совпадает с полем `name` в запросе  |
| 10 | Параметр не передан в запросе:                    | Код ответа — 400                                         |
|    | `kit_body = {}`                                   |                                                          |
| 11 | Передан другой тип параметра (число):             | Код ответа — 400                                         |
|    | `kit_body = { "name": 123 }`                      |                                                          |

- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполняется командой pytest
