from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я работаю 24/7 на Render!")

app = ApplicationBuilder().token("8224724997:AAE896Cj7cFM5Hy0H1AEQBSDfv61oLd-_yY").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
