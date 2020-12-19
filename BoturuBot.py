from telegram.ext import Updater, CommandHandler
from telegram import ChatAction
import requests 
import re

def help(update, context):
    update.message.reply_text('Senpai, esto son los comandos u//u: \n /help \n /doggo')

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def doggo(update, context):
    url=get_image_url()
    context.bot.send_photo(chat_id=update.effective_chat.id, photo = url)

def main():
    updater = Updater(token='1443354425:AAF5mOMsV6lGXJXDGMv7bDAM6-YYeJp_UnA', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('doggo', doggo))
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()