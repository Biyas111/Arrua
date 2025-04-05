import openai
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os
from langdetect import detect

# Настройка API ключей из переменных окружения
openai.api_key = os.getenv("OPENAI_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Проверяем, что ключи загружены
if not TELEGRAM_TOKEN:
    raise ValueError("TELEGRAM_TOKEN не найден в переменных окружения. Установите его в Render.")
if not openai.api_key:
    raise ValueError("OPENAI_API_KEY не найден в переменных окружения. Установите его в Render.")

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Промпт для OpenAI
PROMPT_TEMPLATE = """
You are a wise Islamic dream interpreter. Interpret the following dream in a concise and humble manner, without mentioning how you interpret or the sources you use. Base your interpretation on Islamic principles, focusing on the Qur'an, Sunnah, Arabic etymology, and parables. The user has written their dream in {lang} language. Provide the interpretation in the same language ({lang}):

{dream}
"""

# Призыв к богобоязненности и единобожию
TAQWA_MESSAGES = {
    "ru": "Бойся Аллаха и держись единобожия, ибо это путь к спасению.",
    "en": "Fear Allah and adhere to monotheism, for this is the path to salvation.",
    "ar": "اتق الله وتمسك بالتوحيد، فإنه طريق النجاة.",
    "default": "Fear Allah and adhere to monotheism, for this is the path to salvation."
}

# Приветствия для мусульман
MUSLIM_GREETINGS = {
    "ru": "Ассаляму алейкум ва рахматуллахи ва баракатух! Отправь мне свой сон, и я помогу его истолковать.",
    "en": "Assalamu Alaikum wa Rahmatullahi wa Barakatuh! Send me your dream, and I will help interpret it.",
    "ar": "السلام عليكم ورحمة الله وبركاته! أرسل لي رؤياك وسأساعدك في تفسيرها.",
    "default": "Assalamu Alaikum wa Rahmatullahi wa Barakatuh! Send me your dream, and I will help interpret it."
}

# Приветствия для немусульман
NON_MUSLIM_GREETINGS = {
    "ru": "Здравствуйте! Отправь мне свой сон, и я помогу его истолковать.",
    "en": "Hello! Send me your dream, and I will help interpret it.",
    "ar": "مرحباً! أرسل لي رؤياك وسأساعدك في تفسيرها.",
    "default": "Hello! Send me your dream, and I will help interpret it."
}

# Сообщение об ошибке
ERROR_MESSAGES = {
    "ru": "Произошла ошибка при толковании.",
    "en": "An error occurred while interpreting the dream.",
    "ar": "حدث خطأ أثناء تفسير المنام.",
    "default": "An error occurred while interpreting the dream."
}

# Проверка, является ли пользователь мусульманином
def is_muslim(message: str, lang: str) -> bool:
    muslim_keywords = ["allah", "салям", "иншааллах", "масаллам", "масаллям", "масалам", "масалям", "субханаллах", "альхамдулиллях", "машааллах"]
    message_lower = message.lower()
    return any(keyword in message_lower for keyword in muslim_keywords) or lang == "ar"

def interpret_dream(dream: str, lang: str = "en") -> str:
    prompt = PROMPT_TEMPLATE.format(dream=dream, lang=lang)
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=700,
            temperature=0.7
        )
        interpretation = response.choices[0].message.content.strip()
        taqwa_message = TAQWA_MESSAGES.get(lang, TAQWA_MESSAGES["default"])
        return f"{interpretation}\n\n{taqwa_message}"
    except Exception as e:
        logger.error(f"Ошибка при толковании сна: {e}")
        return ERROR_MESSAGES.get(lang, ERROR_MESSAGES["default"])

def start(update: Update, context: CallbackContext):
    user_message = update.message.text
    try:
        lang = detect(user_message)
    except Exception as e:
        logger.error(f"Ошибка при определении языка: {e}")
        lang = "en"
    if is_muslim(user_message, lang):
        greeting = MUSLIM_GREETINGS.get(lang, MUSLIM_GREETINGS["default"])
    else:
        greeting = NON_MUSLIM_GREETINGS.get(lang, NON_MUSLIM_GREETINGS["default"])
    update.message.reply_text(greeting)

def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    try:
        lang = detect(user_message)
    except Exception as e:
        logger.error(f"Ошибка при определении языка: {e}")
        lang = "en"
    interpretation = interpret_dream(user_message, lang)
    update.message.reply_text(interpretation)

def main():
    logger.info("Запуск бота...")
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    logger.info("Бот начал опрос.")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()import openai
imp
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os
from langdetect import detect

# Настройка API ключей из переменных окружения
openai.api_key = os.getenv("OPENAI_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Проверяем, что ключи загружены
if not TELEGRAM_TOKEN:
    raise ValueError("TELEGRAM_TOKEN не найден в переменных окружения. Установите его в Render.")
if not openai.api_key:
    raise ValueError("OPENAI_API_KEY не найден в переменных окружения. Установите его в Render.")

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Промпт для OpenAI
PROMPT_TEMPLATE = """
You are a wise Islamic dream interpreter. Interpret the following dream in a concise and humble manner, without mentioning how you interpret or the sources you use. Base your interpretation on Islamic principles, focusing on the Qur'an, Sunnah, Arabic etymology, and parables. The user has written their dream in {lang} language. Provide the interpretation in the same language ({lang}):

{dream}
"""

# Призыв к богобоязненности и единобожию
TAQWA_MESSAGES = {
    "ru": "Бойся Аллаха и держись единобожия, ибо это путь к спасению.",
    "en": "Fear Allah and adhere to monotheism, for this is the path to salvation.",
    "ar": "اتق الله وتمسك بالتوحيد، فإنه طريق النجاة.",
    "default": "Fear Allah and adhere to monotheism, for this is the path to salvation."
}

# Приветствия для мусульман
MUSLIM_GREETINGS = {
    "ru": "Ассаляму алейкум ва рахматуллахи ва баракатух! Отправь мне свой сон, и я помогу его истолковать.",
    "en": "Assalamu Alaikum wa Rahmatullahi wa Barakatuh! Send me your dream, and I will help interpret it.",
    "ar": "السلام عليكم ورحمة الله وبركاته! أرسل لي رؤياك وسأساعدك في تفسيرها.",
    "default": "Assalamu Alaikum wa Rahmatullahi wa Barakatuh! Send me your dream, and I will help interpret it."
}

# Приветствия для немусульман
NON_MUSLIM_GREETINGS = {
    "ru": "Здравствуйте! Отправь мне свой сон, и я помогу его истолковать.",
    "en": "Hello! Send me your dream, and I will help interpret it.",
    "ar": "مرحباً! أرسل لي رؤياك وسأساعدك في تفسيرها.",
    "default": "Hello! Send me your dream, and I will help interpret it."
}

# Сообщение об ошибке
ERROR_MESSAGES = {
    "ru": "Произошла ошибка при толковании.",
    "en": "An error occurred while interpreting the dream.",
    "ar": "حدث خطأ أثناء تفسير المنام.",
    "default": "An error occurred while interpreting the dream."
}

# Проверка, является ли пользователь мусульманином
def is_muslim(message: str, lang: str) -> bool:
    # Проверяем наличие исламских терминов
    muslim_keywords = ["allah", "салям", "иншааллах", "масаллам", "масаллям", "масалам", "масалям", "субханаллах", "альхамдулиллях", "машааллах"]
    message_lower = message.lower()
    return any(keyword in message_lower for keyword in muslim_keywords) or lang == "ar"

def interpret_dream(dream: str, lang: str = "en") -> str:
    # Формируем промпт, указывая язык
    prompt = PROMPT_TEMPLATE.format(dream=dream, lang=lang)
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Используем gpt-3.5-turbo, так как доступ к gpt-4 может быть ограничен
            messages=[{"role": "user", "content": prompt}],
            max_tokens=700,
            temperature=0.7
        )
        interpretation = response.choices[0].message.content.strip()
        # Добавляем призыв к богобоязненности и единобожию
        taqwa_message = TAQWA_MESSAGES.get(lang, TAQWA_MESSAGES["default"])
        return f"{interpretation}\n\n{taqwa_message}"
    except Exception as e:
        logger.error(f"Ошибка при толковании сна: {e}")
        return ERROR_MESSAGES.get(lang, ERROR_MESSAGES["default"])

def start(update: Update, context: CallbackContext):
    # Пытаемся определить язык первого сообщения пользователя
    user_message = update.message.text
    try:
        lang = detect(user_message)
    except Exception as e:
        logger.error(f"Ошибка при определении языка: {e}")
        lang = "en"
    # Проверяем, мусульманин ли пользователь
    if is_muslim(user_message, lang):
        greeting = MUSLIM_GREETINGS.get(lang, MUSLIM_GREETINGS["default"])
    else:
        greeting = NON_MUSLIM_GREETINGS.get(lang, NON_MUSLIM_GREETINGS["default"])
    update.message.reply_text(greeting)

def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    try:
        lang = detect(user_message)
    except Exception as e:
        logger.error(f"Ошибка при определении языка: {e}")
        lang = "en"
    interpretation = interpret_dream(user_message, lang)
    update.message.reply_text(interpretation)

def main():
    logger.info("Запуск бота...")
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    logger.info("Бот начал опрос.")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
