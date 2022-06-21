from importlib.metadata import entry_points
import os
import time
import requests
from dotenv import load_dotenv
from telegram.ext import CommandHandler, Updater, Filters, MessageHandler, ConversationHandler
import logging
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update


load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    filename='program.log',
    filemode='w',
    format='%(asctime)s - %(levelname)s - %(message)s - %(name)s'
)
logger = logging.getLogger(__name__)
logger.addHandler(
    logging.StreamHandler()
)

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID')
REG_CODE = os.getenv('REG_CODE')

CODE, NAME_SURNAME = range(2)


def start_bot(update, context):
    chat = update.effective_chat
    user_id = update.message.chat.id
    if user_id == int(ADMIN_ID):
        text = 'Привет, Иван!'
        context.bot.send_message(chat_id=chat.id, text=text)
        logging.info('Админ прошел валидацию')
        return ConversationHandler.END
    else:
        name = update.message.chat.first_name
        text = f'Приветствую, {name}! Напиши код доступа'
        context.bot.send_message(chat_id=chat.id, text=text)
        return CODE


def code_validation(update, context):
    code = update.message.text
    chat = update.effective_chat
    name = update.message.chat.first_name
    surname = update.message.chat.last_name
    if code == REG_CODE:
        logging.info(f'{name, surname} ввел верный код')
        text = 'Код верный. Введи фамилию и имя'
        context.bot.send_message(chat_id=chat.id, text=text)
        return NAME_SURNAME
    else:
        text = 'код неверный, в доступе отказано'
        context.bot.send_message(chat_id=chat.id, text=text)
        return CODE


def user_registration(update, context):
    name_surname = update.message.text
    chat = update.effective_chat
    logging.info(f'{name_surname} зарегистрировался')
    text = f'{name_surname} успешно зарегистрирован для получения кодов'
    context.bot.send_message(chat_id=chat.id, text=text)
    return ConversationHandler.END


def cancel(update, _):
    user = update.message.from_user
    logger.info("Пользователь %s отменил регистрацию.", user.first_name)
    update.message.reply_text(
        'Регистрация отменена',
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


if __name__ == '__main__':

    updater = Updater(token=BOT_TOKEN)
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start_bot)],
        states={
            CODE: [MessageHandler(Filters.text, code_validation)],
            NAME_SURNAME: [MessageHandler(Filters.text, user_registration)],
            },
        fallbacks=[CommandHandler('cancel', cancel)], #не работает
        )
    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()
