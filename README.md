# Telegram Bot - 24/7 на Railway ☁️

Готовый шаблон Telegram бота для развертывания на облаке Railway.

## ✨ Что получаешь

- ✅ Готовый код бота на Python
- ✅ Работает 24/7 на облаке
- ✅ Простая настройка
- ✅ Примеры команд (/start, /help, /info)
- ✅ Обработка текстовых сообщений

## 📋 Требования

- GitHub аккаунт (бесплатно)
- Railway аккаунт (есть бесплатный лимит)
- Токен от Telegram @BotFather

## 🚀 Быстрый старт

### 1. Получи токен бота

```
Напиши @BotFather в Telegram
Выбери /newbot
Дай имя и username
Скопируй токен
```

### 2. Загрузи на GitHub

```bash
git clone https://github.com/твой-юзер/telegram-bot.git
cd telegram-bot
git add .
git commit -m "Initial commit"
git push origin main
```

### 3. Развер на Railway

1. Открой railway.app
2. Sign in with GitHub
3. "+ New Project" → "Deploy from GitHub repo"
4. Выбери этот репо
5. Добавь переменную:
   - `TELEGRAM_BOT_TOKEN` = твой_токен

### 4. Готово! 🎉

Бот работает 24/7. Тестируй в Telegram!

## 📁 Структура файлов

```
.
├── bot.py              # Основной код бота
├── requirements.txt    # Зависимости Python
├── Procfile           # Инструкция для Railway
├── .gitignore         # Что не коммитить
├── .env.example       # Пример переменных
└── README.md          # Этот файл
```

## 🔧 Локальное тестирование

```bash
# Установи зависимости
pip install -r requirements.txt

# Создай .env файл
cp .env.example .env
# Отредактируй .env и добавь свой токен

# Запусти бота
python bot.py
```

## 📝 Команды бота

- `/start` - Начать
- `/help` - Справка
- `/info` - Информация о боте
- Любое сообщение - бот повторит его

## 🛠️ Кастомизация

Отредактируй `bot.py` для своих команд:

```python
async def my_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Твой текст здесь")

# Добавь в main():
application.add_handler(CommandHandler("mycommand", my_command))
```

## 💡 Советы

- Никогда не коммит `.env` файл!
- Используй `.env.example` как шаблон
- Все переменные окружения в Railway
- Смотри логи в Railway при ошибках

## 📚 Документация

- [python-telegram-bot](https://python-telegram-bot.readthedocs.io/)
- [Railway Docs](https://docs.railway.app/)
- [Telegram Bot API](https://core.telegram.org/bots/api)

## 📞 Проблемы?

1. Проверь логи в Railway
2. Убедись что токен верный
3. Смотри requirements.txt - все ли установлено
4. Коммитить только код, не .env!

---

Удачи! 🚀 Если что-то не работает - спроси в чате!
