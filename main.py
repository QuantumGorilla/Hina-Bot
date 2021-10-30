import os
from Hina import Hina
from commands import commands


def main():
    TOKEN = os.getenv("TOKEN")
    mode = os.getenv("MODE")
    hina = Hina(TOKEN, mode=mode)
    hina.add_commands(commands)
    hina.run()


if __name__ == '__main__':
    main()
