import logging
from os import getenv
from typing import Callable
from telegram.bot import Bot
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.updater import Updater
from telegram.update import Update
from dataclasses import dataclass

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s,"
)
logger = logging.getLogger()


@dataclass
class Command:
    """Class for keeping track of a command"""
    name: str
    description: str
    callback: Callable[[Update, CallbackContext], None]


class Hina:
    def __init__(self, token: str, mode: str = "dev"):
        self.bot = Bot(token=token)
        self.mode = mode
        self.updater = Updater(self.bot.token, use_context=True)
        self.help = "Senpai, estos son los comandos u//u:"

    def run(self):
        self.add_command(
            Command(
                "taskete",
                "Muestra esta ayuda",
                lambda update, _: update.message.reply_text(self.help)
            )
        )
        if self.mode == "dev":
            self.updater.start_polling()
            self.updater.idle()
        elif self.mode == "prod":
            PORT = int(getenv("PORT", "8443"))
            HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
            TOKEN = self.bot.token
            self.updater.start_webhook(
                listen="0.0.0.0", port=PORT, url_path=TOKEN)
            self.updater.bot.set_webhook(
                f"https://{HEROKU_APP_NAME}.herokuapp.com/{TOKEN}")
        else:
            logger.info('Mode not specified')

    def add_command(self, command: Command):
        self.help += f"\n /{command.name} - {command.description}"
        self.updater.dispatcher.add_handler(command.callback)
