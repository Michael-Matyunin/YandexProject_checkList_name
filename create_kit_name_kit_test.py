import sender_stand_request

import data

# тестовые значения для проверок 2 и 4

symvol_511 = ("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
              "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
              "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
              "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
              "abcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdab"
              "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
              "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
              "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
              "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
              )

symvol_512 = ("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
              "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
              "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
              "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
              "abcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdab"
              "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
              "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
              "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
              "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
              )

# получение измененного набора
def get_kit_body(name):
    current_kit_body = data.kit_body.copy()

    current_kit_body["name"] = name
    return current_kit_body

# базовая функция для позитивных тестов
def positive_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_user_kit(kit_body)

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name

# тест на 1 символ
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")

# тест на 511 символов
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert(symvol_511)
# тест на английские символы
def test_create_kit_english_letter_in_name_get_success_response():
    positive_assert("QWErty")
# тест на русские символы
def test_create_kit_russian_letter_in_name_get_success_response():
    positive_assert("Мария")
# тест на спецсимволы
def test_create_kit_special_symbol_in_name_get_success_response():
    positive_assert("№%@,")
# тест на пробелы
def test_create_kit_space_in_name_get_success_response():
    positive_assert(" Человек и КО ")
# тест на цифры
def test_create_kit_numbers_in_name_get_success_response():
    positive_assert("123")

# базовая функция для негативных тестов
def negative_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_user_kit(kit_body)

    assert kit_response.status_code == 400

# тест на 0 символов
def test_create_kit_0_letter_in_name_get_error_response():
    negative_assert("")

# тест на 512 символов
def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert(symvol_512)


# базовая функция для запроса без параметра
def negative_assert_no_name(kit_body):
    kit_response = sender_stand_request.post_new_user_kit(kit_body)

    assert kit_response.status_code == 400

# тест запроса без параметра
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_no_name(kit_body)

# тест запроса с другим типом параметра
def test_create_kit_another_parametr_in_name_get_error_response():
    negative_assert(123)
