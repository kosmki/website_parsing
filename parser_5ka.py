import requests
import json
import time


class Parser5ka:
    def __init__(self, start_url, params):
        self.url = start_url
        self.params = params

    def parse(self):
        while self.url:
            response: requests.Response = requests.get(self.url, params=self.params, headers=headers)
            if response.status_code == 200:
                print('url is opened')

            # сбор данных
            data = response.json()
            for product in data.get('results'):
                self.save_products(product)
                print(product.get('name'))

            # переход к следующей странице,если она есть
            self.url = data.get('next')
            if self.url:
                time.sleep(0.2)
                self.parse()

    def save_products(self, product: dict):
        with open(f'result/{str(product["id"]).replace("/", "")}.json', 'w', encoding='UTF-8') as file:
            json.dump(product, file, ensure_ascii=False)


if __name__ == '__main__':
    url = 'https://5ka.ru/api/v2/special_offers/'
    params = {'records_per_page': 12, }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",
    }

    parser = Parser5ka(url, params)
    parser.parse()
