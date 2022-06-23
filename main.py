from telegram.ext import Updater, Dispatcher, CommandHandler, CallbackContext
from telegram.update import Update
import settings

updater = Updater(token=settings.TELEGRAM_TOKEN)


def start(update, context: CallbackContext):
    update.message.reply_text('Salom!')
    context.bot.send_message(
        chat_id=update.message.chat_id, text='Salom yana bir bor!')


dispatcher = updater.dispatcher
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()
