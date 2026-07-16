import jwt
import datetime


class JWTManager:

    SECRET_KEY = "food_delivery_secret_key"

    @staticmethod
    def generate_token(user_id, username, role):

        payload = {
            "user_id": user_id,
            "username": username,
            "role": role,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }

        token = jwt.encode(
            payload,
            JWTManager.SECRET_KEY,
            algorithm="HS256"
        )

        return token

    @staticmethod
    def verify_token(token):

        try:

            payload = jwt.decode(
                token,
                JWTManager.SECRET_KEY,
                algorithms=["HS256"]
            )

            return payload

        except jwt.ExpiredSignatureError:
            print("Token Expired.")
            return None

        except jwt.InvalidTokenError:
            print("Invalid Token.")
            return None