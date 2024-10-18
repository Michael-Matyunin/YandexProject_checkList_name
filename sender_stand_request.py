import configuration

import requests

import data


# создать пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


# получить токен
def get_new_user_token():
    response = post_new_user(data.user_body)
    return response.json().get("authToken")

# создать набор
def post_new_user_kit(kit_body):
    header_copy = data.headers.copy()
    header_copy["Authorization"] += get_new_user_token()
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json=kit_body,
                         headers=header_copy)
