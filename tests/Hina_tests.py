from telegram.ext import Updater, CommandHandler
import nekos, requests, re, random, os

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
    if len(context.args) != 0:
        update.message.reply_text('B-b-baka, '+ context.args[0] + ' ! >_<')
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=nekos.img('baka'))
    else:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=nekos.img('baka'))
    
def hey(update, context):
    context.bot.send_video(chat_id=update.effective_chat.id, video=open('media/Hey.mp4', 'rb'), supports_streaming=True)

def navidad(update, context):
    update.message.reply_text('Feliz navidad, s-senpai! uwu')
    context.bot.send_audio(chat_id=update.effective_chat.id, audio=open('media/Navidad.mp3', 'rb'))
    
def quien(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Quién?')
    context.bot.send_audio(chat_id=update.message.chat_id, audio=open('media/Quien.mp3', 'rb'))

def buenosdias(update,context):
    file = random.choice(os.listdir('media/chayanne'))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('media/chayanne/'+file, 'rb'))
    
def buenasnoches(update, context):
    file = random.choice(os.listdir('media/buenas_noches'))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('media/buenas_noches/'+file, 'rb'))
    
def princesas(update, context):
    context.bot.send_video(chat_id=update.effective_chat.id, video=open('media/Princesas.mp4', 'rb'), supports_streaming=True)

def despegala(update, context):
    try:    
        user = update.message.reply_to_message
        context.bot.send_message(chat_id=update.effective_chat.id, text='Omae wa mou... Shindeiru')
        context.bot.kickChatMember(chat_id=update.effective_chat.id, user_id=user.from_user['id'])
    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Hpta, el cv es admin')
    
def main():
    updater = Updater(token='TOKEN', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('despegala', despegala))
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()