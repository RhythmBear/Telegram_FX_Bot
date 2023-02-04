from datetime import datetime as dt
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update._effective_chat.id,
        text="Hey {}, You've reached your personal FX assistant, How may I help you?"
    )

async def reverse(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    reversed_text = user_input[::-1]
    await context.bot.send_message(
        chat_id=update._effective_chat.id, text=reversed_text
        )
