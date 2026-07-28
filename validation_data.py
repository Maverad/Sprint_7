class CourierValidation:
    #Success
    CREATE_COURIER_SUCCESS = {"ok": True}
    LOGIN_COURIER_SUCCESS = {'id': 1}

    #Errors
    COURIER_ALREADY_EXIST = {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}
    LOGIN_COURIER_WRONG_DATA = {"message": "Учетная запись не найдена"}
    CREATE_COURIER_BAD_REQUEST = {"message": "Недостаточно данных для создания учетной записи"}
    LOGIN_COURIER_BAD_REQUEST = {"message": "Недостаточно данных для входа"}


class OrderValidation:
    #Success
    CREATE_AN_ORDER = {'track': 1}