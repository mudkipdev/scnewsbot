from __init__ import __version__
from platform import python_version
from datetime import datetime
import hikari
import arc
import miru

start_time = datetime.now()
plugin = arc.GatewayPlugin("Core")
arc.loader(lambda client: client.add_plugin(plugin))
arc.unloader(lambda client: client.remove_plugin(plugin))


@plugin.include
@arc.slash_command("about", "Shows you some info about the bot.")
async def about(
    context: arc.GatewayContext,
):
    libraries = f"- Python {python_version()}\n"
    libraries += f"- Hikari {hikari.__version__}\n"
    libraries += f"- Arc {arc.__version__}\n"
    libraries += f"- Miru {miru.__version__}"

    embed = hikari.Embed(
        color=0x00DD99,
        title="About",
        description="""
            SCNewsBot is a Discord bot created for the r/starcitizen
            Discord server to help with writing news posts.
        """,
    )
    embed.add_field(name="Version", value="v" + __version__)
    embed.add_field(name="Author", value="[mudkip](https://mudkip.dev)")
    embed.add_field(name="Uptime", value=f"<t:{round(start_time.timestamp())}:R>")
    embed.add_field(name="Libraries", value=libraries)

    view = miru.View()
    view.add_item(
        miru.LinkButton(
            label="Source Code",
            url="https://github.com/mudkipdev/scnewsbot/tree/rewrite",
        )
    )

    await context.respond(
        embed=embed,
        components=view,
        flags=hikari.MessageFlag.EPHEMERAL,
    )
