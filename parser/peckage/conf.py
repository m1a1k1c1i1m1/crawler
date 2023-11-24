import json

body = {
    "page": 1,
    "properties": [
        {
            "name": "price_currency",
            "value": 2
        }
    ],
    "sorting": 1
}

URL_CARS = 'https://api.av.by/offer-types/cars/filters/main/apply'
URL_PHONE = 'https://api.av.by/offers/{}/phones'
TODO_DIR = 'todo/'
PAGE_DIR = 'page/'
CAR_DIR = 'CAR/'
HEDERS = {
    "content-type": "application/json"
}


class Setings:

    def first_page(self):
        data_page = {
            'page_all_flag': False,
            'type_page': 'cars',
            'body': body,
            'publicUrl': URL_CARS,
            'headers': HEDERS,
            'name_todo': str(body['page'])
        }
        return data_page

    def all_data_page(self):
        all_data_page = {
            'page_all_flag': True,
            'type_page': 'cars',
            'body': body,
            'headers': HEDERS,
            'publicUrl': URL_CARS,
            'name_todo': str(body['page'])
        }
        return all_data_page

    def format_json(self, data):
        try:
            new_value = dict()
            usd = data['price']['usd']['amount']
            byn = data['price']['byn']['amount']
            new_car = data['properties']
            for items in new_car:
                key_name = items['name']
                value = items['value']
                if value != True:
                    new_value.update({f'{key_name}': value})
            new_value.update({
                'locationName': data['locationName'],
                'sellerName': data['sellerName'],
                'refreshedAt': data['refreshedAt'],
                'publishedAt': data['publishedAt'],
                'publicUrl': data['publicUrl'],
                'price_byn': byn,
                'price_usd': usd,
                'name_todo': str(data['id'])
            })
            return new_value
        except Exception as error:
            print(error)

    def json_content(self, req, data):
        json_content = {
            'name': data['name_todo'],
            'content': json.loads(req),
            'type_page': data['type_page'],
            'page_all_flag': data['page_all_flag']
        }
        return json_content

    def todo_phone(self, id_car, url):
        json_content = {
            'name_todo': url,
            'type_page': "phone",
            'publicUrl': URL_PHONE.format(id_car),
            'page_all_flag': False,
            'headers': HEDERS,
            'body': None,
        }
        return json_content

    def json_phone(self, data, number):
        json_content = {
            'content': data,
            'number': number
        }
        return json_content
