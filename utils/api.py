from utils.http_methods import HttpMethods


"""Методы ля тестирования Google Maps API"""

base_url = 'https://rahulshettyacademy.com' # базовый URL
key = '?key=qaclick123' # параметр для всех запросов

class GoogleMapsAPI:

    @staticmethod
    def create_new_place():
        """Метод для создания новой локации"""

        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            },
            "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_resource = '/maps/api/place/add/json' # ресурс метода POST
        post_url = base_url + post_resource + key
        print(post_url)
        result_post = HttpMethods.post(post_url, json_for_create_new_place)
        print(result_post.text)
        return result_post


    @staticmethod
    def get_new_place(place_id):
        """Метод для проверки новой локации"""

        get_resource = '/maps/api/place/get/json' # ресурс метода GET
        get_url = base_url + get_resource + key + '&place_id=' + place_id
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get


    @staticmethod
    def put_new_place(place_id):
        """Метод для изменения новой локации"""

        json_for_update_new_place = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }

        put_resource = '/maps/api/place/update/json' # ресурс метода PUT
        put_url = base_url + put_resource + key
        print(put_url)
        result_put = HttpMethods.put(put_url, json_for_update_new_place)
        print(result_put.text)
        return result_put


    @staticmethod
    def delete_new_place(place_id):
        """Метод для удаления новой локации"""

        json_for_delete_new_place = {
            "place_id": place_id
        }

        delete_resource = '/maps/api/place/delete/json' # ресурс метода DELETE
        delete_url = base_url + delete_resource + key
        print(delete_url)
        result_delete = HttpMethods.delete(delete_url, json_for_delete_new_place)
        print(result_delete.text)
        return result_delete