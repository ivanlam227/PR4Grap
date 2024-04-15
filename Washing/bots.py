import telebot
import config
from keyboards import MarkupBuilder
from validators import InputValidator

class WashingMachine:
    def __init__(self, brand, model, serial_number):
        self.brand = brand
        self.model = model
        self.serial_number = serial_number
        self.parts = []

    def add_part(self, part_name):
        self.parts.append(part_name)

    def remove_part(self, part_name):
        if part_name in self.parts:
            self.parts.remove(part_name)
            return True
        else:
            return False

    def list_parts(self):
        return self.parts

class BotHandler:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token, skip_pending=True)
        self.washing_machines = {}

    def start(self):
        @self.bot.message_handler(commands=['start', 'help'])
        def send_welcome(message):
            self.bot.reply_to(message, "Привет! Я бот для учета комплектующих стиральных машин. Используй кнопки ниже:", reply_markup=MarkupBuilder.main_markup())

        @self.bot.message_handler(func=lambda message: message.text == "👤 Зарегистрировать стиральную машину")
        def register_washing_machine(message):
            self.bot.reply_to(message, "Введите бренд стиральной машины:")
            self.bot.register_next_step_handler(message, self.process_brand_step)

        @self.bot.message_handler(func=lambda message: message.text == "➕ Добавить комплектующую")
        def add_part(message):
            self.bot.reply_to(message, "Введите название комплектующей:")
            self.bot.register_next_step_handler(message, self.process_add_part_step)

        @self.bot.message_handler(func=lambda message: message.text == "➖ Удалить комплектующую")
        def remove_part(message):
            self.bot.reply_to(message, "Введите название комплектующей для удаления:")
            self.bot.register_next_step_handler(message, self.process_remove_part_step)

        @self.bot.message_handler(func=lambda message: message.text == "📋 Список комплектующих")
        def list_parts(message):
            if not self.washing_machines:
                self.bot.send_message(message.chat.id, "Список стиральных машин пуст.")
                return
            if not message.chat.id in self.washing_machines:
                self.bot.send_message(message.chat.id, "Сначала зарегистрируйте стиральную машину с помощью кнопки '👤 Зарегистрировать стиральную машину'.")
                return
            washing_machine = self.washing_machines[message.chat.id]
            parts = washing_machine.list_parts()
            if parts:
                self.bot.send_message(message.chat.id, "Список комплектующих:")
                for part in parts:
                    self.bot.send_message(message.chat.id, part)
            else:
                self.bot.send_message(message.chat.id, "Список комплектующих пуст.")

        self.bot.polling()

    def process_brand_step(self, message):
        try:
            brand = message.text
            if not InputValidator.is_valid_brand(brand):
                self.bot.send_message(message.chat.id, "Некорректный бренд. Попробуйте снова.")
                return self.register_washing_machine(message)
            self.bot.reply_to(message, "Введите модель стиральной машины:")
            self.bot.register_next_step_handler(message, self.process_model_step, brand)
        except Exception as e:
            self.bot.reply_to(message, 'Ошибка:\n' + str(e))

    def process_model_step(self, message, brand):
        try:
            model = message.text
            if not InputValidator.is_valid_model(model):
                self.bot.send_message(message.chat.id, "Некорректная модель. Попробуйте снова.")
                return self.process_brand_step(message, brand)
            self.bot.reply_to(message, "Введите серийный номер стиральной машины:")
            self.bot.register_next_step_handler(message, self.process_serial_number_step, brand, model)
        except Exception as e:
            self.bot.reply_to(message, 'Ошибка:\n' + str(e))

    def process_serial_number_step(self, message, brand, model):
        try:
            serial_number = message.text
            if not InputValidator.is_valid_serial_number(serial_number):
                self.bot.send_message(message.chat.id, "Некорректный серийный номер. Попробуйте снова.")
                return self.process_model_step(message, brand)
            self.washing_machines[message.chat.id] = WashingMachine(brand, model, serial_number)
            self.bot.send_message(message.chat.id, "Строительная машина успешно зарегистрирована.")
        except Exception as e:
            self.bot.reply_to(message, 'Ошибка:\n' + str(e))

    def process_add_part_step(self, message):
        try:
            part_name = message.text
            if not message.chat.id in self.washing_machines:
                self.bot.send_message(message.chat.id, "Сначала зарегистрируйте стиральную машину с помощью кнопки '👤 Зарегистрировать стиральную машину'.")
                return
            washing_machine = self.washing_machines[message.chat.id]
            washing_machine.add_part(part_name)
            self.bot.send_message(message.chat.id, f"Комплектующая '{part_name}' успешно добавлена к стиральной машине.")
        except Exception as e:
            self.bot.reply_to(message, 'Ошибка:\n' + str(e))
            self.bot.register_next_step_handler(message, self.process_add_part_step)  # Регистрируем обработчик снова

    def process_remove_part_step(self, message):
        try:
            part_name = message.text
            if not message.chat.id in self.washing_machines:
                self.bot.send_message(message.chat.id, "Сначала зарегистрируйте стиральную машину с помощью кнопки '👤 Зарегистрировать стиральную машину'.")
                return
            washing_machine = self.washing_machines[message.chat.id]
            if washing_machine.remove_part(part_name):
                self.bot.send_message(message.chat.id, f"Комплектующая '{part_name}' успешно удалена.")
            else:
                self.bot.send_message(message.chat.id, f"Комплектующей '{part_name}' нет в списке.")
                self.bot.send_message(message.chat.id, "Введите название комплектующей для удаления:")
                self.bot.register_next_step_handler(message, self.process_remove_part_step)  # Регистрируем обработчик снова
                return
        except Exception as e:
            self.bot.reply_to(message, 'Ошибка:\n' + str(e))
            self.bot.send_message(message.chat.id, "Введите название комплектующей для удаления:")
            self.bot.register_next_step_handler(message, self.process_remove_part_step)  # Регистрируем обработчик снова

if __name__ == "__main__":
    bot_handler = BotHandler(config.TOKEN)
    bot_handler.start()
