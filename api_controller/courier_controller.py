import requests
from helpers import GenerateData as GD
from api_controller.base_controller import BaseController
import allure
from data import TestLogin

class CourierController(BaseController):
    CREATE_COURIER_ENDPOINT = "api/v1/courier"
    LOGIN_COURIER_ENDPOINT = "api/v1/courier/login"

    @allure.step('Создание курьера со случайными данными')
    def create_courier_with_random_data(self):
        payload = GD()
        r = requests.post(self.get_url_with_endpoint(self.CREATE_COURIER_ENDPOINT), json=payload.create_full_courier_payload())
        return r

    @allure.step('Создание курьера и возврат данных по нему')
    def create_courier_and_return_data(self):
        payload = GD()
        payload = payload.create_full_courier_payload()
        r = requests.post(self.get_url_with_endpoint(self.CREATE_COURIER_ENDPOINT), json=payload)
        if r.status_code == 201:
            return payload
        else:
            return {}

    @allure.step('Создание курьера с указанными данными')
    def create_courier_with_expected_data(self, password, firstName, login):
        payload = {
             "firstName": firstName,
             "login": login,
             "password": password
        }
        r = requests.post(self.get_url_with_endpoint(self.CREATE_COURIER_ENDPOINT), json=payload)
        return r

    @allure.step('Запрос на создание курьера без обязательного атрибута - "Пароль"')
    def create_courier_without_password_negative(self):
        data = GD()
        payload = {
            "firstName": data.generate_random_string(5),
            "login": data.generate_random_email()
            }
        r = requests.post(self.get_url_with_endpoint(self.CREATE_COURIER_ENDPOINT), json=payload)
        return r

    @allure.step('Логин курьера с позитивными данными')
    def login_courier_positive(self, login, password):
        payload = {
            "login": login,
            "password": password
        }
        r = requests.post(self.get_url_with_endpoint(self.LOGIN_COURIER_ENDPOINT), json=payload)
        return r

    @allure.step('Логин курьера без обязательного поля - "Пароль"')
    def login_courier_without_login(self):
        payload = {
            "password": TestLogin.already_exists['password']
        }
        r = requests.post(self.get_url_with_endpoint(self.LOGIN_COURIER_ENDPOINT), json=payload)
        return r