import re


class Validator:

    @staticmethod
    def validate_email(email):

        pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

        return re.match(pattern, email) is not None


    @staticmethod
    def validate_phone(phone):

        phone = str(phone)

        pattern = r'^[6-9][0-9]{9}$'

        return re.match(pattern, phone) is not None


    @staticmethod
    def validate_password(password):

        pattern = r'^(?=.*[A-Za-z])(?=.*\d).{6,}$'

        return re.match(pattern, password) is not None


    @staticmethod
    def validate_username(username):

        pattern = r'^[A-Za-z][A-Za-z0-9_]{2,}$'

        return re.match(pattern, username) is not None
    
    @staticmethod
    def validate_role(role):

      role = role.lower()

      if role in ["admin", "customer"]:
        return True

        return False