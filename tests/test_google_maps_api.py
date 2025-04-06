import pytest
import allure
from utils.api import GoogleMapsAPI
from utils.checking import Checking
import json

# token = json.loads(result_post.text)
# print(list(token))

@allure.epic('Test create place')
class TestCreatePlace:
    """Создание, изменение, удаление новой локации"""

    @allure.description('Test create, update, delete new place')
    def test_create_new_place(self):

        print('Метод POST')
        result_post = GoogleMapsAPI.create_new_place()
        check_post = result_post.json()
        place_id = check_post['place_id']
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(
            result_post,
            [
                'status',
                'place_id',
                'scope',
                'reference',
                'id'
            ]
        )
        Checking.check_json_value(result_post, 'status', 'OK')


        print('Метод GET POST')
        result_get = GoogleMapsAPI.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(
            result_get,
            [
                'location',
                'accuracy',
                'name',
                'phone_number',
                'address',
                'types',
                'website',
                'language'
            ]
        )
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')


        print('Метод PUT')
        result_put = GoogleMapsAPI.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')


        print('Метод GET PUT')
        result_get = GoogleMapsAPI.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(
            result_get,
            [
                'location',
                'accuracy',
                'name',
                'phone_number',
                'address',
                'types',
                'website',
                'language'
            ]
        )
        Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')


        print('Метод DELETE')
        result_delete = GoogleMapsAPI.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')


        print('Метод GET DELETE')
        result_get = GoogleMapsAPI.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ['msg'])
        Checking.check_json_search_word_in_value(result_get, 'msg', 'failed')


        print('Тестирование создания, изменения, удаления новой локации прошло успешно!')