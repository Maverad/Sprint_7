from helpers import GenerateData as GD

class BaseController:
    MAIN_URL = "https://qa-scooter.education-services.ru/"

    def get_url_with_endpoint(self, endpoint):
        return self.MAIN_URL + endpoint
