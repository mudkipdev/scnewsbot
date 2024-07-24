import os
from hikari import GatewayBot, Intents
from dotenv import load_dotenv


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
    bot.run()


if __name__ == "__main__":
    main()
