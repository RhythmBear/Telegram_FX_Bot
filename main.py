import logging
from credentials import Token
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler
from responses import start, reverse

print("bot has started running")
# Creating a logger to be able to monitor bot processes
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


# Building the application
if __name__ == '__main__':
    app = ApplicationBuilder().token(Token).build()

    start_handler = CommandHandler('start', start)
    message_handler = MessageHandler(filters.TEXT, reverse)
    app.add_handler(start_handler)
    app.add_handler(message_handler)

    app.run_polling()
    print("Bot is running...")




