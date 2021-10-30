
import logging
import os
from typing import Callable, List
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


def send_photo(src: str, message=None):
    """Generates a function for sending a photo with an optional message"""
    def send(update: Update, context: CallbackContext):
        if message != None:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text=message)
        context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open(f"./media/{src}", "rb"),
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
        filename = random.choice(os.listdir(f"./media/{folder}"))
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
        filename = random.choice(os.listdir(f"./media/{folder}"))
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


def reply_with(message: str, function: Callable[[Update, CallbackContext], None]):
    def send(update: Update, context: CallbackContext):
        reply_user = update.message.reply_to_message
        user = update.message.from_user
        msg = message.replace("[from]", f'@{user["username"]}')
        to = ""
        logging.info("reply_user:"+reply_user)
        if reply_user == None:
            if len(context.args) > 0:
                to = " ".join(context.args)
            else:
                msg = ""
        else:
            if reply_user.from_user["username"] == None:
                to = reply_user.from_user["first_name"]
            else:
                to = f"{reply_user.from_user['first_name']} (@{reply_user.from_user['username']})"
        msg = msg.replace("[to]", to)
        if msg != "":
            context.bot.send_message(
                chat_id=update.effective_chat.id, text=msg)
        function(update, context)()
    return send


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


commands: List[Command] = [
    Command("doggo", "Foto random de un doggo", doggo),
    Command("neko", "Foto random de un neko", neko),
    Command("hentai", "NSFW ;)", hentai),
    Command("dollar", "Every dollar spent on...",
            send_photo_from_url(nekos.img('gecg'))),
    Command("oilo", "Oílo", send_photo_from_url(nekos.img('smug'))),
    Command("pat", "uwu", reply_with("[from] is patting [to] uwu",
                                     send_photo_from_url(nekos.img("pat")))),
    Command("baka", "Baka >_<", reply_with(
        "B-b-baka, [to]! >_<", send_photo_from_url(nekos.img("baka")))),
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
    Command("metienesque", "Me tienes que sopletear...",
            reply_with("Hey, [to]", send_video("Butifarra.mp4"))),
    Command("comedia", "Donco media", reply_with(
        "Jajaja cule chiste hpta, [to]", choose_video("comedia"))),
    Command("mimir", "Hora de mimir", send_video(
        "Mimir.mp4", "Hora de mimir! uwu")),
    Command("die", "I just wanna die", send_video(
        "Die.mp4", "Solo quiero morir :(")),
    Command("uypah", "Uy, pah, lo dijiteeeeeeeee", reply_with(
        "Uy, pah, LO DIJITEEEEEEE ([to])", send_video("Trece.mp4"))),
    Command("respete", "No, señor, respete", reply_with(
        "Respeta, [to], cachón", send_video("Respete.mp4"))),
    Command("escribebien", "Escribe bien, cachón", send_video(
        "EscribeBien.mp4", "Escribe bien, cachón")),
    Command("no", "No", choose_photo("no")),
    Command("si", "Sí", choose_photo("yes")),
    Command("simp", "SIMP", reply_with("SIMP, [to]", choose_photo("simp"))),
    Command("ayno", "Ay, no, eso sí jamás", send_video("Ayno.mp4")),
    Command("bye", "La despego", send_video(
        "Bye.mp4", "La despego, chao, cachones")),
    Command("perro", "Perro con perro", send_video(
        "Perro.mp4", "Perro con perro, perro con perro")),
    Command("cagaste", "Cagaste, master", reply_with(
        "Cagaste, [to]", choose_photo("cagaste"))),
    Command("fino", "Fino, mi rey", reply_with(
        "Fino, mi rey ([to])", choose_photo("fino"))),
    Command("re", "REEEEEEEEEEEEEEEEEEEEE", re_scream),
    Command("abueno", "Te me cuidas, crack", reply_with(
        "Te me cuidas, crack ([to])", choose_photo("abueno"))),
    Command("callese", "Me tiene jodidamente mamado", reply_with(
        "Cállese, [to], me tiene jodidamente mamado", choose_video("callese"))),
    Command("horny", "Estoy horny", choose_video("horny", "Estoy horny.")),
    Command("meto", "Hijuputa, tetra hijueputa", send_video(
        "Meto.mp4", "A ti también te la meto")),
    Command("rico", "Rico hpta", choose_video("rico", "Rico hpta")),
    Command("kya", "Kya~", send_video("Kya.mp4", "Kya~")),
    Command("dato", "Qué buen dato, crack", reply_with(
        "Datazo, crack, pero nadie te preguntó, cv ([to])", choose_video("dato"))),
    Command("antojaron", "Ya antojaron",
            choose_video("antojaron", "Ya antojaron")),
    Command("chirrete", "Me viste cara de chirrete?",
            send_video("Chirrete.mp4")),
    Command("decepcion", "Qué decepción", reply_with(
        "Decepcionado de ti, [to]", send_video("Decepcion.mp4"))),
    Command("tragatela", "Bueno, trágatela", reply_with(
        "Bueno, trágatela ([to])", choose_video("tragatela"))),
    Command("sapo", "Cule sapo", reply_with(
        "Cule sapo, [to]", choose_video("sapo"))),
    Command("hya", "#HYAPOSTING", send_video(
        "Hya.mp4", "#HYYYYYAAAAAAA_POSTING")),
    Command("marica", "MARICAAAAA", reply_with(
        "MMMMMJUMMMMMMM ([to])", choose_video("marica"))),
    Command("chad", "Can you feel my heart", send_video("Chad.mp4")),
    Command("risa", "Cule risa", reply_with(
        "Cule risa, [to]", send_video("Risa.mp4"))),
    Command("come", "Vaya a come mondá", reply_with(
        "Vaya a come' mondá, [to]", send_video("Come.mp4"))),
    Command("siono", "Sí o no", siono),
    Command("foxy", "Cute foxy", foxy),
    Command("qk", "Mi qk pa usté", reply_with(
        "Mi qk pa ti, [to]", send_video("Qk.mp4"))),
    Command("felicidades", "Evangelion te felicita",
            send_video("Felicidades.mp4")),
    Command("this", "Filthy Frank", send_video("This.mp4")),
    Command("cringe", "Oh no, cringe", reply_with(
        "Das cringe, [to]", choose_video("cringe"))),
    Command("mister", "El chico lindo del corbatín", send_video("Mister.mp4")),
    Command("seso", "Yo no sé de eso, háblame de seso mejor",
            reply_with("Yo no sé de eso, [to]", send_video("Seso.mp4"))),
    Command("tiktok", "El negrito de ojos claros", send_video("Tiktok.mp4")),
    Command("nojoda", "Que vivan los mongólicos, nojoda!", reply_with(
        "Que vida [to], nojoda!", send_video("Nojoda.mp4"))),
    Command("mimido", "Mimido zzzzz", choose_video(
        "mimido", caption="Zzzzzzzzzzzz")),
    Command("llorar", "Deja de llorar, maldita puta",
            send_video("llorar.mp4")),
    Command("caro", "Ta caro", send_video("ta_caro.mp4")),
]
