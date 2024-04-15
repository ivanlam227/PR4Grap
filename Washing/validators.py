class InputValidator:
    @staticmethod
    def is_valid_brand(brand):
        return brand.strip() != ""

    @staticmethod
    def is_valid_model(model):
        return model.strip() != ""

    @staticmethod
    def is_valid_serial_number(serial_number):
        return serial_number.strip() != ""
