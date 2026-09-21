import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

# Загрузить переменные из .env
load_dotenv()

# Включить логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Получить токен из переменной окружения
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN не найден в переменных окружения!")

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Ответить на /start"""
    user = update.effective_user
    await update.message.reply_text(
        f"Привет, {user.mention_html()}! 👋\n\n"
        f"Я твой бот и работаю 24/7 на облаке! 🚀\n\n"
        f"Команды:\n"
        f"/start - главное меню\n"
        f"/help - справка\n"
        f"/info - информация\n",
        parse_mode='HTML'
    )

# Обработчик команды /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправить справку"""
    help_text = """
📖 Справка по командам:

/start - начать
/help - эта справка
/info - информация о боте

Также ты можешь написать мне любое сообщение, и я его повторю!
    """
    await update.message.reply_text(help_text)

# Обработчик команды /info
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправить информацию о боте"""
    info_text = """
ℹ️ Информация о боте:

🤖 Это Telegram бот
☁️ Работает на Railway 24/7
🐍 Написан на Python
💪 Всегда онлайн и готов помогать!
    """
    await update.message.reply_text(info_text)

# Обработчик всех текстовых сообщений
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Повторить сообщение пользователя"""
    user_text = update.message.text
    await update.message.reply_text(f"Ты написал: {user_text}")

# Обработчик ошибок
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Логирование ошибок"""
    logger.error(f"Exception while handling an update: {context.error}")

def main() -> None:
    """Запустить бота"""
    # Создать приложение
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Добавить обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("info", info))

    # Добавить обработчик текстовых сообщений (должен быть в конце)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Добавить обработчик ошибок
    application.add_error_handler(error_handler)

    # Запустить бота (polling mode)
    logger.info("Бот запущен! Нажми Ctrl+C чтобы остановить.")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
