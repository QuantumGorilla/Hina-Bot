from telegram.ext import Updater, CommandHandler
import nekos, requests, re, random


def help(update, context):
    update.message.reply_text("""
                              Senpai, esto son los comandos u//u: 
                              \n /help - Mostrar los comandos
                              \n /doggo - Foto random de un doggo
                              \n /neko - Foto random de un neko
                              \n /hentai - NFSW ;)
                              """)

def random_target():
    possible = ['feet', 'yuri', 'trap', 'futanari', 'hololewd', 'lewdkemo',
                'cum', 'erokemo', 'les', 'wallpaper', 'lewdk', 'ngif', 'lewd', 'feed',
                'gecg', 'eroyuri', 'eron', 'cum_jpg', 'nsfw_neko_gif', 'solo', 'kemonomimi',
                'nsfw_avatar', 'anal', 'erofeet', 'blowjob', 'pussy', 'tits', 'holoero', 'pussy_jpg',
                'waifu', 'kiss', 'femdom', 'neko', 'spank', 'cuddle', 'erok', 'fox_girl', 'boobs',
                'random_hentai_gif', 'smallboobs', 'ero']
    return random.choice(possible)


def hentai(update, context):
    context.bot.send_photo(
        chat_id=update.effective_chat.id, photo=nekos.img(random_target()))
    
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

def main():
    updater = Updater(
        token='1443354425:AAF5mOMsV6lGXJXDGMv7bDAM6-YYeJp_UnA', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('doggo', doggo))
    dp.add_handler(CommandHandler('neko', neko))
    dp.add_handler(CommandHandler('hentai', hentai))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
