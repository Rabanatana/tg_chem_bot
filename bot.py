from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from conf import TOKEN 
import analysis

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Я - бот для анализа химических соединений. \
Отправь мне строку SMILES или InChi и я расчитаю\
некоторые из их свойств и построю 2D-структуру.')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(analysis.find_props(update.message.text))



def main():

    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Бот работает, ошибок нет")
    application.run_polling()

if __name__ == '__main__':
    main()
