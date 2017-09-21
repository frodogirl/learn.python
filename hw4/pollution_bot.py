from air_pollution import get_json_data_from_server, SOURCE_URL
from air_pollution import make_pollution_dict, calculate_pollution_level

# За основу можно использовать код уже существующего бота
# При запуске, бот должен один раз получить и обоработать данные
# с портала Открытых Данных, используюя функции из предыдущей задачи

# После этого, он должен ждать сообщения с названием района, пытаться
# найти данные о нем в словаре. И если данные найдены - отправлять
# одно многострочное сообщение, в котором на каждой строке - название
# загрязнения и его уровень, включая взвешенное.

import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep

update_id = None

def echo(bot, leveled_pollution):
    global update_id
    # Request updates after the last update_id
    for update in bot.getUpdates(offset=update_id, timeout=10):
        # chat_id is required to reply to any message
        chat_id = update.message.chat_id
        update_id = update.update_id + 1
        
        if update.message:  # your bot can receive updates without messages
            # Reply to the message
            if (update.message.text in leveled_pollution.keys()):   
                all_pollution = leveled_pollution[update.message.text]
                for pollution_name in all_pollution.keys():
                    pollution_value = all_pollution.get(pollution_name)
                    bot.sendMessage(chat_id=chat_id, text=pollution_name + ': ' + str(pollution_value))


if __name__ == '__main__':

    #global update_id
    # Telegram Bot Authorization Token
    bot = telegram.Bot('220792881:AAFsfLEdRq6pO8Wjqk1Ff6xpM7S94l5RDPM')
    
    # get the first pending update_id, this is so we can skip over it in case
    # we get an "Unauthorized" exception.
    try:
        update_id = bot.getUpdates()[0].update_id
    except IndexError:
        update_id = None

    raw_data = get_json_data_from_server(SOURCE_URL)
    pollution = make_pollution_dict(raw_data)
    leveled_pollution = calculate_pollution_level(pollution)

    while True:
        try:
            echo(bot, leveled_pollution)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # The user has removed or blocked the bot.
            update_id += 1

