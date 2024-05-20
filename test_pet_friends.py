import os

from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import json

pf = PetFriends()


# Проверка получения ключа авторизации c невалидным email#
def test_get_api_key_for_invalid_user(email=invalid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 403  # Проверяем наличие статуса 4xx в ответе сервера и наличие ключа key в ответе#
    assert 'key' not in result

# Проверка получения ключа авторизации c невалидным паролем#
def test_get_api_key_for_unvalid_user(email=valid_email, password=invalid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 403  # Проверяем наличие статуса 4xx в ответе сервера и наличие ключа key в ответе#
    assert 'key' not in result


#Запрос списка питмцев с некорректным auth_key#
def test_get_all_pets_with_valid_key(filter=''):
    face_auth_key = {'key': 'ea738148a1f19838e1c5d1413877f3691a3731380e733e877b0ae'}
    status, result = pf.get_list_of_pets(face_auth_key, filter)
    assert status == 403  # Проверяем наличие статуса 4xx в ответе сервера и наличие ключа key в ответе#



# Проверяем что можно добавить питомца с некорректными данными#
def test_add_new_pet_with_valid_data(name='7@№2', animal_type='Болонка',
                                     age='1', pet_photo='images/Piki.jpg'):
    pet_photo = os.path.join(os.path.dirname('Piki.jpg'), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)  # Запрашиваем ключ auth_key#
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200  # Проверяем наличие статуса 200 в ответе сервера и наличие ключа key в ответе#
    assert result['name'] == name


def test_add_new_pet_with_valid_data(name='Пики', animal_type='Болонка',
                                     age='-1', pet_photo='images/Piki.jpg'):
    pet_photo = os.path.join(os.path.dirname('Piki.jpg'), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)  # Запрашиваем ключ auth_key#
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200  # Проверяем наличие статуса 200 в ответе сервера и наличие ключа key в ответе#
    assert result['name'] == name


    def test_add_new_pet_with_valid_data(name='Пики', animal_type='@42@',
                                         age='-1', pet_photo='images/Piki.jpg'):
        pet_photo = os.path.join(os.path.dirname('Piki.jpg'), pet_photo)
        _, auth_key = pf.get_api_key(valid_email, valid_password)  # Запрашиваем ключ auth_key#
        status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
        assert status == 200  # Проверяем наличие статуса 200 в ответе сервера и наличие ключа key в ответе#
        assert result['name'] == name



def test_add_new_pet_with_valid_data(name='Пики', animal_type='Болонка',
                                     age='-1', pet_photo='images/Пики.pdf'):
    pet_photo = os.path.join(os.path.dirname('Пики.pdf'), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)  # Запрашиваем ключ auth_key#
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 500  # Проверяем наличие статуса 500 в ответе сервера и наличие ключа key в ответе#



def test_delete_self_pet():
    _, face_auth_key = {'key': 'ea738148a1f19838e1c5d1413877f3691a3731380e733e877b0ae'}  # Вводим некорректный ключ auth_key#
    _, my_pets = pf.get_list_of_pets(face_auth_key, "my_pets")  # Запрашиваем список своих питомцев#
    pet_id = my_pets['pets'][0]['id']  # Берём id первого питомца из списка своих питомцев#
    status, result = pf.delete_pet(face_auth_key, pet_id)  # Отправляем запрос на удаление#
    assert status == 403  # Проверяем наличие статуса 200 в ответе сервера и наличие ключа key в ответе#



def test_delete_self_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)  # Запрашиваем ключ auth_key#
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets") # Запрашиваем список своих питомцев#
    pet_id = {'/6/15/+9408/47пз9Й48/РА/'}  # Берём id первого питомца из списка своих питомцев#
    status, result = pf.delete_pet(auth_key, pet_id)  # Отправляем запрос на удаление#
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')  # Запрашиваем список своих питомцев#
    assert status == 404  # Проверяем наличие статуса 200 в ответе сервера и наличие ключа key в ответе#









