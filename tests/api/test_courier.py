import allure
from api_controller.courier_controller import CourierController as CC
from validation_data import CourierValidation as CV
from data import TestLogin as TL
from helpers import GenerateData as GD


class TestCourierCreate:
    # /api/v1/courier

    @allure.title('Создание курьера')
    def test_create_courier_positive(self):
        controller = CC()
        r = controller.create_courier_with_random_data()

        assert r.status_code == 201
        assert r.json() ==  CV.CREATE_COURIER_SUCCESS

    @allure.title('Создание курьера, который уже создан')
    def test_create_courier_already_exist(self):
        controller = CC()
        data = controller.create_courier_and_return_data()
        assert data is not None, 'Не удалось создать пользователя'
        r = controller.create_courier_with_expected_data(login=data.get('login'), firstName=data.get('firstName'), password=data.get('password'))

        assert r.status_code == 409
        assert r.json()['message'] == CV.COURIER_ALREADY_EXIST['message']
        assert r.json()['code'] == CV.COURIER_ALREADY_EXIST['code']

    @allure.title('Создание курьера без обязательного аттрибута')
    def test_create_courier_missing_required_attributes(self):
        controller = CC()
        r = controller.create_courier_without_password_negative()

        assert r.status_code == 400
        assert r.json()['message'] == CV.CREATE_COURIER_BAD_REQUEST['message']

class TestLoginCourier:
    # /api/v1/courier/login

    @allure.title('Логин существующего курьера')
    def test_courier_login_positive(self):
        controller = CC()
        r = controller.login_courier_positive(login=TL.already_exists.get('login'), password=TL.already_exists.get('password'))

        assert r.status_code == 200
        assert type(r.json()['id']) == type(CV.LOGIN_COURIER_SUCCESS['id'])

    @allure.title('Логин несуществующего курьера')
    def test_courier_login_wrong_data(self):
        controller = CC()
        data = GD()
        r = controller.login_courier_positive(login=data.generate_random_email(), password=data.generate_random_digits(5))
    
        assert r.status_code == 404
        assert r.json()['message'] == CV.LOGIN_COURIER_WRONG_DATA['message']

    @allure.title('Логин курьера без обязательного аттрибута')
    def test_login_courier_missing_required_attributes(self):
        controller = CC()
        r = controller.login_courier_without_login()
         
        assert r.status_code == 400
        assert r.json()['message'] == CV.LOGIN_COURIER_BAD_REQUEST['message']
