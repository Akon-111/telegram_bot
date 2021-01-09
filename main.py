from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, ConversationHandler, MessageHandler,Filters
from covid19 import Covid19

buttons = ReplyKeyboardMarkup([[ 'Statistika'],['Dunyo']], resize_keyboard = True)
covid = Covid19() 

def start(update,context):
    update.message.reply_html(
    	'<b>Assalomu alaykum, {}</b>\n \nMen Koronavirus statistikasi haqida ma"lumot beruvchi botman'.format(update.message.from_user.first_name), reply_markup = buttons)
    return 1

def stats (update,context):
	data = covid.getByCountryCode("UZ")
	update.message.reply_html(
		'🇺🇿<b>O"zbekistonda</b>\n \n<b>Yuqtirganlar:</b> {}\n <b>Sog"ayganlar: </b>{}\n<b> Vafot etganlar:</b> {}'.
		format(
		data['confirmed'],
		data['recovered'],
        data['deaths']), 
        reply_markup = buttons)


def world (update,context):
	data = covid.getLatest()
	update.message.reply_html(
		'🌎<b>Dunyoda</b>\n \n<b>Yuqtirganlar:</b>{}\n<b>Sogayganlar:</b>{}\n<b>Vafot etganlar:</b>[}'.format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths'])
         ), reply_markup = buttons)


updater = Updater('1581441216:AAG-sHW2QLxWFPmAO2dIe5vr8SxS2-yWfjU', use_context=True)
conv_handler = ConversationHandler(
	entry_points = [CommandHandler('start',start)],
    states={
        1:[
            MessageHandler(Filters.regex('^(Statistika)$'),stats),
            MessageHandler(Filters.regex('^(Dunyo)$'),world),
        ]
    }, 
    fallbacks = [MessageHandler(Filters.text,start)]
    )


updater.dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()