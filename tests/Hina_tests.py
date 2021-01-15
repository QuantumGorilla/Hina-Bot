import telegram
from telegram.ext import Updater, CommandHandler
import nekos, random


def random_target():
    possible = ['feet', 'yuri', 'trap', 'futanari', 'hololewd', 'lewdkemo',
                'cum', 'erokemo', 'les', 'lewdk', 'lewd', 'eroyuri', 'eron', 
                'cum_jpg', 'nsfw_neko_gif', 'solo', 'anal', 'blowjob', 'pussy', 
                'tits', 'holoero', 'pussy_jpg', 'femdom', 'spank', 'erok', 'boobs',
                'ero']
    return random.choice(possible)

def hentai(update, context):
    context.bot.send_photo(
        chat_id=update.effective_chat.id, photo=nekos.img(random_target()))
    
def main():
    updater = Updater(token='1448142051:AAFGjpOMeUn8Cat2pDIMKUAragLVgFkXaMQ', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('hentai', hentai))
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()