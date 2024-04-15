from telebot import types

class MarkupBuilder:
    @staticmethod
    def main_markup():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("👤 Зарегистрировать стиральную машину")
        item2 = types.KeyboardButton("➕ Добавить комплектующую")
        item3 = types.KeyboardButton("➖ Удалить комплектующую")
        item4 = types.KeyboardButton("📋 Список комплектующих")
        markup.add(item1, item2, item3, item4)
        return markup
