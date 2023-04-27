
class Util:

    @staticmethod
    def validate_phone_number(number):
        if number.isdigit():
            return True
        else:
            return False
