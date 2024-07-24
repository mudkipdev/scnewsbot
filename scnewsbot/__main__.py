import os
from dotenv import load_dotenv
from hikari import GatewayBot, Intents
import arc


EXTENSIONS = ("core",)


def main() -> None:
    load_dotenv()
    token = os.getenv("DISCORD_TOKEN")

    if not token:
        print("Please set a DISCORD_TOKEN environment variable.")
        exit(1)

    if os.name != "nt":
        import uvloop

        uvloop.install()

    bot = GatewayBot(intents=Intents.ALL_UNPRIVILEGED, token=token)
    client = arc.GatewayClient(bot)

    for extension in EXTENSIONS:
        client.load_extension(extension)

    bot.run()


if __name__ == "__main__":
    main()
