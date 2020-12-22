import logging, os, telegram
from telegram.ext import Updater, CommandHandler
import nekos, requests, re, random, sys

#Config logging

logging.basicConfig(
    level = logging.INFO, format="%(asctime) - %(name)s - %(levelname)s - %(message)s,"
)

logger = logging.getLogger()

#Ask Token
TOKEN = os.getenv("TOKEN")
mode = os.getenv("MODE")

if mode == "dev":
    def run(updater):
        updater.start_polling()
        updater.idle()
elif mode == "prod":
    def run(updater):
        PORT = int(os.environ.get("PORT","8443"))
        HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
        updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
        updater.bot.set_webhook(f"https://{HEROKU_APP_NAME}.herokuapp.com/{TOKEN}")
else:
    logger.info('Mode not specified.')
    sys.exit()

def help(update, context):
    update.message.reply_text("""
                              Senpai, estos son los comandos u//u: \n /help - Mostrar los comandos \n /doggo - Foto random de un doggo \n /neko - Foto random de un neko \n /hentai - NFSW ;) \n /oilo - Oilo \n /pat - uwu \n /baka - Baka >_< \n /hey - Hey, loco, que pasa valemia \n /navidad - la navidad es todo aquello \n /quien - Quién monda es Dorian? \n /buenosdias - Ohayo, darin! (Chayanne) \n /buenasnoches - Piolin te desea buenas noches \n /princesas - Comando especial para Valeria
                              """)

def get_url(identifier):
    if identifier == 0:
        contents = requests.get('https://random.dog/woof.json').json()
        url = contents['url']
        return url
    else:
        contents = requests.get('http://aws.random.cat//meow').json()
        url = contents['file']
        return url

def get_image_url(identifier):
    allowed_extension = ['jpg', 'jpeg', 'png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url(identifier)
        if identifier == 0:
            file_extension = re.search("([^.]*)$", url).group(1).lower()
        else:
            file_extension = re.search("([^.]*)$", url).group(0).lower()
    return url

def doggo(update, context):
    url = get_image_url(0)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=url)

def  neko(update, context):
    url = get_image_url(1)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=url)

def random_target():
    possible = ['feet', 'yuri', 'trap', 'futanari', 'hololewd', 'lewdkemo',
                'cum', 'erokemo', 'les', 'lewdk', 'ngif', 'lewd', 'feed',
                'gecg', 'eroyuri', 'eron', 'cum_jpg', 'nsfw_neko_gif', 'solo', 'kemonomimi',
                'nsfw_avatar', 'anal', 'erofeet', 'blowjob', 'pussy', 'tits', 'holoero', 'pussy_jpg',
                'waifu', 'kiss', 'femdom', 'neko', 'spank', 'cuddle', 'erok', 'fox_girl', 'boobs',
                'random_hentai_gif', 'smallboobs', 'ero']
    return random.choice(possible)


def hentai(update, context):
    context.bot.send_photo(
        chat_id=update.effective_chat.id, photo=nekos.img(random_target()))

def oilo(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=nekos.img('smug'))
    
def pat(update, context):
    user = update.message.from_user
    if len(context.args) != 0:
        update.message.reply_text('@' + user['username'] + ' is patting ' + context.args[0] + ' uwu')
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=nekos.img('pat'))
    else:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=nekos.img('pat'))

def baka(update, context):
    user = update.message.from_user
    if len(context.args) != 0:
        update.message.reply_text('B-b-baka, '+ context.args[0] + ' ! >_<')
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=nekos.img('baka'))
    else:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=nekos.img('baka'))
    
def hey(update, context):
    context.bot.send_video(chat_id=update.message.chat_id, video=open('./media/Hey.mp4', 'rb'), supports_streaming=True)

def navidad(update, context):
    update.message.reply_text('Feliz navidad, s-senpai! uwu')
    context.bot.send_audio(chat_id=update.message.chat_id, audio=open('./media/Navidad.mp3', 'rb'))

def quien(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text='Quién?')
    context.bot.send_audio(chat_id=update.message.chat_id, audio=open('media/Quien.mp3', 'rb'))

def buenosdias(update,context):
    file = random.choice(os.listdir('media/chayanne'))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('media/chayanne/'+file, 'rb'))
    
def buenasnoches(update, context):
    file = random.choice(os.listdir('media/buenas_noches'))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('media/buenas_noches/'+file, 'rb'))

def princesas(update, context):
    context.bot.send_video(chat_id=update.message.chat_id, video=open('media/Princesas.mp4', 'rb'), supports_streaming=True)

def main():
    Boturu = telegram.Bot(token = TOKEN)
    updater = Updater(Boturu.token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('doggo', doggo))
    dp.add_handler(CommandHandler('neko', neko))
    dp.add_handler(CommandHandler('hentai', hentai))
    dp.add_handler(CommandHandler('oilo', oilo))
    dp.add_handler(CommandHandler('pat', pat))
    dp.add_handler(CommandHandler('baka', baka))
    dp.add_handler(CommandHandler('hey', hey))
    dp.add_handler(CommandHandler('navidad', navidad))
    dp.add_handler(CommandHandler('quien', quien))
    dp.add_handler(CommandHandler('buenosdias', buenosdias))
    dp.add_handler(CommandHandler('buenasnoches', buenasnoches))
    dp.add_handler(CommandHandler('princesas', princesas))
    run(updater)
    
if __name__ == '__main__':
    main()
