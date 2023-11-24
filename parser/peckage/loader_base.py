import requests
from loguru import logger as log

class Loader:

    def __init__(self, data=None):
        self.data = data
        self.type_zapros(self.data)

    def post_zapros(self, data, header):
        req = requests.post(url=data['publicUrl'], json=self.data['body'], headers=header).content.decode('utf-8')
        return req

    def get_zapros(self, header):
        try:
            url = self.data['publicUrl']
            req = requests.get(url=url, headers=header).content.decode('utf-8')
            print(1)
            return req
        except Exception as error:
            log.info(error)
            header["X-Api-Key"] = 'p4ead4a57824d75bdc88702'
            return requests.get(url, headers=header).content.decode('utf-8')


    def type_zapros(self, data, header):
        if self.data['body'] == None:
            return self.get_zapros(header)
        else:
            return self.post_zapros(data, header)
