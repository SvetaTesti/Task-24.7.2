import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import json


class PetFriends:
    def __init__(self):
        self.base_url = 'https://petfriends.skillfactory.ru/'


#Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON #
    #с уникальным ключем пользователя, найденного по указанным email и паролем#
    def get_api_key(self, email, password):  #Получение ключа авторизации#
        headers = {
            'email': email,
            'password': password
        }
        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

#Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON#
    #со списком наденных питомцев, совпадающих с фильтром.#
    def get_list_of_pets(self, auth_key, filter: str = ""):
        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url + 'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

#Метод позволяет добавить информацию о новом питомце и возвращает статус запроса#
    # и результат в формате JSON с данными добавленного питомца#
    def add_new_pet(self, auth_key: json, name: str, animal_type: str,
                    age: str, pet_photo):
        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

#Метод отправляет на сервер запрос на удаление питомца по указанному ID#
    # и возвращает статус запроса и результат в формате JSON с текстом уведомления о успешном удалении#
    def delete_pet(self, auth_key, pet_id: str = ""):
        headers = {'auth_key': auth_key['key']}


        res = requests.delete(self.base_url + '/api/pets/' + pet_id, headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result


#Метод отправляет запрос на сервер о новых данных питомца по указанному ID и
        #возвращает статус запроса и результат в формате JSON с обновлённыи данными питомца#
    def put_pet(self, auth_key, pet_id: str, name: str, animal_type: str, age: int):
        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.put(self.base_url + '/api/pets/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result


