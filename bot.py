from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

TOKEN = "ВАШ_НОВЫЙ_ТОКЕН"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привет!\n\n"
        "Доступные команды:\n"
        "/help\n"
        "/yesno\n"
        "/number\n"
        "/coin"
    )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Запустить бота\n"
        "/help - Помощь\n"
        "/yesno - Ответить Да или Нет\n"
        "/number - Случайное число\n"
        "/coin - Орёл или Решка"
    )

async def yesno(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(["✅ Да", "❌ Нет"]))

async def number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 2:
        await update.message.reply_text("Напиши так: /number 1 100")
        return

    try:
        a = int(context.args[0])
        b = int(context.args[1])

        if a > b:
            a, b = b, a

        await update.message.reply_text(f"🎲 {random.randint(a, b)}")

    except ValueError:
        await update.message.reply_text("Нужно ввести два числа.")

async def coin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(["🦅 Орёл", "🪙 Решка"]))

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("yesno", yesno))
app.add_handler(CommandHandler("number", number))
app.add_handler(CommandHandler("coin", coin))

app.run_polling()
