from django.core.management.base import BaseCommand
from django.conf import settings
import requests
from telegram import Bot, Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telebot.models import Pupil, Teacher
import logging
from telegram.ext import (
    CommandHandler, Updater, Filters, MessageHandler, ConversationHandler
)

cat_url = 'https://api.thecatapi.com/v1/images/search'
dog_url = 'https://api.thedogapi.com/v1/images/search'

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


CODE, NAME_SURNAME, COMMUNICATE, FUNC = range(4)


def start_bot(update, context):
    '''Начало работы с ботом'''
    chat = update.effective_chat
    user_id = update.message.chat.id
    if user_id == int(settings.ADMIN_ID):
        text = 'Привет, Иван!'
        context.bot.send_message(chat_id=chat.id, text=text)
        logging.info('Админ прошел валидацию')
        return COMMUNICATE  # ConversationHandler.END
    elif any([
        Pupil.objects.filter(profile_id=user_id).exists(),
        Teacher.objects.filter(profile_id=user_id).exists()
    ]):
        text = 'Напиши начать'
        context.bot.send_message(chat_id=chat.id, text=text)
        return COMMUNICATE
    else:
        name = update.message.chat.first_name
        text = f'Приветствую, {name}! Для доступа к сервису необходимо ввести код'
        context.bot.send_message(chat_id=chat.id, text=text)
        return CODE


def code_validation(update, context):
    '''Проверка корректности кода доступа'''
    code = update.message.text
    chat = update.effective_chat
    name = update.message.chat.first_name
    surname = update.message.chat.last_name
    if code == settings.REG_CODE:
        logging.info(f'{name, surname} ввел верный код')
        text = 'Код верный. Введи фамилию и имя'
        context.bot.send_message(chat_id=chat.id, text=text)
        return NAME_SURNAME
    else:
        text = 'код неверный, в доступе отказано'
        context.bot.send_message(chat_id=chat.id, text=text)
        return CODE


def user_registration(update, context):
    '''Регистрация пользователя в БД'''
    name_surname = update.message.text.split()
    chat = update.effective_chat
    pupil, _ = Pupil.objects.get_or_create(
        profile_id=update.message.chat.id,
        defaults={
            'profile_id': update.message.chat_id,
            'name': name_surname[1],
            'surname': name_surname[0],
        }
    )
    logging.info(f'{name_surname} зарегистрировался')
    text = f'{name_surname[1]} успешно зарегистрирован для получения кодов. Напиши начать'
    context.bot.send_message(chat_id=chat.id, text=text)
    return COMMUNICATE


def cancel(update, _):
    '''Отмена регистрации'''
    user = update.message.from_user
    logger.info("Пользователь %s отменил регистрацию.", user.first_name)
    update.message.reply_text(
        'Регистрация отменена',
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


def communicate(update, context):
    chat = update.effective_chat
    button = ReplyKeyboardMarkup([
        ['/cat'], ['/dog'],
        ['/cancel']
    ], resize_keyboard=True)
    text = 'Только зарегистрированным пользователям я отправляю кошечек и собачек.'
    context.bot.send_message(chat_id=chat.id,
                             text=text,
                             reply_markup=button
                             )
    return FUNC


def get_new_image():
    try:
        response = requests.get(cat_url)
    except Exception as error:
        logging.error(f'Ошибка при запросе к основному API: {error}')
        response = requests.get(dog_url)
    response = response.json()
    random_pic = response[0].get('url')
    return random_pic


def new_cat(update, context):
    try:
        response = requests.get(cat_url)
    except Exception as error:
        logging.error(f'Ошибка при запросе к основному API: {error}')
        response = requests.get(dog_url)
    response = response.json()
    random_pic = response[0].get('url')
    chat = update.effective_chat
    context.bot.send_photo(chat.id, random_pic)


def new_dog(update, context):
    try:
        response = requests.get(dog_url)
    except Exception as error:
        logging.error(f'Ошибка при запросе к основному API: {error}')
        response = requests.get(cat_url)
    response = response.json()
    random_pic = response[0].get('url')
    chat = update.effective_chat
    context.bot.send_photo(chat.id, random_pic)


class Command(BaseCommand):
    help = 'Телеграм бот'

    def handle(self, *args, **options):
        updater = Updater(token=settings.BOT_TOKEN)
        dispatcher = updater.dispatcher
        registration_handler = ConversationHandler(
            entry_points=[CommandHandler('start', start_bot)],
            states={
                CODE: [MessageHandler(Filters.text, code_validation)],
                NAME_SURNAME: [MessageHandler(
                    Filters.text, user_registration)],
                COMMUNICATE: [
                    MessageHandler(Filters.text, communicate)],
                FUNC: [
                    CommandHandler('cat', new_cat),
                    CommandHandler('dog', new_dog)
                ]
            },
            fallbacks=[CommandHandler('cancel', cancel)],  # не работает
        )
        dispatcher.add_handler(registration_handler)
        updater.start_polling()
        updater.idle()

    
