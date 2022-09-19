from pip._vendor import requests
from pprint import pprint
import time 
import json 

class Vk_Ya_Api:
    def __init__(self, token_vk, token_ya):
        self.token_vk = token_vk 
        self.token_ya = token_ya

    def get_photos(self, url, vk_id):
        resalt_list = []
        url = url
        params = {
            'owner_id': vk_id,
            'album_id': 'profile',
            'access_token': token_vk_1,
            'count': 5,
            'extended': 1,
            'v': '5.131'
        }
        res = requests.get(url + 'photos.get', params = params).json()
        res = res["response"]["items"]
        for str_ in res:
            for resp in str_["sizes"]:
                if resp["type"] == 'z':
                    resalt_list.append({"file_name" : f'{str_["likes"]["count"]}' + ".jpg", "sizes": resp['url']})  
        with open('jp.json', 'w') as f: 
            json.dump(resalt_list, f, ensure_ascii=False, indent=4)

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token_ya)}

    def upload(self, file_path):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': file_path, 'overwrite': 'True'}
        headers = self.get_headers()
        link_dickt = requests.get(url, headers = headers, params = params).json()
        href = link_dickt.get('href', '')
        post_ = requests.put(href, data = open(file_path, 'rb'))
        return print(post_.status_code)        



if __name__ == '__main__':
    token_vk_1 = ''
    token_ya_1 = ''
    url = 'https://api.vk.com/method/'
    vk_id_1 =  
    Nurkov = Vk_Ya_Api(token_vk_1, token_ya_1)
    Nurkov.get_photos(url, vk_id_1)
    Nurkov.get_headers()
    Nurkov.upload("jp.json")



