
import os
from typing import List
import typing
from telegram.ext import CallbackContext
from telegram import Update
import nekos
import requests
import re
import random

from Hina import Command


def send_photo_from_url(src: str):
    """Generates a function for sending a photo from an URL"""
    def send(update: Update, context: CallbackContext):
        context.bot.send_photo(
            chat_id=update.effective_chat.id, photo=src
        )
    return send


def send_video(src: str, message=None):
    """Generates a function for sending a video with an optional message"""
    def send(update: Update, context: CallbackContext):
        if message != None:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text=message)
        context.bot.send_video(
            chat_id=update.effective_chat.id,
            video=open(f"./media/{src}", "rb"),
            supports_streaming=True
        )
    return send


def choose_photo(folder: str, message=None):
    """Generates a function for sending a photo with an optional message"""
    def send(update: Update, context: CallbackContext):
        if message != None:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text=message)
        filename = random.choice(os.listdir("./media/{folder}"))
        context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open(f"./media/{folder}/{filename}", "rb"),
        )
    return send


def choose_video(folder: str, message=None, caption=None):
    """Generates a function for sending a video with an optional message"""
    def send(update: Update, context: CallbackContext):
        if message != None:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                message=message
            )
        filename = random.choice(os.listdir("./media/{folder}"))
        context.bot.send_video(
            chat_id=update.effective_chat.id,
            video=open(f"./media/{folder}/{filename}", "rb"),
            supports_streaming=True,
            caption=caption
        )
    return send


def get_url(identifier):
    if identifier == 0:
        contents = requests.get("https://random.dog/woof.json").json()
        url = contents["url"]
        return url
    else:
        contents = requests.get("http://aws.random.cat/meow").json()
        url = contents["file"]
        return url


def get_valid_url(identifier):
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
    url = get_valid_url(0)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=url)


def neko(update, context):
    url = get_valid_url(1)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=url)


def hentai(update, context):
    tag = random.choice([
        "feet", "yuri", "trap", "futanari", "hololewd", "lewdkemo",
        "cum", "erokemo", "les", "lewdk", "lewd", "eroyuri", "eron",
        "cum_jpg", "nsfw_neko_gif", "solo", "anal", "blowjob", "pussy",
        "tits", "holoero", "pussy_jpg", "femdom", "spank", "erok", "boobs",
        "ero"
    ])
    context.bot.send_photo(
        chat_id=update.effective_chat.id, photo=nekos.img(tag))


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


def navidad(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Feliz navidad, s-senpai! uwu")
    context.bot.send_audio(chat_id=update.effective_chat.id,
                           audio=open("./media/Navidad.mp3", "rb"))


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


commands: List[Command] = [
    Command("doggo", "Foto random de un doggo", doggo),
    Command("neko", "Foto random de un neko", neko),
    Command("hentai", "NSFW ;)", hentai),
    Command("dollar", "Every dollar spent on...",
            send_photo_from_url(nekos.img('gecg'))),
    Command("oilo", "Oílo", send_photo_from_url(nekos.img('smug'))),
    Command("pat", "uwu", pat),
    Command("baka", "Baka >_<", baka),
    Command("hey", "Hey, loco, qué pasa valemía", send_video("Hey.mp4")),
    Command("navidad", "la navidad es todo aquello", navidad),
    Command("quien", "Quién mondá es Dorian?",
            send_video("Quien.mp4", message="Quién?")),
    Command("buenosdias", "Ohayo, darin (Chayanne)", choose_photo('chayanne')),
    Command("buenasnoches", "Piolín te desea buenas noches",
            choose_photo('buenas_noches')),
    Command("princesas", "Comando especial para Valeria",
            send_video("Princesas.mp4")),
    Command("noticias", "Noticias icónicas de Colombia",
            choose_photo("noticias")),
    Command("despegala", "Despégala, cachón", despegala),
    Command("metienesque", "Me tienes que sopletear...", butifarra),
    Command("comedia", "Donco media", comedia),
    Command("mimir", "Hora de mimir", send_video(
        "Mimir.mp4", "Hora de mimir! uwu")),
    Command("die", "I just wanna die", send_video(
        "Die.mp4", "Solo quiero morir :(")),
    Command("uypah", "Uy, pah, lo dijiteeeeeeeee", trece),
    Command("respete", "No, señor, respete", respete),
    Command("escribebien", "Escribe bien, cachón", send_video(
        "EscribeBien.mp4", "Escribe bien, cachón")),
    Command("no", "No", choose_photo("no")),
    Command("si", "Sí", choose_photo("yes")),
    Command("simp", "SIMP", simp),
    Command("ayno", "Ay, no, eso sí jamás", send_video("Ayno.mp4")),
    Command("bye", "La despego", send_video(
        "Bye.mp4", "La despego, chao, cachones")),
    Command("perro", "Perro con perro", send_video(
        "Perro.mp4", "Perro con perro, perro con perro")),
    Command("cagaste", "Cagaste, master", cagaste),
    Command("fino", "Fino, mi rey", fino),
    Command("re", "REEEEEEEEEEEEEEEEEEEEE", re_scream),
    Command("abueno", "Te me cuidas, crack", abueno),
    Command("callese", "Me tiene jodidamente mamado", callese),
    Command("horny", "Estoy horny", choose_video("horny", "Estoy horny.")),
    Command("meto", "Hijuputa, tetra hijueputa", send_video(
        "Meto.mp4", "A ti también te la meto")),
    Command("rico", "Rico hpta", choose_video("rico", "Rico hpta")),
    Command("kya", "Kya~", send_video("Kya.mp4", "Kya~")),
    Command("dato", "Qué buen dato, crack", dato),
    Command("antojaron", "Ya antojaron",
            choose_video("antojaron", "Ya antojaron")),
    Command("chirrete", "Me viste cara de chirrete?",
            send_video("Chirrete.mp4")),
    Command("decepcion", "Qué decepción", decepcion),
    Command("tragatela", "Bueno, trágatela", tragatela),
    Command("sapo", "Cule sapo", sapo),
    Command("hya", "#HYAPOSTING", send_video(
        "Hya.mp4", "#HYYYYYAAAAAAA_POSTING")),
    Command("marica", "MARICAAAAA", marica),
    Command("chad", "Can you feel my heart", send_video("Chad.mp4")),
    Command("risa", "Cule risa", risa),
    Command("come", "Vaya a come mondá", come),
    Command("siono", "Sí o no", siono),
    Command("foxy", "Cute foxy", foxy),
    Command("qk", "Mi qk pa usté", qk),
    Command("felicidades", "Evangelion te felicita",
            send_video("Felicidades.mp4")),
    Command("this", "Filthy Frank", send_video("This.mp4")),
    Command("cringe", "Oh no, cringe", cringe),
    Command("mister", "El chico lindo del corbatín", send_video("Mister.mp4")),
    Command("seso", "Yo no sé de eso, háblame de seso mejor", seso),
    Command("tiktok", "El negrito de ojos claros", send_video("Tiktok.mp4")),
    Command("nojoda", "Que vivan los mongólicos, nojoda!", nojoda),
    Command("mimido", "Mimido zzzzz", choose_video(
        "mimido", caption="Zzzzzzzzzzzz")),
    Command("llorar", "Deja de llorar, maldita puta",
            send_video("llorar.mp4")),
    Command("caro", "Ta caro", send_video("ta_caro.mp4")),

]
