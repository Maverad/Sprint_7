import random
import string

class GenerateData:

    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    
    def generate_random_digits(self, length):
        letters = string.digits
        random_digits = ''.join(random.choice(letters) for i in range(length))
        return random_digits
    
    def generate_random_email(self):
        return self.generate_random_string(5) + "@" + self.generate_random_string(3) + ".ru"
        
    def create_full_courier_payload(self):
        payload = {}
        payload.update({"firstName": self.generate_random_string(5), "password": self.generate_random_digits(5),"login": self.generate_random_email()})
        return payload

    def create_full_order_payload(self):
        payload_order = (
            {
                "firstName": self.generate_random_string(7),
                "lastName": self.generate_random_string(6),
                "address": self.generate_random_string(7) + self.generate_random_string(5),
                "metroStation": f"{random.randint(1, 50)}",
                "phone": "7" + self.generate_random_digits(11),
                "rentTime": random.randint(1, 7),
                "deliveryDate": "2027-06-06",
                "comment": self.generate_random_string(10) + self.generate_random_string(6),
                "color": []
            }
        )
        return payload_order
