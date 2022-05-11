# -*- coding: utf-8 -*-
"""
##Discord Hook syncer
tt_thoma's discord bot for Webhook sync
"""
import discord

from discord.ext import commands

import utils
import config
import translator
import timer

time = timer.Timer()


## Pre-load phase
print("Pre-loading 1/4")


# Logging
def log(message: str):
    current_time = time.get_current_time()
    final_message = None

    if config.timestamp:
        final_message = f"[{round(current_time, 2)}s]\n {message}"

    final_message = final_message or message
    config.write_log(final_message)
    print(final_message)


print("Pre-loading 2/4")
intents = discord.Intents.default()  # intents lol
intents.members = True

print("Pre-loading 3/4")
# Webhook integrations
webhook_to_en = discord.Webhook.from_url(config.en_webhook_url, adapter=discord.RequestsWebhookAdapter())
webhook_to_fr = discord.Webhook.from_url(config.fr_webhook_url, adapter=discord.RequestsWebhookAdapter())
webhook, content = None, ""

print("Pre-loading 4/4\n\n")
# Loading Bot

bot = commands.Bot(
    command_prefix=config.prefix,
    description="Simple discord bot, "
                "for eventually testing purposes",
    intents=intents
)

## Main

time.start()
config.write_log("\n____________________New session____________________\n")
log("Connecting")


# Displays a message when connected
@bot.event
async def on_ready():
    log(f"-----------------\n"
        f"Connexion successful!\n"
        f"Logged in as {bot.user}\n"
        f"(id {bot.user.id})\n"
        f"------------------")
    log_channel = bot.get_channel(config.logging_channel_id)
    await log_channel.send(f"**The bot has successfully (re)started!**\n"
                           f"> :ping_pong: __Ping__: {round(bot.latency * 100, 2)}ms")


@bot.event
async def on_message(message):
    global webhook, content

    triggered = False
    split_content = message.content.split(" ")
    split_content_checkup = message.content.split()

    try:
        user = bot.get_user(message.author.id) or await bot.fetch_user(message.author.id)
    except discord.NotFound:
        user = None

    if not ("nsd" in split_content and message.author.id == config.bot_id) \
            and user and not message.author.bot:
        if message.channel.id == config.fr_channel_id:
            webhook = webhook_to_en
            triggered = True

            if "nts" in split_content_checkup or "```" in split_content_checkup:
                content = utils.remove_nts(split_content)
            else:
                content = translator.translate(message.content, "fr", "en")

        elif message.channel.id == config.en_channel_id:
            webhook = webhook_to_fr
            triggered = True

            if "nts" in split_content_checkup or "```" in split_content_checkup:
                content = utils.remove_nts(split_content)
            else:
                content = translator.translate(message.content, "en", "fr")

        if triggered:
            name = message.author.nick or message.author.name
            avatar = message.author.avatar_url
            log(f"New message...\n"
                f"{name}#{message.author.discriminator}: {message.content}\n"
                f"[id]: {message.id}\n"
                f"[guild]: {message.guild.name}, {message.guild.member_count} members\n"
                f"------------------")
            utils.send_in_webhook(webhook, name, avatar, content)


# Run the bot
bot.run("tokean leak !!1!11!")
