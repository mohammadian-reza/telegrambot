from telegram.ext import Updater, CommandHandler
updater = Updater('246550078:AAHZx2ZgxsHx4MreteCFTd3F5y5RHrQzfXM')

def sendsticker_method(bot , update):
    chat_id = update.message.chat_id
    sticker = open('E:\mypic.webp', 'rb')
    bot.sendSticker(chat_id, sticker)
    sticker.close()

send_command= CommandHandler('sendsticker', sendsticker_method )
updater.dispatcher.add_handler(send_command)
updater.start_polling()

# for exit
updater.idle()
