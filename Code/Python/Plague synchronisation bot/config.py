# -*- coding:utf-8 -*-
import json
"""
Discord bot configuration
=========================

##Everything needed in the config
"""
with open("config.json") as json_file:
    global_config = json.load(json_file)

prefix = "?"

fr_webhook_url = global_config["webhooks"]["fr"]
en_webhook_url = global_config["webhooks"]["en"]

bot_id = global_config["IDs"]["bot"]
fr_channel_id = global_config["IDs"]["fr_channel"]
en_channel_id = global_config["IDs"]["en_channel"]

logging_channel_id = global_config["IDs"]["logging_channel"]
timestamp = global_config["logs"]["timestamps"]


def write_log(thing: str):
    log_file = open(global_config["logs"]["filename"]+".log", "a")
    log_file.write(thing+"\n")
    log_file.close()
