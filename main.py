from telegram.ext import Updater, Dispatcher, CommandHandler, CallbackContext
from telegram.update import Update
import requests
import settings



updater = Updater(token=settings.TELEGRAM_TOKEN)


def start(update, context: CallbackContext):
    update.message.reply_text("Assalamu Alaykum! Wikipediyadan ma'lumot qidiruvchi"
                              " botga hush kelibsiz! Biron nima izlash uchun /search"
                              " va so'rovingizni yozing. Misol /search Amir Temur")


def search(update: Update, cotext: CallbackContext):
    args= cotext.args
    search_text= ' '.join(args)
    response=requests.get('https://en.wikipedia.org/w/appi.php',{
        'action':'opensearch',
        'search': search_text,
        'limit': 1,
        'namespace': 0,
        'format': 'json',
    })

    result=response.json()
    print(result)

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('search', search))

updater.start_polling()
updater.idle()
