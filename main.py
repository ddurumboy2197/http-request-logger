import datetime
import jwt

class SessionManager:
    def __init__(self, secret_key, expiry_minutes):
        self.secret_key = secret_key
        self.expiry_minutes = expiry_minutes

    def generate_token(self, user_id):
        payload = {
            'user_id': user_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=self.expiry_minutes)
        }
        return jwt.encode(payload, self.secret_key, algorithm='HS256')

    def verify_token(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return payload['user_id']
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None

# Misol
session_manager = SessionManager('secret_key', 30)  # 30 daqiqa muddatga token yaratadi
token = session_manager.generate_token(1)
print(token)

user_id = session_manager.verify_token(token)
print(user_id)
```

Kodda quyidagilar mavjud:

- `SessionManager` klassi yaratildi, u session yaratish va tokenni tekshirish uchun metodlarni o'z ichiga oladi.
- `generate_token` metodida token yaratish uchun payload yaratiladi, u user_id va tokenning muddati (exp) ni o'z ichiga oladi.
- `verify_token` metodida tokenni tekshirish uchun payload yaratiladi, u tokenni tekshiradi va user_id qaytaradi. Agar token muddati tugagan bo'lsa, None qaytaradi.
- Misolda `SessionManager` klassi yaratiladi, token yaratiladi va tokenni tekshirish uchun metodni chaqiriladi.
