# -*- coding: utf-8 -*-
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep


update_id = None


def echo(bot):
    global update_id
    # Request updates after the last update_id
    for update in bot.getUpdates(offset=update_id, timeout=10):
        # chat_id is required to reply to any message
        chat_id = update.message.chat_id
        update_id = update.update_id + 1

        if update.message:  # your bot can receive updates without messages
            # Reply to the message
            bot.sendMessage(chat_id=chat_id, text=update.message.text)


if __name__ == '__main__':
    global update_id
    # Telegram Bot Authorization Token
    bot = telegram.Bot('220792881:AAFsfLEdRq6pO8Wjqk1Ff6xpM7S94l5RDPM')

    # get the first pending update_id, this is so we can skip over it in case
    # we get an "Unauthorized" exception.
    try:
        update_id = bot.getUpdates()[0].update_id
    except IndexError:
        update_id = None

    while True:
        try:
            echo(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # The user has removed or blocked the bot.
            update_id += 1
