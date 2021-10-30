
import os
from typing import List
from telegram.ext import CallbackContext
import nekos
import requests
import re
import random

from Hina import Command


def get_url(identifier):
    if identifier == 0:
        contents = requests.get("https://random.dog/woof.json").json()
        url = contents["url"]
        return url
    else:
        contents = requests.get("http://aws.random.cat//meow").json()
        url = contents["file"]
        return url


def get_image_url(identifier):
    allowed_extension = ["jpg", "jpeg", "png"]
    file_extension = ""
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


def neko(update, context):
    url = get_image_url(1)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=url)


def random_target():
    possible = ["feet", "yuri", "trap", "futanari", "hololewd", "lewdkemo",
                "cum", "erokemo", "les", "lewdk", "lewd", "eroyuri", "eron",
                "cum_jpg", "nsfw_neko_gif", "solo", "anal", "blowjob", "pussy",
                "tits", "holoero", "pussy_jpg", "femdom", "spank", "erok", "boobs",
                "ero"]
    return random.choice(possible)


def hentai(update, context):
    context.bot.send_photo(
        chat_id=update.effective_chat.id, photo=nekos.img(random_target()))


def dollar(update, context):
    context.bot.send_photo(
        chat_id=update.effective_chat.id, photo=nekos.img("gecg"))


def oilo(update, context):
    context.bot.send_photo(
        chat_id=update.effective_chat.id, photo=nekos.img("smug"))


def pat(update, context: CallbackContext):
    reply_user = update.message.reply_to_message
    user = update.message.from_user
    if reply_user == None:
        if len(context.args) != 0:
            word = " "
            context.bot.send_message(chat_id=update.effective_chat.id, text="@" +
                                     user["username"] + " is patting " + word.join(context.args) + " uwu")
            context.bot.send_photo(
                chat_id=update.effective_chat.id, photo=nekos.img("pat"))
        else:
            context.bot.send_photo(
                chat_id=update.effective_chat.id, photo=nekos.img("pat"))
    else:
        if reply_user.from_user["username"] == None:
            context.bot.send_message(chat_id=update.effective_chat.id, text="@" +
                                     user["username"] + " is patting " + reply_user.from_user["first_name"] + " uwu")
            context.bot.send_photo(
                chat_id=update.effective_chat.id, photo=nekos.img("pat"))
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="@" +
                                     user["username"] + " is patting " + reply_user.from_user["first_name"] + " " + "(@" + reply_user.from_user["username"] + ")" + " uwu")
            context.bot.send_photo(
                chat_id=update.effective_chat.id, photo=nekos.img("pat"))


def baka(update, context):
    reply_user = update.message.reply_to_message
    if reply_user == None:
        if len(context.args) != 0:
            word = " "
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="B-b-baka, " + word.join(context.args) + " ! >_<")
            context.bot.send_photo(
                chat_id=update.effective_chat.id, photo=nekos.img("baka"))
        else:
            context.bot.send_photo(
                chat_id=update.effective_chat.id, photo=nekos.img("baka"))
    else:
        if reply_user.from_user["username"] == None:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="B-b-baka, " + reply_user.from_user["first_name"] + " ! >_<")
            context.bot.send_photo(
                chat_id=update.effective_chat.id, photo=nekos.img("baka"))
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="B-b-baka, " +
                                     reply_user.from_user["first_name"] + "(@" + reply_user.from_user["username"] + ")" + " ! >_<")
            context.bot.send_photo(
                chat_id=update.effective_chat.id, photo=nekos.img("baka"))


def hey(update, context):
    context.bot.send_video(chat_id=update.effective_chat.id, video=open(
        "./media/Hey.mp4", "rb"), supports_streaming=True)


def navidad(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Feliz navidad, s-senpai! uwu")
    context.bot.send_audio(chat_id=update.effective_chat.id,
                           audio=open("./media/Navidad.mp3", "rb"))


def quien(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Quién?")
    context.bot.send_video(chat_id=update.effective_chat.id, video=open(
        "./media/Quien.mp4", "rb"), supports_streaming=True)


def buenosdias(update, context):
    file = random.choice(os.listdir("media/chayanne"))
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=open("./media/chayanne/"+file, "rb"))


def buenasnoches(update, context):
    file = random.choice(os.listdir("media/buenas_noches"))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(
        "./media/buenas_noches/"+file, "rb"))


def princesas(update, context):
    context.bot.send_video(chat_id=update.effective_chat.id, video=open(
        "./media/Princesas.mp4", "rb"), supports_streaming=True)


def noticias(update, context):
    file = random.choice(os.listdir("media/noticias"))
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=open("./media/noticias/"+file, "rb"))


def despegala(update, context):
    try:
        reply_user = update.message.reply_to_message
        if reply_user != None:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="Omae wa mou... Shindeiru")
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(
                "./media/Shindeiru.png", "rb"))
            context.bot.kickChatMember(
                chat_id=update.effective_chat.id, user_id=reply_user.from_user["id"])
        else:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="No mandaste a despegarla a nadie, cachón")
    except:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(
            "./media/Hina-fail-ban.jpg", "rb"))
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="Hpta, el cv es admin")


def butifarra(update, context):
    reply_user = update.message.reply_to_message
    if reply_user == None:
        if len(context.args) != 0:
            word = " "
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="Hey, " + word.join(context.args))
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/Butifarra.mp4", "rb"), supports_streaming=True)
        else:
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/Butifarra.mp4", "rb"), supports_streaming=True)
    else:
        if reply_user.from_user["username"] == None:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="Hey, " + reply_user.from_user["first_name"])
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/Butifarra.mp4", "rb"), supports_streaming=True)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Hey, " +
                                     reply_user.from_user["first_name"] + " " + "(@" + reply_user.from_user["username"]+")")
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/Butifarra.mp4", "rb"), supports_streaming=True)


def comedia(update, context):
    reply_user = update.message.reply_to_message
    file = random.choice(os.listdir("media/comedia"))
    if reply_user == None:
        if len(context.args) != 0:
            word = " "
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Jajaja cule chiste hpta, " + word.join(context.args) + ", cv")
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(
                "./media/comedia/"+file, "rb"))
        else:
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(
                "./media/comedia/"+file, "rb"))
    else:
        if reply_user.from_user["username"] == None:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Jajaja cule chiste hpta, " + reply_user.from_user["first_name"] + ", cv")
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(
                "./media/comedia/"+file, "rb"))
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Jajaja cule chiste hpta, " +
                                     reply_user.from_user["first_name"] + " " + "(@" + reply_user.from_user["username"]+")" + ", cv")
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(
                "./media/comedia/"+file, "rb"))


def mimir(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Hora de mimir! uwu")
    context.bot.send_video(chat_id=update.effective_chat.id, video=open(
        "./media/Mimir.mp4", "rb"), supports_streaming=True)


def die(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Solo quiero morir :(")
    context.bot.send_video(chat_id=update.effective_chat.id, video=open(
        "./media/Die.mp4", "rb"), supports_streaming=True)


def trece(update, context):
    reply_user = update.message.reply_to_message
    if reply_user == None:
        if len(context.args) != 0:
            word = " "
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Uy, pah, LO DIJITEEEEEE " + "(" + word.join(context.args) + ")")
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/Trece.mp4", "rb"), supports_streaming=True)
        else:
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/Trece.mp4", "rb"), supports_streaming=True)
    else:
        if reply_user.from_user["username"] == None:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Uy, pah, LO DIJITEEEEEE " + "(" + reply_user.from_user["first_name"] + ")")
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/Trece.mp4", "rb"), supports_streaming=True)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Uy, pah, LO DIJITEEEEEE " + "(@" + reply_user.from_user["username"] + ")")
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/Trece.mp4", "rb"), supports_streaming=True)


def respete(update, context):
    reply_user = update.message.reply_to_message
    if reply_user == None:
        if len(context.args) != 0:
            word = " "
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Respeta, " + word.join(context.args) + ", cachón")
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/Respete.mp4", "rb"), supports_streaming=True)
        else:
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/Respete.mp4", "rb"), supports_streaming=True)
    else:
        if reply_user.from_user["username"] == None:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Respeta, " + reply_user.from_user["first_name"] + ", cachón")
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/Respete.mp4", "rb"), supports_streaming=True)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Respeta, " +
                                     reply_user.from_user["first_name"] + " (@" + reply_user.from_user["username"] + "), cachón")
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/Respete.mp4", "rb"), supports_streaming=True)


def escribe_bien(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Escribe bien, cachón")
    context.bot.send_video(chat_id=update.effective_chat.id, video=open(
        "./media/EscribeBien.mp4", "rb"), supports_streaming=True)


def no(update, context):
    file = random.choice(os.listdir("media/no"))
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=open("./media/no/"+file, "rb"))


def si(update, context):
    file = random.choice(os.listdir("media/yes"))
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=open("./media/yes/"+file, "rb"))


def simp(update, context):
    reply_user = update.message.reply_to_message
    file = random.choice(os.listdir("media/simp"))
    if reply_user == None:
        if len(context.args) != 0:
            word = " "
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="SIMP, " + word.join(context.args))
            context.bot.send_photo(
                chat_id=update.effective_chat.id, photo=open("./media/simp/"+file, "rb"))
        else:
            context.bot.send_photo(
                chat_id=update.effective_chat.id, photo=open("./media/simp/"+file, "rb"))
    else:
        if reply_user.from_user["username"] == None:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="SIMP, " + reply_user.from_user["first_name"])
            context.bot.send_photo(
                chat_id=update.effective_chat.id, photo=open("./media/simp/"+file, "rb"))
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="SIMP, " +
                                     reply_user.from_user["first_name"] + " (@" + reply_user.from_user["username"] + ")")
            context.bot.send_photo(
                chat_id=update.effective_chat.id, photo=open("./media/simp/"+file, "rb"))


def ayno(update, context):
    context.bot.send_video(chat_id=update.effective_chat.id, video=open(
        "./media/Ayno.mp4", "rb"), supports_streaming=True)


def bye(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="La despego, chao, cachones")
    context.bot.send_video(chat_id=update.effective_chat.id, video=open(
        "./media/Bye.mp4", "rb"), supports_streaming=True)


def perro(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Perro con perro, perro con perro")
    context.bot.send_video(chat_id=update.effective_chat.id, video=open(
        "./media/Perro.mp4", "rb"), supports_streaming=True)


def cagaste(update, context):
    reply_user = update.message.reply_to_message
    file = random.choice(os.listdir("media/cagaste"))
    if reply_user == None:
        if len(context.args) != 0:
            word = " "
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="Cagaste, " + word.join(context.args))
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(
                "./media/cagaste/"+file, "rb"))
        else:
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(
                "./media/cagaste/"+file, "rb"))
    else:
        if reply_user.from_user["username"] == None:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="Cagaste, " + reply_user.from_user["first_name"])
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(
                "./media/cagaste/"+file, "rb"))
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Cagaste, " +
                                     reply_user.from_user["first_name"] + " (@" + reply_user.from_user["username"] + ")")
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(
                "./media/cagaste/"+file, "rb"))


def fino(update, context):
    reply_user = update.message.reply_to_message
    file = random.choice(os.listdir("media/fino"))
    if reply_user == None:
        if len(context.args) != 0:
            word = " "
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="Fino, mi rey (" + word.join(context.args) + ")")
            context.bot.send_photo(
                chat_id=update.effective_chat.id, photo=open("./media/fino/"+file, "rb"))
        else:
            context.bot.send_photo(
                chat_id=update.effective_chat.id, photo=open("./media/fino/"+file, "rb"))
    else:
        if reply_user.from_user["username"] == None:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Fino, mi rey (" + reply_user.from_user["first_name"] + ")")
            context.bot.send_photo(
                chat_id=update.effective_chat.id, photo=open("./media/fino/"+file, "rb"))
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Fino, mi rey (@" + reply_user.from_user["username"] + ")")
            context.bot.send_photo(
                chat_id=update.effective_chat.id, photo=open("./media/fino/"+file, "rb"))


def re_scream(update, context):
    file = random.choice(os.listdir("media/re"))
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
    if "mp3" in file:
        context.bot.send_audio(
            chat_id=update.effective_chat.id, audio=open("./media/re/"+file, "rb"))
    else:
        context.bot.send_video(chat_id=update.effective_chat.id, video=open(
            "./media/re/"+file, "rb"), supports_streaming=True)


def abueno(update, context):
    reply_user = update.message.reply_to_message
    file = random.choice(os.listdir("media/abueno"))
    if reply_user == None:
        if len(context.args) != 0:
            word = " "
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Te me cuidas, crack (" + word.join(context.args) + ")")
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(
                "./media/abueno/"+file, "rb"))
        else:
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(
                "./media/abueno/"+file, "rb"))
    else:
        if reply_user.from_user["username"] == None:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Te me cuidas, crack (" + reply_user.from_user["first_name"] + ")")
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(
                "./media/abueno/"+file, "rb"))
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Te me cuidas, crack (@" + reply_user.from_user["username"] + ")")
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(
                "./media/abueno/"+file, "rb"))


def callese(update, context):
    reply_user = update.message.reply_to_message
    file = random.choice(os.listdir("media/callese"))
    if reply_user == None:
        if len(context.args) != 0:
            word = " "
            context.bot.send_message(chat_id=update.effective_chat.id, text="Callese, " +
                                     word.join(context.args) + ", me tiene jodidamente mamado")
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/callese/"+file, "rb"), supports_streaming=True)
        else:
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/callese/"+file, "rb"), supports_streaming=True)
    else:
        if reply_user.from_user["username"] == None:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Callese, " +
                                     reply_user.from_user["first_name"] + ", me tiene jodidamente mamado")
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/callese/"+file, "rb"), supports_streaming=True)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Callese, " +
                                     reply_user.from_user["first_name"] + " (@" + reply_user.from_user["username"] + "), me tiene jodidamente mamado")
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/callese/"+file, "rb"), supports_streaming=True)


def horny(update, context):
    file = random.choice(os.listdir("media/horny"))
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Estoy horny.")
    context.bot.send_video(chat_id=update.effective_chat.id, video=open(
        "./media/horny/"+file, "rb"), supports_streaming=True)


def meto(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="A ti también te la meto")
    context.bot.send_video(chat_id=update.effective_chat.id, video=open(
        "./media/Meto.mp4", "rb"), supports_streaming=True)


def rico(update, context):
    file = random.choice(os.listdir("media/rico"))
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Rico hpta")
    context.bot.send_video(chat_id=update.effective_chat.id, video=open(
        "./media/rico/"+file, "rb"), supports_streaming=True)


def kya(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Kya~")
    context.bot.send_video(chat_id=update.effective_chat.id, video=open(
        "./media/Kya.mp4", "rb"), supports_streaming=True)


def dato(update, context):
    reply_user = update.message.reply_to_message
    file = random.choice(os.listdir("media/dato"))
    if reply_user == None:
        if len(context.args) != 0:
            word = " "
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Datazo, crack, pero nadie te pregunto, cv (" + word.join(context.args) + ")")
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/dato/"+file, "rb"), supports_streaming=True)
        else:
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/dato/"+file, "rb"), supports_streaming=True)
    else:
        if reply_user.from_user["username"] == None:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Datazo, crack, pero nadie te pregunto, cv (" + reply_user.from_user["first_name"] + ")")
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/dato/"+file, "rb"), supports_streaming=True)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Datazo, crack, pero nadie te pregunto, cv (@" + reply_user.from_user["username"] + ")")
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/dato/"+file, "rb"), supports_streaming=True)


def antojaron(update, context):
    file = random.choice(os.listdir("media/antojaron"))
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Ya antojaron")
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=open("./media/antojaron/"+file, "rb"))


def chirrete(update, context):
    context.bot.send_video(chat_id=update.effective_chat.id, video=open(
        "./media/Chirrete.mp4", "rb"), supports_streaming=True)


def decepcion(update, context):
    reply_user = update.message.reply_to_message
    if reply_user == None:
        if len(context.args) != 0:
            word = " "
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="Decepcionado de ti, " + word.join(context.args))
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/Decepcion.mp4", "rb"), supports_streaming=True)
        else:
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/Decepcion.mp4", "rb"), supports_streaming=True)
    else:
        if reply_user.from_user["username"] == None:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Decepcionado de ti, " + reply_user.from_user["first_name"])
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/Decepcion.mp4", "rb"), supports_streaming=True)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Decepcionado de ti, " +
                                     reply_user.from_user["first_name"] + " (@" + reply_user.from_user["username"] + ")")
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/Decepcion.mp4", "rb"), supports_streaming=True)


def tragatela(update, context):
    reply_user = update.message.reply_to_message
    file = random.choice(os.listdir("media/tragatela"))
    if reply_user == None:
        if len(context.args) != 0:
            word = " "
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Bueno, tragatela (" + word.join(context.args) + ")")
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/tragatela/" + file, "rb"), supports_streaming=True)
        else:
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/tragatela/" + file, "rb"), supports_streaming=True)
    else:
        if reply_user.from_user["username"] == None:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Tragatela, " +
                                     reply_user.from_user["first_name"] + ", ya, tragatela")
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/tragatela/" + file, "rb"), supports_streaming=True)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Tragatela, " +
                                     reply_user.from_user["first_name"] + " (@" + reply_user.from_user["username"] + "), ya, tragatela")
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/tragatela/" + file, "rb"), supports_streaming=True)


def sapo(update, context):
    reply_user = update.message.reply_to_message
    file = random.choice(os.listdir("media/sapo"))
    if reply_user == None:
        if len(context.args) != 0:
            word = " "
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="Cule sapo, " + word.join(context.args))
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/sapo/"+file, "rb"), supports_streaming=True)
        else:
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/sapo/"+file, "rb"), supports_streaming=True)
    else:
        if reply_user.from_user["username"] == None:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Cule sapo, " + reply_user.from_user["first_name"])
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/sapo/"+file, "rb"), supports_streaming=True)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Cule sapo, " +
                                     reply_user.from_user["first_name"] + " (@" + reply_user.from_user["username"] + ")")
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/sapo/"+file, "rb"), supports_streaming=True)


def hya(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="#HYYYYYAAAAAAA_POSTING")
    context.bot.send_video(chat_id=update.effective_chat.id, video=open(
        "./media/Hya.mp4", "rb"), supports_streaming=True)


def marica(update, context):
    reply_user = update.message.reply_to_message
    file = random.choice(os.listdir("media/marica"))
    if reply_user == None:
        if len(context.args) != 0:
            word = " "
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="MMMMMJUMMMMMMM (" + word.join(context.args) + ")")
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/marica/"+file, "rb"), supports_streaming=True)
        else:
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/marica/"+file, "rb"), supports_streaming=True)
    else:
        if reply_user.from_user["username"] == None:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="MMMMMJUMMMMMMM (" + reply_user.from_user["first_name"] + ")")
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/marica/"+file, "rb"), supports_streaming=True)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="MMMMMJUMMMMMMM (@" + reply_user.from_user["username"] + ")")
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/marica/"+file, "rb"), supports_streaming=True)


def chad(update, context):
    context.bot.send_video(chat_id=update.effective_chat.id, video=open(
        "./media/Chad.mp4", "rb"), supports_streaming=True)


def risa(update, context):
    reply_user = update.message.reply_to_message
    if reply_user == None:
        if len(context.args) != 0:
            word = " "
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="Cule risa, " + word.join(context.args))
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/Risa.mp4", "rb"), supports_streaming=True)
        else:
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/Risa.mp4", "rb"), supports_streaming=True)
    else:
        if reply_user.from_user["username"] == None:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Cule risa, " + reply_user.from_user["first_name"])
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/Risa.mp4", "rb"), supports_streaming=True)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Cule risa, @" + reply_user.from_user["username"])
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/Risa.mp4", "rb"), supports_streaming=True)


def come(update, context):
    reply_user = update.message.reply_to_message
    if reply_user == None:
        if len(context.args) != 0:
            word = " "
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="Vaya a come monda, " + word.join(context.args))
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/Come.mp4", "rb"), supports_streaming=True)
        else:
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/Come.mp4", "rb"), supports_streaming=True)
    else:
        if reply_user.from_user["username"] == None:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Vaya a come monda, " + reply_user.from_user["first_name"])
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/Come.mp4", "rb"), supports_streaming=True)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Vaya a come monda, @" +
                                     reply_user.from_user["username"] + "(" + reply_user.from_user["first_name"] + ")")
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/Come.mp4", "rb"), supports_streaming=True)


def siono(update, context):
    response = requests.get("https://yesno.wtf/api").json()
    answer = "Sí" if response["answer"] == "yes" else "No"
    image_url = response["image"]
    context.bot.send_animation(
        chat_id=update.effective_chat.id, animation=image_url, caption=answer)


def foxy(update, context):
    response = requests.get(
        "https://randomfox.ca/floof/?ref=apilist.fun").json()
    image_url = response["image"]
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=image_url)


def qk(update, context):
    reply_user = update.message.reply_to_message
    if reply_user == None:
        if len(context.args) != 0:
            word = " "
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/Qk.mp4", "rb"), supports_streaming=True, caption="Mi qk pa ti, " + word.join(context.args))
        else:
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/Qk.mp4", "rb"), supports_streaming=True)
    else:
        if reply_user.from_user["username"] == None:
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/Qk.mp4", "rb"), supports_streaming=True, caption="Mi qk pa ti, " + reply_user.from_user["first_name"])
        else:
            context.bot.send_video(chat_id=update.effective_chat.id, video=open("./media/Qk.mp4", "rb"), supports_streaming=True,
                                   caption="Mi qk pa ti, @" + reply_user.from_user["username"] + "(" + reply_user.from_user["first_name"] + ")")


def felicidades(update, context):
    context.bot.send_video(chat_id=update.effective_chat.id, video=open(
        "./media/Felicidades.mp4", "rb"), supports_streaming=True, caption="Felicidades!")


def this(update, context):
    context.bot.send_video(chat_id=update.effective_chat.id, video=open(
        "./media/This.mp4", "rb"), supports_streaming=True, caption="This is so much cancer")


def cringe(update, context):
    reply_user = update.message.reply_to_message
    filename = random.choice(os.listdir("media/cringe"))
    video = open(f"./media/cringe/{filename}", "rb")
    if reply_user == None:
        if len(context.args) != 0:
            word = " "
            context.bot.send_video(chat_id=update.effective_chat.id, video=video,
                                   supports_streaming=True, caption="Das cringe, " + word.join(context.args))
        else:
            context.bot.send_video(
                chat_id=update.effective_chat.id, video=video, supports_streaming=True)
    else:
        if reply_user.from_user["username"] == None:
            context.bot.send_video(chat_id=update.effective_chat.id, video=video,
                                   supports_streaming=True, caption="Das cringe, " + reply_user.from_user["first_name"])
        else:
            context.bot.send_video(chat_id=update.effective_chat.id, video=video, supports_streaming=True,
                                   caption="Das cringe, @" + reply_user.from_user["username"] + "(" + reply_user.from_user["first_name"] + ")")


def mister(update, context):
    context.bot.send_video(chat_id=update.effective_chat.id, video=open(
        "./media/Mister.mp4", "rb"), supports_streaming=True, caption="El chico lindo del corbatin")


def seso(update, context):
    reply_user = update.message.reply_to_message
    if reply_user == None:
        if len(context.args) != 0:
            word = " "
            context.bot.send_video(chat_id=update.effective_chat.id, video=open("./media/Seso.mp4", "rb"),
                                   supports_streaming=True, caption="Yo no sé de eso, " + word.join(context.args) + ", hablame de seso mejor")
        else:
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/Seso.mp4", "rb"), supports_streaming=True)
    else:
        if reply_user.from_user["username"] == None:
            context.bot.send_video(chat_id=update.effective_chat.id, video=open("./media/Seso.mp4", "rb"), supports_streaming=True,
                                   caption="Yo no sé de eso, " + reply_user.from_user["first_name"] + ", hablame de seso mejor")
        else:
            context.bot.send_video(chat_id=update.effective_chat.id, video=open("./media/Seso.mp4", "rb"), supports_streaming=True,
                                   caption="Yo no sé de eso, @" + reply_user.from_user["username"] + "(" + reply_user.from_user["first_name"] + "), hablame de seso mejor")


def tiktok(update, context):
    context.bot.send_video(chat_id=update.effective_chat.id, video=open(
        "./media/Tiktok.mp4", "rb"), supports_streaming=True, caption="Te lo dice el negrito de ojos claros")


def nojoda(update, context):
    reply_user = update.message.reply_to_message
    if reply_user == None:
        if len(context.args) != 0:
            word = " "
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/Nojoda.mp4", "rb"), supports_streaming=True, caption="Que viva, " + word.join(context.args) + ", nojoda!")
        else:
            context.bot.send_video(chat_id=update.effective_chat.id, video=open(
                "./media/Nojoda.mp4", "rb"), supports_streaming=True)
    else:
        if reply_user.from_user["username"] == None:
            context.bot.send_video(chat_id=update.effective_chat.id, video=open("./media/Nojoda.mp4", "rb"),
                                   supports_streaming=True, caption="Que viva, " + reply_user.from_user["first_name"] + ", nojoda!")
        else:
            context.bot.send_video(chat_id=update.effective_chat.id, video=open("./media/Nojoda.mp4", "rb"), supports_streaming=True,
                                   caption="Que viva, @" + reply_user.from_user["username"] + "(" + reply_user.from_user["first_name"] + "), nojoda!")


def mimido(update, context):
    file = random.choice(os.listdir("media/mimido"))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(
        "./media/mimido/"+file, "rb"), caption="Zzzzzzzzzzzz")


def caro(update, context):
    video = open("./media/ta_caro.mp4", "rb")
    context.bot.send_video(chat_id=update.effective_chat.id,
                           video=video, supports_streaming=True)


def llorar(update, context):
    video = open("./media/llorar.mp4", "rb")
    context.bot.send_video(chat_id=update.effective_chat.id,
                           video=video, supports_streaming=True)


commands: List[Command] = [
    Command("doggo", "Foto random de un doggo", doggo),
    Command("neko", "Foto random de un neko", neko),
    Command("hentai", "NSFW ;)", hentai),
    Command("dollar", "Every dollar spent on...", dollar),
    Command("oilo", "Oílo", oilo),
    Command("pat", "uwu", pat),
    Command("baka", "Baka >_<", baka),
    Command("hey", "Hey, loc, qué pasa valemía", hey),
    Command("navidad", "la navidad es todo aquello", navidad),
    Command("quien", "Quién mondá es Dorian?", quien),
    Command("buenosdias", "Ohayo, darin (Chayanne)", buenosdias),
    Command("buenasnoches", "Piolín te desea buenas noches", buenasnoches),
    Command("princesas", "Comando especial para Valeria", princesas),
    Command("noticias", "Noticias icónicas de Colombia", noticias),
    Command("despegala", "Despégala, cachón", despegala),
    Command("metienesque", "Me tienes que sopletear...", butifarra),
    Command("comedia", "Donco media", comedia),
    Command("mimir", "Hora de mimir", mimir),
    Command("die", "I just wanna die", die),
    Command("uypah", "Uy, pah, lo dijiteeeeeeeee", trece),
    Command("respete", "No, señor, respete", respete),
    Command("escribebien", "Escribe bien, cachón", escribe_bien),
    Command("no", "No", no),
    Command("si", "Sí", si),
    Command("simp", "SIMP", simp),
    Command("ayno", "Ay, no, eso sí jamás", ayno),
    Command("bye", "La despego", bye),
    Command("perro", "Perro con perro", perro),
    Command("cagaste", "Cagaste, master", cagaste),
    Command("fino", "Fino, mi rey", fino),
    Command("re", "REEEEEEEEEEEEEEEEEEEEE", re_scream),
    Command("abueno", "Te me cuidas, crack", abueno),
    Command("callese", "Me tiene jodidamente mamado", callese),
    Command("horny", "Estoy horny", horny),
    Command("meto", "Hijuputa, tetra hijueputa", meto),
    Command("rico", "Rico hpta", rico),
    Command("kya", "Kya~", kya),
    Command("dato", "Qué buen dato, crack", dato),
    Command("antojaron", "Ya antojaron", antojaron),
    Command("chirrete", "Me viste cara de chirrete?", chirrete),
    Command("decepcion", "Qué decepción", decepcion),
    Command("tragatela", "Bueno, trágatela", tragatela),
    Command("sapo", "Cule sapo", sapo),
    Command("hya", "#HYAPOSTING", hya),
    Command("marica", "MARICAAAAA", marica),
    Command("chad", "Can you feel my heart", chad),
    Command("risa", "Cule risa", risa),
    Command("come", "Vaya a come mondá", come),
    Command("siono", "Sí o no", siono),
    Command("foxy", "Cute foxy", foxy),
    Command("qk", "Mi qk pa usté", qk),
    Command("felicidades", "Evangelion te felicita", felicidades),
    Command("this", "Filthy Frank", this),
    Command("cringe", "Oh no, cringe", cringe),
    Command("mister", "El chico lindo del corbatín", mister),
    Command("seso", "Yo no sé de eso, háblame de seso mejor", seso),
    Command("tiktok", "El negrito de ojos claros", tiktok),
    Command("nojoda", "Que vivan los mongólicos, nojoda!", nojoda),
    Command("mimido", "Mimido zzzzz", mimido),
    Command("llorar", "Deja de llorar, maldita puta", llorar),
    Command("caro", "Ta caro", caro),

]
