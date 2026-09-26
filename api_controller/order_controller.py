import requests
from helpers import GenerateData as GD
from api_controller.base_controller import BaseController
import allure

class OrderController(BaseController):
    CREATE_AN_ORDER = "api/v1/orders"
    GET_AN_ORDER_LIST = "api/v1/orders"

    @allure.step('Создание заказа с рандомными значениями')
    def create_an_order_with_random_data(self):
        payload = GD()
        r = requests.post(self.get_url_with_endpoint(self.CREATE_AN_ORDER), json=payload.create_full_courier_payload())
        return r

    @allure.step('Создание заказа с выбором цвета')
    def create_an_order_with_expected_color(self, color):
        payload = GD()
        payload = payload.create_full_courier_payload()
        payload.update({"color": color})
        r = requests.post(self.get_url_with_endpoint(self.CREATE_AN_ORDER), json=payload)
        return r

    @allure.step('Получение списка заказов')
    def get_an_order_list(self):
        r = requests.get(self.get_url_with_endpoint(self.GET_AN_ORDER_LIST))
        return r