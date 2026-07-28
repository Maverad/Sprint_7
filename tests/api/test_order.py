import allure
from api_controller.order_controller import OrderController as OC
from validation_data import OrderValidation as OV
import pytest

class TestOrder:
    # POST /api/v1/orders  and   GET /api/v1/orders

    @allure.title('Создание заказа с рандомными значениями')
    def test_create_an_order(self):
        controller = OC()
        r = controller.create_an_order_with_random_data()

        assert r.status_code == 201
        assert type(r.json().get('track')) is type(OV.CREATE_AN_ORDER['track'])

    @allure.title('Создание заказа с различным цветом')
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], [], ['BLACK', 'GREY']])
    def test_create_an_order_with_different_colors(self, color):
        controller = OC()
        r = controller.create_an_order_with_expected_color(color)

        assert r.status_code == 201
        assert type(r.json().get('track')) is type(OV.CREATE_AN_ORDER['track'])


    @allure.title('Проверка списка заказов')
    def test_an_order_list(self):
        controller = OC()
        r = controller.get_an_order_list()
        data = r.json()

        assert r.status_code == 200
        assert 'orders' in data