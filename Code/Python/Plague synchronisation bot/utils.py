# -*- coding: utf-8 -*-
import time


def check_if_number(string):  # useful function to avoid some issues
    try:
        int(string)
        return True
    except ValueError:
        return False


def send_in_webhook(webhook, name, avatar_url, content):  # Bruh
    webhook.send(username=name, avatar_url=avatar_url, content=content)


def remove_nts(item_list: list):
    return_thing = ""
    try:
        item_list.remove("nts")
        for thing in item_list:
            return_thing += thing + " "
    except ValueError:
        for thing in item_list:
            return_thing += thing + " "

    return return_thing
